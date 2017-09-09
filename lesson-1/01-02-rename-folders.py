# -*- coding: utf-8 -*-
import os

folder = r"/Users/alabebop/TuboDropbox/Dropbox/兔Dropbox/projects/udacity/ud036/lesson-1/prank"
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(folder)
    #print(file_list)
    
    #(2) for each file, rename filename
    os.chdir(folder)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
