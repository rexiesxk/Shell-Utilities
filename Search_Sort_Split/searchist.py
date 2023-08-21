# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:05:18 2023
This script sort outs scraped or downloaded data and moves them into respective folders. 
It also cleans up long and invalid names. It creates directories for filetypes 
and lists out contents of the folders respectively. 
Use Sudo in linux or Run powershell or ide as administrator to execute the script
@author: RexieSxK
"""
import os
import shutil
import platform
import sys
import string
import hashlib

def is_admin():
    """Check if the script has elevated privileges."""
    if platform.system() == 'Windows':
        try:
            os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\\windows'), 'temp']))
        except:
            return False
        else:
            return True
    else:
        if 'SUDO_UID' in os.environ.keys():
            return True
        else:
            return False

def get_valid_filename(s):
    """Generate a valid filename from the given string."""
    s = str(s).strip().replace(' ', '_')
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    if len(s) > 240:
        name, ext = os.path.splitext(s)
        hashed_name = hashlib.md5(name.encode()).hexdigest()
        s = f"{hashed_name}{ext}"
    return s

def move_files_by_type(base_path):
    """Sort and move files by type. Comment out filetype you don't need for the task."""
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.tiff', '.webp', '.bmp', '.gif', '.ico', '.jfif', '.svg'],
        'Documents': ['.txt', '.doc', '.pdf', '.docx', '.djvu', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Databases': ['.db', '.sql', '.mdb', '.accdb', '.sqlite', '.dbf', '.odb', '.myd', '.fp7', '.nsf'],
        'Videos': ['.mp4', '.mkv', '.avi', '.flv', '.mov', '.wmv', '.m4v', '.3gp', '.h264', '.rm'],
        'Audios': ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac', '.wma', '.aiff', '.ra', '.mid'],
        'Executables': ['.exe', '.msi', '.jar', '.bat', '.sh', '.app', '.apk', '.cgi', '.com', '.wsf'],
        'Backups': ['.bak', '.tmp', '.bup', '.tib', '.bkp', '.bac', '.tbk', '.save', '.tar', '.gz'],
        'Archives': ['.zip', '.rar', '.7z', '.tar.gz', '.iso', '.bin', '.dmg', '.pkg', '.rpm', '.deb'],
        'Web Files': ['.html', '.htm', '.css', '.js', '.php', '.asp', '.aspx', '.jsp', '.cfm'],
        'XML and Data': ['.xml', '.json', '.yml', '.yaml', '.csv', '.ini', '.plist']
    }

    global_list = {}

    for file_type, extensions in file_types.items():
        dir_name = f"Sorted {file_type}"
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        
        global_list[file_type] = []

        for root, _, files in os.walk(base_path):
            for filename in files:
                if any(filename.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, filename)

                    # Create a valid destination filename
                    destination_filename = get_valid_filename(filename)
                    destination_path = os.path.join(dir_path, destination_filename)

                    # Check if the file already exists in the destination directory
                    counter = 1
                    base, ext = os.path.splitext(destination_path)
                    while os.path.exists(destination_path):
                        destination_path = f"{base} ({counter}){ext}"
                        counter += 1

                    shutil.move(file_path, destination_path)
                    global_list[file_type].append(os.path.basename(destination_path))

        with open(os.path.join(dir_path, 'list.txt'), 'w', encoding='utf-8') as list_file:
            for filename in global_list[file_type]:
                list_file.write(filename + '\n')

    with open(os.path.join(base_path, 'globallist.txt'), 'w', encoding='utf-8') as global_file:
        for file_type, files in global_list.items():
            global_file.write(file_type + ':\n')
            for filename in files:
                global_file.write(filename + '\n')
            global_file.write('\n')

if __name__ == "__main__":
    if not is_admin():
        print("The script needs to be run with elevated privileges!")
        sys.exit()

    user_input = input("Enter a directory path (or press enter to use the current directory): ")
    path = user_input if user_input else os.getcwd()
    
    if os.path.exists(path):
        move_files_by_type(path)
        print("Files sorted successfully!")
    else:
        print(f"Path '{path}' does not exist.")

