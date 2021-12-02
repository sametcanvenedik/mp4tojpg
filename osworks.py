import os
import mymodul as md

def sourcepathgenerator():
    spath= md.filepath("","")
    sname= "video"
    source_num =0
    while True:
        source = spath + sname + "{}".format(source_num) + ".mp4"
        source_num += 1
        yield source


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

def sourcepaths():
    paths =[]
    path = sourcepathgenerator()
    source = next(path)
    while os.path.exists(source):
        paths.append(source)
        source = next(path)
    return paths

def test():
    print(sourcepaths())

