import datetime
import os
import pathlib
import time
from PIL import Image

st_time = time.time()
end_time = time.time()
sep = os.path.sep
ext = {}
ext2 = {}
prev_path = ''
excld_names = ['FB_IMG', 'Screenshot', '$RECYCLE.BIN',
               'Eclipse', 'eclipse', 'java', 'JAVA', 'Java'
               'metadata', 'MyJava', '.lock', 'mysql', 'MySql'
               'JavaScript', 'sublime', 'Sublime', 'css', 'classpath',
               'src', 'IMG00333-20101122-1746.jpg', 'Copy']

excld_ext = ['jpeg', 'png', 'PNG', 'xpm', 'XPM', 'xml', 'py',
             'html', 'Identifier', 'js', 'txt', 'xlsx', 'class', 'Java']
def exclude(file):
    if any(x in file for x in excld_names):
        return True
    if any(x in file for x in excld_ext):
        return True
def is_image_file(file_path):
    try:
        # Attempt to open the file as an image
        Image.open(file_path)
        return True
    except (IOError, SyntaxError):
 #       print("Couldn'nt open this file: {0}, error: {1}".format(file_path, IOError))
 #       print(SyntaxError)
        # IOError: Unable to open file as image
        # SyntaxError: Not a valid image file
        return False

def scan_for_photos(directory):
    photo_files = []
    for root, dirs, files in os.walk(directory):
        r = ''
        prev_path = ''
        for file in files:
#            if r != root:
#                print(root)
#            r = root
            file_path = os.path.join(root, file)
            if not exclude(file_path):
                isFile = os.path.isfile(file_path)
                sz = 0
                if isFile:
                    sz = os.path.getsize(file_path)
                ex = pathlib.Path(file_path).suffix
                if not exclude(file) and sz < 178956970:
                    if is_image_file(file_path):
                        photo_files.append(file_path)
                        st = os.stat(file_path)
                        ts = os.path.getctime(file_path)  # this returns the creation timestamp.
                        #ts = st.st_ctime
                        cdt = datetime.datetime.fromtimestamp(ts)  # this converts the timestamp to datetime object.
                        #sz = os.path.getsize(file_path)
                        ts = os.path.getmtime(file_path)
                        mdt = datetime.datetime.fromtimestamp(ts)


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
        if prev_path != root:
            text = root.split(os.path.sep)
            str = ''
            for i in range(1, len(text) -1):
                str += '\t'
            str += text[-1]
            print(str)
            prev_path = root
    return photo_files

# Example usage:
#directory_to_scan = "C:\\Users\\julio\\OneDrive\\Pictures"
st_time = time.time()
directory_to_scan = "/media/julio/TOSHIBA EXT"
photos = scan_for_photos(directory_to_scan)
end_time = time.time()
dur_time = end_time - st_time
print("Found {0} photos in {1} seconds".format(len(photos)), dur_time)
#for photo in photos:
#    print(photo)

print('<------- Photo extensions ---------->')
for k, v in ext.items():
    print(k, v)

print('<------- Other extensions ---------->')
for k, v in ext2.items():
    print(k, v)
