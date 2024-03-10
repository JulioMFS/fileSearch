import hashlib
import os
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

# Specify the directory to search for duplicate files
directory_to_search = "D:"

# Find duplicate files
duplicates = find_duplicate_files(directory_to_search)

if duplicates:
    print("Duplicate files found:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicate files found.")
