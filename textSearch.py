import os
from time import sleep


# The colours of the things
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
file_type = input("File Type : ")
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"

# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
    print("path doesn't exist:  ", search_path)
    search_path = "."

# Repeat for each file in the directory
for fname in os.listdir(path=search_path):

    # Apply file type filter
    if fname.endswith(file_type):

        # Open file for reading
        fo = open(search_path + fname, 'r')

        # Read the first line from the file
        line = fo.read()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        if line != '':
            # Search for string in line
            index = line.find(search_str)
            if (index != -1):
                print(bcolors.OKGREEN + '[+]' + bcolors.ENDC + ' ', fname, sep="")
                print('      ')
                sleep(0.01)
            else:
                print(bcolors.FAIL + '[-]' + bcolors.ENDC + ' ', fname, ' ', 'does not contain', ' ', search_str,
                      sep="")
                print("       ")
                sleep(0.01)
            line = fo.readline()

            # Increment line counter
            line_no += 1
        # Close the files
        fo.close()