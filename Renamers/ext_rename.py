# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:16:55 2023
  This renames all files in the curent directory to have new extension
  For example .jpg to .png. Doesn't prompt for any system confirmation
@author: RexieSxK
"""

import os

def bulk_rename(new_extension):
    
    for filename in os.listdir(os.getcwd()):
        base, ext = os.path.splitext(filename)
        if ext:  # Ensure it's a file with an extension
            new_filename = f"{base}.{new_extension}"
            os.rename(filename, new_filename)
            print(f"Renamed {filename} to {new_filename}")

def main():
    new_extension = input("Enter the new file extension (without the dot): ")
    bulk_rename(new_extension)
    print("Finished renaming files.")

if __name__ == "__main__":
    main()
