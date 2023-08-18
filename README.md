
# Shell-Utilities

This repository consists of tutorials, resources , python,perl and shell scripts and command snippets for building system utilities.


## List of  Utilities 

1. [Splitter](https://github.com/rexiesxk/Shell-Utilities/tree/main/Splitter)

This python script splits huge text/csv files into smaller size as per user input.

The original text file and the script should be in the same directory. 

The output is redirected into a new directory, "splitfiles", and directory is created if not present.

2. [Renamers](https://github.com/rexiesxk/Shell-Utilities/tree/main/Renamers)

This folder contains a few bulk-renamer and lister scripts.

Each of them can be used independently as per requirement.

  [list1.py](https://github.com/rexiesxk/Shell-Utilities/blob/main/Renamers/list1.py)

      This program list the name of all the folders in the current directory 
      
      and redirects the output in a text file namesd 'list.txt' 

      It handles almost all the foreign languages 'characters. Let me know if you face any encoding error.
  
   [list2.py](https://github.com/rexiesxk/Shell-Utilities/blob/main/Renamers/list2.py)

      This programs lists all the names of folders in a directoy, 
      
      then copies all the files from original directory to new directories with _test and -train appended to them, 

      then it renames the filesin newly created folders as per new folder names and preserves the extension. 
      
      If any original folder is empty, it saves their names to list2.txt

