import os
import filecmp
import shutil


def remove_duplicate_folders(root_dir):
    # Dictionary to store directories and their contents
    dir_dict = {}

    # Traverse the directory structure
    for root, dirs, files in os.walk(root_dir):
        # Ignore hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Create a hashable representation of directory contents
        dir_contents = tuple(sorted(files))

        # If directory contents already exist, remove duplicate folder
        if dir_contents in dir_dict:
            print(f"Removing duplicate folder: {root}")
            shutil.rmtree(root)
        else:
            dir_dict[dir_contents] = root


if __name__ == "__main__":
    root_directory = input("Enter the root directory path: ")
    remove_duplicate_folders(root_directory)
