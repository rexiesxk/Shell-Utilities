
# Utilities

This repository consists of tutorials, resources , python,perl and shell scripts and command snippets for building system utilities.

## CAUTION : Always make a backup copy of your files and folders before running the scripts. 
### While using renamers make sure you're not renaming any essential system or program files and folders.
### Renamer scripts should be used to avoid mundane redundancy where the name or order of the file is not that significant.
### Never run these scripts in the root folder or top hierarchial folder of your drive. 
### Copy the script in the desired folder and run with cmd/shell or any ide.

## List of  Utilities 

1. [Splitter](https://github.com/rexiesxk/Shell-Utilities/tree/main/Splitter)

This python script splits huge text/csv files into smaller size as per user input.

The original text file and the script should be in the same directory. 

The output is redirected into a new directory, "splitfiles", and directory is created if not present.

2. [Renamers](https://github.com/rexiesxk/Shell-Utilities/tree/main/Renamers)

This folder contains a few bulk-renamer and lister scripts.

Each of them can be used independently as per requirement.

  - [list1.py](https://github.com/rexiesxk/Shell-Utilities/blob/main/Renamers/list1.py)

      This program list the name of all the folders in the current directory 
      
      and redirects the output in a text file namesd 'list.txt' 

      It handles almost all the foreign languages 'characters. Let me know if you face any encoding error.
  
   - [list2.py](https://github.com/rexiesxk/Shell-Utilities/blob/main/Renamers/list2.py)

      This programs lists all the names of folders in a directoy, 
      
      then copies all the files from original directory to new directories with _test and _train appended to them, 

      then it renames the files in newly created folders as per new folder names and preserves the extension. 
      
      If any original folder is empty, it saves their names to list2.txt

  - [SeqRenamer.py](https://github.com/rexiesxk/Shell-Utilities/blob/main/Renamers/SeqRenamer.py)

    This file renames the files in the current directory sequentially.

    First it sorts the files alphabetically, time modified or size based on user input.

    Then it renames the files taking the  base name of  top sorted file as first file.

  - [searchist.py](https://github.com/rexiesxk/Utilities/blob/main/Search_Sort_Split/searchist.py)

     This script sort outs scraped or downloaded data containing mixed filetypes

     and moves them into respective folders.
    
     It also cleans up long and invalid names. It creates directories for filetypes
    
     and lists out contents of the folders respectively. 

     Use Sudo in linux or Run powershell or ide as administrator to execute the script
      

