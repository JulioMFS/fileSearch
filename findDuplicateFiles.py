import hashlib
import os
import sys
import timeit
from collections import defaultdict
from datetime import datetime

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to read '{file_path}'.")
    except IOError as e:
        print(f"IOError occurred while reading '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return hasher.hexdigest()

def find_duplicate_files(directory):
    file_hash_map = defaultdict(list)
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if 'eclipse' in file_path or 'Program Files' in file_path:
                continue
            file_hash = get_file_hash(file_path)
            file_hash_map[file_hash].append(file_path)

    duplicate_files = []
    for file_hash, file_paths in file_hash_map.items():
        if len(file_paths) > 1:
            duplicate_files.extend(file_paths)

    return duplicate_files

def printTime(msg, start, start_time, end_time):
    end = timeit.default_timer()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
#    print("{} ran for {:0>2}:{:0>2}:{:05.2f}".format(msg, int(hours), int(minutes), seconds))
    print("{} ran for {:0>2}:{:0>2}:{:0>2}".format(msg, int(hours), int(minutes), seconds))
    hours, rem = divmod(start, 3600)
    minutes, seconds = divmod(rem, 60)
    print('\nStarted at \t{}'.format(start_time))

    hours, rem = divmod(end, 3600)
    minutes, seconds = divmod(rem, 60)
    print('Ended at \t{}'.format(end_time))

start = timeit.default_timer()
# Get current date and time
start_time = datetime.now()
# Format the current time as a string
start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")

old_stdout = sys.stdout
progWithExtension = sys.argv[0]
tempTuple = os.path.splitext(progWithExtension)
prog = tempTuple[0]
logfile = prog + '.log'
log_file = open(logfile,"w")

sys.stdout = log_file
# Specify the directory to search for duplicate files
sep = os.sep
directory_to_search = "E:" + sep

#directory_to_search = '/media/julio/TOSHIBA EXT'
# Find duplicate files
duplicates = find_duplicate_files(directory_to_search)
if duplicates:
    print("Duplicate files found by prog: {0}, in {1}".format(progWithExtension, directory_to_search))
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicate files found.")

end_time = datetime.now()
# Format the current time as a string
end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")
printTime('--> Finding Duplicates ' + directory_to_search, start, start_time_str, end_time_str)
sys.stdout = old_stdout

log_file.close()
