# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:12:56 2023
This script converts mdb files into csv files and splits the csv files

as per user input: size/number of lines. 

@author: Rexie
"""
import os
import csv
import pyodbc
import shutil
import sys

def has_write_permission(directory):
    test_file = os.path.join(directory, 'temp_test.txt')
    try:
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return True
    except:
        return False

def mdb_to_csv(mdb_path, output_folder):
    # Connect to the MDB file using ODBC
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + mdb_path + ';'
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Get the list of tables in the MDB
    table_list = [row.table_name for row in cursor.tables(tableType='TABLE')]

    for table_name in table_list:
        print(f"Converting {table_name} to CSV...")
        
        # Create CSV file for the table
        csv_path = os.path.join(output_folder, table_name + '.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Get columns
            columns = [column.column_name for column in cursor.columns(table=table_name)]
            csv_writer.writerow(columns)
            
            # Fetch rows from the table
            cursor.execute(f"SELECT * FROM {table_name}")
            for row in cursor.fetchall():
                csv_writer.writerow(row)

    cursor.close()
    conn.close()

def split_csv(filename, delimiter=',', row_limit=None, size_limit=None, output_name_template='output_%s.csv'):
    with open(filename, 'r', encoding='utf-8') as source:
        reader = csv.reader(source, delimiter=delimiter)
        headers = next(reader)
        
        current_piece = 1
        current_out_path = output_name_template % current_piece
        current_out_writer = csv.writer(open(current_out_path, 'w', encoding='utf-8'), delimiter=delimiter)
        current_out_writer.writerow(headers)
        
        current_size = 0
        current_rows = 0
        for row in reader:
            current_rows += 1
            current_size += sum(len(s) for s in row)
            
            if (row_limit and current_rows > row_limit) or (size_limit and current_size > size_limit*1024):
                current_piece += 1
                current_out_path = output_name_template % current_piece
                current_out_writer = csv.writer(open(current_out_path, 'w', encoding='utf-8'), delimiter=delimiter)
                current_out_writer.writerow(headers)
                current_size = 0
                current_rows = 0
                
            current_out_writer.writerow(row)

def main():
    # Check platform
    platform = sys.platform
    if platform == 'win32':
        print("Running on Windows.")
    elif platform.startswith('linux'):
        print("Running on Linux.")
    else:
        print(f"Running on {platform}.")
    
    current_directory = os.getcwd()
    
    # Check permissions
    if not has_write_permission(current_directory):
        print(f"No write permissions in {current_directory}. Please check your permissions.")
        return
    
    mdb_files = [file for file in os.listdir(current_directory) if file.endswith('.mdb')]
    
    # Ask user for splitting preference
    choice = input("Do you want to split by size (enter 's') or by number of lines (enter 'l')? ")
    if choice == 's':
        size = int(input("Enter the maximum size (in KB) for each split file: "))
    elif choice == 'l':
        lines = int(input("Enter the maximum number of lines for each split file: "))
    
    for mdb_file in mdb_files:
        print(f"Processing {mdb_file}...")
        mdb_path = os.path.join(current_directory, mdb_file)
        
        # Check read permissions on mdb file
        if not os.access(mdb_path, os.R_OK):
            print(f"No read permissions for {mdb_file}. Skipping.")
            continue

        # Convert to CSV
        mdb_to_csv(mdb_path, current_directory)

        csv_files = [f for f in os.listdir(current_directory) if f.endswith('.csv') and not os.path.exists(os.path.join(current_directory, 'done', f))]

        for csv_file in csv_files:
            print(f"Splitting {csv_file}...")
            
            # Split CSV based on user's choice
            if choice == 's':
                split_csv(csv_file, size_limit=size, output_name_template=csv_file.replace('.csv', '_%s.csv'))
            elif choice == 'l':
                split_csv(csv_file, row_limit=lines, output_name_template=csv_file.replace('.csv', '_%s.csv'))

        # Move mdb and original csv to "done" folder
        done_dir = os.path.join(current_directory, 'done')
        if not os.path.exists(done_dir):
            os.makedirs(done_dir)
        shutil.move(mdb_path, done_dir)
        for csv_file in csv_files:
            shutil.move(csv_file, done_dir)

if __name__ == "__main__":
    main()
