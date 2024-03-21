import os
import sys
from collections import defaultdict

def find_duplicate_files(root_folder, extensions):
    file_dict = defaultdict(list)
    for root, dirs, files in os.walk(root_folder):
        print(root, len(files), ' files')
        for file in files:
            if file.lower().endswith(extensions):
                file_dict[file].append(os.path.join(root, file))
                print('\t', file)

    duplicate_files = {k: v for k, v in file_dict.items() if len(v) > 1}
    return duplicate_files

def cleanup_duplicate_files(root_folder, extensions):
    duplicate_files = find_duplicate_files(root_folder, extensions)
    for file_name, paths in duplicate_files.items():
        print(f"Duplicate files found for: {file_name}")
        for path in paths:
            print(f" - {path}")
"""        print("Select which file to keep and which to remove (or enter 's' to skip):")
        choice = input()
        if choice.isdigit() and int(choice) < len(paths):
            index = int(choice)
            for i, path in enumerate(paths):
                if i != index:
                    print(f"Removing: {path}")
                    os.remove(path)
        elif choice.lower() == 's':
            print("Skipping...")
        else:
            print("Invalid choice. Skipping...")
"""
if __name__ == "__main__":
    old_stdout = sys.stdout
    progWithExtension = sys.argv[0]
    tempTuple = os.path.splitext(progWithExtension)
    prog = tempTuple[0]
    logfile = prog + '.log'
    log_file = open(logfile, "w")

    sys.stdout = log_file
    # Specify the directory to search for duplicate files
    sep = os.sep

    #root_folder = input("Enter the root folder path: ")
    root_folder = 'D:\\AgromaisTest'
    extensions = (".pdf", ".xlsx", ".jpg", ".csv", ".docx", ".png")  # Add more extensions as needed
    cleanup_duplicate_files(root_folder, extensions)

    sys.stdout = old_stdout
    log_file.close()