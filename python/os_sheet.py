# Python 'os' Module Cheat Sheet

# Importing the module
import os

# Directory and File Manipulation
os.getcwd()                      # Get current working directory
os.chdir(path)                   # Change current working directory to 'path'
os.listdir(path='.')             # List files and directories in 'path'
os.mkdir(path, mode=0o777)       # Create a directory named 'path'
os.makedirs(path, mode=0o777)    # Recursive directory creation
os.rmdir(path)                   # Remove (delete) the directory path
os.removedirs(path)              # Remove directories recursively
os.rename(src, dst)              # Rename the file or directory from src to dst

# Path Manipulation
os.path.abspath(path)            # Return absolute path
os.path.basename(path)           # Return base name of pathname path
os.path.dirname(path)            # Return the directory name of pathname path
os.path.exists(path)             # Check if path exists
os.path.isdir(path)              # Check if path is a directory
os.path.isfile(path)             # Check if path is a file
os.path.join(path1[, path2, ...])# Join one or more path components

# System Information
os.name                          # Name of the operating system
os.environ                       # Environment variables
os.getenv(key, default=None)     # Get an environment variable, return None if not found

# File Properties
os.stat(path)                    # Get status of a file or directory
os.path.getsize(path)            # Return the size, in bytes, of path

# Process Management
os.system(command)               # Execute the command (a string) in a subshell
os.startfile(path[, operation])  # Start a file with its associated application

# Miscellaneous
os.urandom(n)                    # Return n random bytes
os.getpid()                      # Get current process ID

