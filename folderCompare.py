import filecmp


def compare_folders(dir1, dir2):
    comparison = filecmp.dircmp(dir1, dir2)

    # Files only in dir1
    for name in comparison.left_only:
        print(f'File only in {dir1}: {name}')

    # Files only in dir2
    for name in comparison.right_only:
        print(f'File only in {dir2}: {name}')

    # Files that are in both folders but differ
    for name in comparison.diff_files:
        print(f'Files differ: {name}')

    # Recursively compare subfolders
    for sub_dir in comparison.common_dirs:
        compare_folders(
            f'{dir1}/{sub_dir}',
            f'{dir2}/{sub_dir}'
        )


# Usage
compare_folders('f:', 'E:/MyOther32GMemoryStick')
print('-----> Done')
