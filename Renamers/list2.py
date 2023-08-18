# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:27:56 2023
This programs lists all the names of folders in a directoy, then copies all the files from original directory to new directories with test and train appended to them, 
then it renames the filesin newly created folders as per new folder names and preserves the extension. 
If any original folder is empty, it saves their names to list2.txt
@author: RexieSxk
"""
import os
import shutil

def list_directories(path):
    """Returns a sorted list of all folder names in the given path."""
    entries = os.listdir(path)
    dirs = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    dirs.sort()
    return dirs

def save_to_file(folders, output_file):
    """Saves the list of folder names to the output file using utf-8 encoding."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for folder in folders:
            f.write(folder + '\n')

def create_new_folders_and_copy_files(original_path, new_folders):
    """Creates new folders _test and _train for each directory and copies files."""
    empty_folders = []
    for folder in new_folders:
        test_folder = os.path.join(original_path, folder + '_test')
        train_folder = os.path.join(original_path, folder + '_train')

        # Create _test and _train directories
        os.makedirs(test_folder, exist_ok=True)
        os.makedirs(train_folder, exist_ok=True)

        original_folder_path = os.path.join(original_path, folder)
        files = [f for f in os.listdir(original_folder_path) if os.path.isfile(os.path.join(original_folder_path, f))]

        if not files:
            empty_folders.append(folder)
            continue

        # Copy files to the new folders and rename them sequentially
        for idx, file in enumerate(files, 1):
            _, ext = os.path.splitext(file)
            
            shutil.copy2(os.path.join(original_folder_path, file), test_folder)
            shutil.copy2(os.path.join(original_folder_path, file), train_folder)

            os.rename(os.path.join(test_folder, file), os.path.join(test_folder, f"{folder}_test_{idx}{ext}"))
            os.rename(os.path.join(train_folder, file), os.path.join(train_folder, f"{folder}_train_{idx}{ext}"))

    return empty_folders

def main():
    # Get the current directory
    directory_path = os.getcwd()

    # Output will be saved to 'list.txt' and 'list2.txt' in the current directory
    output_file_path = os.path.join(directory_path, "list.txt")
    output_file_path2 = os.path.join(directory_path, "list2.txt")

    folders = list_directories(directory_path)
    save_to_file(folders, output_file_path)

    empty_folders = create_new_folders_and_copy_files(directory_path, folders)

    # Save empty folder names to list2.txt
    save_to_file(empty_folders, output_file_path2)

    print(f"Folder names have been saved to {output_file_path}")
    if empty_folders:
        print(f"Empty folder names have been saved to {output_file_path2}")

if __name__ == "__main__":
    main()
