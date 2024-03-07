import os
from collections import defaultdict

def find_duplicate_folders(root_folder):
    folder_dict = defaultdict(list)
    for root, dirs, files in os.walk(root_folder):
        for d in dirs:
            folder_dict[d].append(os.path.join(root, d))

    duplicate_folders = {k: v for k, v in folder_dict.items() if len(v) > 1}
    return duplicate_folders

def identify_duplicate_folders(root_folder):
    duplicate_folders = find_duplicate_folders(root_folder)
    if not duplicate_folders:
        print("No duplicate folders found.")
    else:
        print("Duplicate folders found:")
        for folder_name, paths in duplicate_folders.items():
            print(f"Folder Name: {folder_name}")
            print("Locations:")
            for path in paths:
                print(f" - {path}")

if __name__ == "__main__":
    root_folder = input("Enter the root folder path: ")
    identify_duplicate_folders(root_folder)
