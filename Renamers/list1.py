# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:10:04 2023
This program list the name of all the folders in the current directory and redirects the output in a text file namesd 'list.txt' 
It handles almost all the foreign character. Let me know if you face any encoding error.
@author: RexieSxk
"""

import os

def list_directories(path):
    """
    Returns a sorted list of all folder names in the given path.
    """
    # List all entries in the directory
    entries = os.listdir(path)

    # Filter out only the directories
    dirs = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]

    # Sort them alphabetically
    dirs.sort()

    return dirs

def save_to_file(folders, output_file):
    """
    Saves the list of folder names to the output file using utf-8 encoding.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for folder in folders:
            f.write(folder + '\n')

def main():
    # Get the current directory
    directory_path = os.getcwd()

    # Output will be saved to 'list.txt' in the current directory
    output_file_path = os.path.join(directory_path, "list.txt")

    folders = list_directories(directory_path)
    save_to_file(folders, output_file_path)

    print(f"Folder names have been saved to {output_file_path}")

if __name__ == "__main__":
    main()
