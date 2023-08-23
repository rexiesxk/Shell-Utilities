
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:56:00 2023
This script splits huge json files running into GBs . 

It reads the file line by line instead of loading the file completely into memory.

You also have an option of keepin the header in split files

@author: RexieSxK
"""
import os
import shutil

def split_file_by_lines(filename, max_lines, with_header=True):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        header = f.readline() if with_header else None
        count = 0
        file_num = 1
        output = None

        for line in f:
            if count == 0:
                output_filename = f"{filename}_part{file_num}.json"
                output = open(output_filename, 'w', encoding='utf-8')
                if header:
                    output.write(header)
                file_num += 1

            output.write(line)
            count += 1

            if count >= max_lines:
                output.close()
                count = 0

        if output:
            output.close()

def split_file_by_size(filename, max_size_kb, with_header=True):
    max_size = max_size_kb * 1024  # convert KB to Bytes
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        header = f.readline() if with_header else None
        buffer = []
        total_size = 0
        file_num = 1

        for line in f:
            line_size = len(line.encode('utf-8'))
            if total_size + line_size > max_size:
                output_filename = f"{filename}_part{file_num}.json"
                with open(output_filename, 'w', encoding='utf-8') as output:
                    if header:
                        output.write(header)
                    for buf_line in buffer:
                        output.write(buf_line)
                buffer = []
                total_size = 0
                file_num += 1

            buffer.append(line)
            total_size += line_size

        if buffer:
            output_filename = f"{filename}_part{file_num}.json"
            with open(output_filename, 'w', encoding='utf-8') as output:
                if header:
                    output.write(header)
                for buf_line in buffer:
                    output.write(buf_line)

def main():
    filename = input("Enter the JSON filename: ")
    choice = input("Choose split criterion - 'lines' or 'size': ")

    with_header = input("Include header in each split file? (yes/no): ").strip().lower() == "yes"

    if choice == 'lines':
        max_lines = int(input("Enter the maximum number of lines per split file: "))
        split_file_by_lines(filename, max_lines, with_header)
    elif choice == 'size':
        max_size_kb = int(input("Enter the maximum size (in KB) per split file: "))
        split_file_by_size(filename, max_size_kb, with_header)
    else:
        print("Invalid choice!")
        return

    # Move original file and script to "done" folder
    if not os.path.exists("done"):
        os.mkdir("done")

    shutil.move(filename, os.path.join("done", filename))
    shutil.move(__file__, os.path.join("done", os.path.basename(__file__)))

    print("Splitting completed. Original file and script have been moved to 'done' folder.")

if __name__ == '__main__':
    main()
