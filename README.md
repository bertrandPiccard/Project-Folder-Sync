# Introduction

This project aims to provide a script able to synchronize two folders, a source and a replica. The content has to be identical after each synchronization and the sync is based on the source folder. 

More details on the requirements:

- Synchronization is one way, from a source to a replica. After synchronization the content of the two folders has to match

- Synchronization should be performed periodically

- File creation/copying/removal operations should be logged to a file and to the console output

- Folder paths, synchronization intervals and log file path should be provided using the command line arguments;
- No usage of third-party libraries that implement folder synchronization
- It is allowed (and recommended) to use external libraries implementing other well-known algorithms 

# Librairies
In this project the following libraries have been used.

- [logging](https://docs.python.org/3/howto/logging.html)

- [sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys) : 

- [filecmp](https://docs.python.org/3/library/filecmp.html?highlight=filecmp#module-filecmp)

- [os](https://docs.python.org/3/library/os.html?highlight=os#module-os)

- [shutil](https://docs.python.org/3/library/shutil.html?highlight=shutil)

- [argparse](https://docs.python.org/3/library/argparse.html?highlight=argpars)

- [time](https://docs.python.org/3/library/time.html?highlight=time#module-time)

# How to use
When the project is available locally, open the terminal on the path of the folder. 

The script can be executed with the following command (example):

``` 
python main.py -s "C:\Users\Bertrand\Desktop\Source" -r "C:\Users\Bertrand\Desktop\Replica" -l
 "C:\Users\Bertrand\Desktop\Log" -i 6

 ```

Make sure the all the folders are created beforehand. If the path is not existing or invalid, the script will stop before the synchronization and a message will be printed in the terminal. Also make sure Python is installed on the computer.

The command arguments are as follows:

  > -h, --help       Show help message and exit

  > -s, --source:    Path of source folder

  > -r, --replica:   Path of replica folder

  > -i, --interval:  Interval between synchronization (seconds)

  > -l, --log:       Path of log folder

 The minimum interval to set between the synchronization is 5 seconds. 

 # Use cases

 The script supports the different scenarios:

 1. A file is modified in the source folder => The file will be updated in the replica folder.
 
 1. A file is modified in the replica folder => The file will be updated to match the source file.

 1. A file or directory is removed from the source folder => The file or directory will be removed from the replica folder.

 1.  A file or directory is removed from the replica folder => The file or directory will be created in the replica folder (copy) to match the source folder

 1. A file or directory is added in the source folder => The file or directory will be created in the replica folder (copy) to match the source folder

 1. A file or directory is added in the replica folder => The file or directory will be removed if it’s not matching the source folder

 # Operations
## Update
The update operation is done only on files. 

A source and replica folder is provided to the function "getMismatchFiles" and will return a list of files that's not matching. 

The function uses the library "filecmp" to compare the two folders and get the common files (matching names). Then, it will compare each files from this list and return the list of mismatch files. 

The list returned is then used in the function "updateFile", which will loop on each file, to remove it in the replica and copy it from the source folder.

### Name update
If a file or directory is renamed, it is considered as another instance. Instead of updating the name, the file or directory will be removed (delete operation) from replica folders and then copied (create operation) from the source folder into the replica folder. So no update operation is used in case of renaming a file or directory.

## Delete
The delete operation uses the function "getToDelete" to receive a list of file or directory to remove. This operation is done only on the replica folder.

This list is generating by comparing the two folders, the "right_only" attribute allow to get the file or directory only available in the replica folder. In other words, there is no match for them in the source folder and should not be there. 

The operation is meant for the files and directories, a different command is needed for the removing as more privilege is needed for the directories. It is the reason of the test with "if" "isFile" or "isDir".

## Create
Create operation is meant for files and directories. When a file or directory is present in the source folder, but not in the replica. 

The list is provided by the function "getToCreate", which will compare two folders with the attribute "left_only". It represents the files or directories only available in the source folder.

The function "create" will loop on the list to copy each file or directory in the replica folder.

When a folder is copied, all of its content will be copied in the replica folder. 

# Recursive function "synchroniseFolder"
The function synchronization is initially executed to compare the source and replica folder. Then it will arrange the content to be the same. However, we also need to check the subdirectories to ensure that all the files inside are matching. 

At the end of the function "synchroniseFolder", it will get a list of all subdirectories from the source folder. If none is present, the script stops.

On the other hand, if there are subdirectories, the function will be called again in order to compare the content of the subdirectories. Then after arranging the subdirectories, the same will happen, if there are again subdirectories the function will call itself again with the new folders to check. It will stop after there is not more subdirectories to check.

# Logging
The logger is generated in "logger.py" and is passed into the function "synchroniseFolder" in order to be used during the operations. 

The logger is able to log into a file, which its path has to be mentioned in the arguments and also in the command output. 

In order to do so, two handlers have to be configured to redirect the log into the file and the command output:
-  >FileHandler(path +"\log.txt")

- >StreamHandler(sys.stdout)

The path of the log folder has to be valid otherwise the script will print a message. 

# Command line arguments
The command line arguments are handled with the library "argparse". All paths are required and will be tested with "os.path.isDir" to check if it is existing or valid path. If that's not the case, the script will print a message and stop.

The interval argument is not required, but has a default value of 5. The value is in seconds and is tested to be higher than 5, otherwise the script will print a message and stop. 

The default value of 5 has been decided on my own. It could be changed if needed. 

# Synchronization execution
In the current state of the project, the script will execute 10 synchronizations with the interval specified in the arguments. After that the program will stop.

This aim to not have the script executing forever in the terminal. 

If it is wanted to have the script to continue, the loop while can be modified like this:

> while True:

And it can be manually stopped with CTRL+C, but will end up with an error in the terminal.
