import os
import datetime
import pathlib
from PIL import Image

ext = {}
ext2 = {}
def is_image_file(file_path):
    try:
        # Attempt to open the file as an image
        Image.open(file_path)
        return True
    except (IOError, SyntaxError):
        # IOError: Unable to open file as image
        # SyntaxError: Not a valid image file
        return False

def scan_for_photos(directory):
    photo_files = []

    for root, dirs, files in os.walk(directory):
        r = ''
        for file in files:
#            if r != root:
#                print(root)
#            r = root
            file_path = os.path.join(root, file)
            if is_image_file(file_path):
                ex = pathlib.Path(file_path).suffix
                if not ('FB_IMG' in file or 'Screenshot' in file or 'jpeg' in ex or 'png' in ex or 'PNG' in ex):
                    photo_files.append(file_path)
                    st = os.stat(file_path)
                    ts = os.path.getctime(file_path)  # this returns the creation timestamp.
                    #ts = st.st_ctime
                    cdt = datetime.datetime.fromtimestamp(ts)  # this converts the timestamp to datetime object.
                    #sz = os.path.getsize(file_path)
                    ts = os.path.getmtime(file_path)
                    mdt = datetime.datetime.fromtimestamp(ts)
                    sz = st.st_size

                    if (ex in ext):
                        ext[ex] += 1
                    else:
                        ext[ex] = 1

#               print('{0}, \tcreated {1} \tmodified {2} \t{3} bytes \t type {4} \t{5}'.format(file, cdt.date(), mdt.date(), sz, ex, file_path))
            else:
                ex = pathlib.Path(file_path).suffix
                if (ex in ext2):
                    ext2[ex] += 1
                else:
                    ext2[ex] = 1
               # print(file_path)
    return photo_files

# Example usage:
#directory_to_scan = "C:\\Users\\julio\\OneDrive\\Pictures"
directory_to_scan = "C:\\Users\\julio\\OneDrive\\Imagens"
photos = scan_for_photos(directory_to_scan)
print("Found {} photos:".format(len(photos)))
#for photo in photos:
#    print(photo)

print('<------- Photo extensions ---------->')
for k, v in ext.items():
    print(k, v)

print('<------- Other extensions ---------->')
for k, v in ext2.items():
    print(k, v)
