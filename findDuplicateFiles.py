import hashlib
import os
import sys
import timeit
from collections import defaultdict
from datetime import datetime
from colorist import Color

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

def find_duplicate_files(directory, log_file):
    file_hash_map = defaultdict(list)
    extensions = {}
    totsz = 0
    totSzToDelete = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            f, ext = os.path.splitext(file_path)
            sz = os.path.getsize(file_path)
            val = [0, 0]
            if ext in extensions:
                val = extensions[ext]
                val[0] += 1
                val[1] += sz
                extensions[ext] = val
            else:
                val[0] = 1
                val[1] = sz
                extensions[ext] = val
            totsz += sz
            if 'eclipse' in file_path or 'Program Files' in file_path:
                continue
            file_hash = get_file_hash(file_path)
            file_hash_map[file_hash].append(filename + ' ' + file_path)

    duplicate_files = []
    print('No of files in file_hash: ', len(file_hash))
    for file_hash, file_paths in file_hash_map.items():
        if len(file_paths) > 1:
            duplicate_files.extend(file_paths)
            i = 0
            for file_path in file_paths:
                f = file_path.split()
                sz = os.path.getsize(f[1])
                txt = '{:<30}{:<60}{}'.format(f[0], f[1], sz)
 #               print("\033[031m" + "Hello" + "\033[0m")
                if i > 0:
                    print(txt, file = log_file)
                    print(f'{Color.RED} {txt} {Color.OFF}')
                    totSzToDelete += sz
                else:
                    print(txt)
                i += 1
            print()
    return duplicate_files, extensions, totSzToDelete

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

#sys.stdout = log_file
# Specify the directory to search for duplicate files
sep = os.sep
directory_to_search = "D:"
#directory_to_search = "D:\AgromaisTest"
#directory_to_search = '/media/julio/TOSHIBA EXT'
# Find duplicate files
duplicates, extensions, totsz = find_duplicate_files(directory_to_search, log_file)
if duplicates:
    print("\nDuplicate files found by prog: {0}, in {1}\n".format(progWithExtension, directory_to_search))
    print('Total bytes to delete: {}\n'.format(totsz))
    str = ''
    #for duplicate in duplicates:
    #    str1 = duplicate.split(' --> ')
    #    if str1[0] != str and str != '':
    #        print('\n')
    #    str = str1[0]
    #    print(duplicate)
else:
    print("No duplicate files found.")
if extensions:
    totsz = 0
    for k, v in extensions.items():
        val = v
        print('{:<7}{:>10}{:>10}'.format(k, val[0], val[1]))
        totsz += val[1]
    print('{}{}'.format(' ' * 16, '-' * 11))
    print('total ext bytes: {:>10}'.format(totsz))
end_time = datetime.now()
# Format the current time as a string
end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")
printTime('\n--> Finding Duplicates ' + directory_to_search, start, start_time_str, end_time_str)
sys.stdout = old_stdout

log_file.close()
