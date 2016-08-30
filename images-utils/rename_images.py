"""
python-version  : 3.4
Author          : Nicola Corda
Description     : Script to extract metadata from pictures
Dependencies    : ExifRead
To run the script pass as input the folder path: python renamePictures.py folderName
"""

import os
import sys
import glob
import exifread
import utils

if len(sys.argv)<=1:
    print('ERROR, INSERT folder path as input ')
else:
    print('Processing files....')
    path = sys.argv[1]
    os.chdir(path)
    cmd = 'pwd'
    os.system(cmd)
    metadata = 0
    for file in glob.glob("*.jpg"):
        print('extraction info from '+file)
        f = open(file, 'rb')
        # Return Exif tags
        tags = exifread.process_file(f)
        for tag in tags:
            if(tag in ('EXIF DateTimeOriginal')):
                timestamp = str(tags[tag])
                formattedTimestamp = utils.delete_date_symbols(timestamp,'YYYY-MM-DD HH:MM:SS')
                newNamePicture=formattedTimestamp+'.jpg'
                rename_cmd = 'mv '+file.replace(" ", "\ ") + ' ' + newNamePicture
                print(rename_cmd)
                os.system(rename_cmd)