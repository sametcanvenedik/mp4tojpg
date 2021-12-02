import os
import mymodul as md

fpath = md.filepath("npsource","")
fname = "images"

global file_num

def createfolder():
    file_num = 0
    while os.path.exists(fpath+"\\" + fname +str(file_num)): # generator kullanıla bilirmi bi bakalım
        file_num += 1
        folder = fpath+"\\" + fname +str(file_num)
    os.makedirs(folder)
    return folder



