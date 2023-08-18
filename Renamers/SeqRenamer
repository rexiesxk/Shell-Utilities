# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:17:27 2023
This file renames the files in the current directory sequentially.

First it sorts the files alphabetically, time modified or size based on user input.

Then it renames the files taking the  base name of  top sorted file as first file.
@author: RexieSxk
"""
import os

def sort_by_name(files):
    return sorted(files)

def sort_by_date(files):
    return sorted(files, key=lambda x: os.path.getmtime(x))

def sort_by_size(files):
    return sorted(files, key=lambda x: os.path.getsize(x))

def rename_files(sorted_files):
    base_name = os.path.splitext(sorted_files[0])[0]
    ext = os.path.splitext(sorted_files[0])[1]

    # Rename the remaining files
    for count, file in enumerate(sorted_files[1:], start=2):
        if not file.endswith('.py'):
            new_name = f"{base_name}_{count}{ext}"
            os.rename(file, new_name)

def main():
    files = [f for f in os.listdir() if os.path.isfile(f) and not f.endswith('.py')]
    if not files:
        print("No valid files found in the current directory.")
        return

    print("Choose the criteria for renaming:")
    print("1: Alphabetically Ascending Order")
    print("2: Time Modified from Oldest to Latest")
    print("3: By File Size Ascending Order")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        sorted_files = sort_by_name(files)
    elif choice == '2':
        sorted_files = sort_by_date(files)
    elif choice == '3':
        sorted_files = sort_by_size(files)
    else:
        print("Invalid choice!")
        return

    rename_files(sorted_files)
    print("Files renamed successfully!")

if __name__ == "__main__":
    main()

