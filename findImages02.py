vailed_ext = ["JPG", ".jpg", "jpeg", ".png"]
import os
from PIL import Image
f_list = []
def Test2(rootDir):     
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        filename, file_extension = os.path.splitext(path) 
        if file_extension in vailed_ext:
#            print(path)
            f_list.append(path)
        if os.path.isdir(path): 
           Test2(path)

#Test2("/media/julio/writable")
sorted_ext = sorted(ext.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_ext)



