import hashlib
import os
import sys
import timeit
from collections import defaultdict


def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    file_hash_map = defaultdict(list)
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = get_file_hash(file_path)
            file_hash_map[file_hash].append(file_path)

    duplicate_files = []
    for file_hash, file_paths in file_hash_map.items():
        if len(file_paths) > 1:
            duplicate_files.extend(file_paths)

    return duplicate_files

def printTime(msg, start):
    end = timeit.default_timer()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{} ran for {:0>2}:{:0>2}:{:05.2f}".format(msg, int(hours), int(minutes), seconds))


start = timeit.default_timer()
old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file
# Specify the directory to search for duplicate files
#directory_to_search = "D:"
directory_to_search = '/media/julio/TOSHIBA EXT'
# Find duplicate files
duplicates = find_duplicate_files(directory_to_search)

if duplicates:
    print("Duplicate files found:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicate files found.")

printTime('--> Finding Duplicates ' + directory_to_search, start)
sys.stdout = old_stdout

log_file.close()