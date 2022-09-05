import os
path = 'C:/Users/MS/Downloads/pinterest-downloader-master/pinterest-downloader-master/images/vvmahesh/Couple Photography Poses'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))