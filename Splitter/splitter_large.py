# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:25:57 2023
This script splits huge text files running into GBs . It reads the file line by line instead of loading the file completely into memory
@author: Rexie
"""

import os

def split_file_by_size(source_filepath, dest_folder, split_file_prefix, size_per_file, keep_header=True):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    with open(source_filepath, 'r', encoding='utf-8') as source_file:
        header = source_file.readline()
        
        # Initialize file count based on existing files in the output directory and names the new file sequentially
        existing_files = [f for f in os.listdir(dest_folder) if f.startswith(split_file_prefix) and f.endswith('.txt')]
        file_count = len(existing_files)
        
        current_out_path = os.path.join(dest_folder, f"{split_file_prefix}_{file_count}.txt")
        current_out_file = open(current_out_path, 'w', encoding='utf-8')
        
        if keep_header:
            current_out_file.write(header)
            
        current_size = 0
        for line in source_file:
            current_out_file.write(line)
            current_size += len(line)
            
            if current_size >= size_per_file:
                current_out_file.close()
                file_count += 1
                current_out_path = os.path.join(dest_folder, f"{split_file_prefix}_{file_count}.txt")
                current_out_file = open(current_out_path, 'w', encoding='utf-8')
                
                if keep_header:
                    current_out_file.write(header)
                    current_size = len(header)
                else:
                    current_size = 0
        current_out_file.close()

if __name__ == "__main__":
    while True:
        file_name = input("Enter the complete filename (with .csv or .txt extension) to split : ") # It should be in the current directory
        full_path = os.path.join(os.getcwd(), file_name)
        
        # Check if file exists and if it has a valid extension
        if not os.path.exists(full_path):
            print(f"File '{file_name}' not found in the current directory.")
            continue
        elif not (file_name.endswith('.csv') or file_name.endswith('.txt')):
            print(f"File '{file_name}' is not a valid .csv or .txt file.")
            continue

        try:
            size_mb = float(input("Enter desired size of each split file in MB : ")) # e.g., 1 for 1MB/ 0.5 for 500KB 
            size_bytes = int(size_mb * 1024 * 1024)
        except ValueError:
            print("Please enter a valid number for the size.")
            continue
# if you want the top of the file(name of columns) to be included  in each file, write yes ; if there are no column names , write no
        keep_header_input = input("Do you want to keep the header in each split file? (yes/no): ").lower()
        keep_header = keep_header_input.startswith('y')

        split_file_by_size(full_path, "splitfiles", file_name, size_bytes, keep_header)

        another_input = input("Do you want to split another file? (yes/no): ").lower()
        if another_input.startswith('n'):
            break
