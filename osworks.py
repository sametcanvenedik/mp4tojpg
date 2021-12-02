import os
import mymodul as md

def pathgenetator():
    fpath = md.filepath("npsource","")
    fname = "images"
    file_num = 0
    while True:
        folder = fpath+"\\" + fname +str(file_num)
        file_num += 1
        yield folder


def createfolder():
    path = pathgenetator()
    folder = next(path)
    while os.path.exists(folder):
        folder = next(path)
    os.makedirs(folder)
    
    return os.path.exists(folder), folder


