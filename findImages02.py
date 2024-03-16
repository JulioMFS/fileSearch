import os
import time
vailed_ext = ["JPG", ".jpg", "jpeg", ".png"]
f_list = []
ext = {}
def Test2(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        filename, file_extension = os.path.splitext(path)
        if (file_extension in ext):
            ext[file_extension] += 1
        else:
            ext[file_extension] = 1

        if file_extension in vailed_ext:
#            print(path)
            f_list.append(path)
        if os.path.isdir(path):
           Test2(path)
st_time = time.time()
#Test2("/media/julio/TOSHIBA EXT")

Test2("E:/")
sorted_ext = sorted(ext.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_ext)

#print(converted_dict)

#for l in converted_dict:
#    print (l)
print('\n<----------------------------------------------------------->')
for k, v in converted_dict.items():
    print(k, '\t\t', v)
end_time = time.time()
tot_time = int(end_time - st_time)
min = int(tot_time /60)
secs = int((tot_time - min) / 60)
print('\n<----------------------------------------------------------->')
print('This progrtam took total {0}, {1}:{2} (mins:secs)'.format(tot_time, min, secs))
print('<----------------------------------------------------------->')
