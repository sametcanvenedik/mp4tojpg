import os
from typing import Any, Optional
import cv2
import matplotlib.pyplot as plt

def filepath(file, *args):
    prt1 = os.getcwd()
    if args:
        fex = args[0]
    else:
        fex = ".jpg"
    fileway = ("{}\\data\\{}{}" .format(prt1,file,fex))
    return fileway

def cshow(name,pic):
    cv2.imshow(name,cv2.cvtColor(pic,cv2.COLOR_BGR2RGB))

def cshows(name,pic):
    cv2.imshow(name,pic)

def pshow(name,pic):
    plt.figure(), plt.title(name), plt.axis("off"),plt.imshow(pic)
    plt.waitforbuttonpress(0.0000001)

def pshowg(name,pic):
    plt.figure()
    plt.imshow(pic,cmap= "gray")
    plt.title(name)
    plt.axis("off")
    plt.waitforbuttonpress(0.0000001)
    
def pwait():
    while True:
        if plt.waitforbuttonpress(timeout = -1) == True:
            break
        else:
            continue

def cwait(*args):
    key = 0
    if args:
        key = args[0]
    k= cv2.waitKey(key)
    if k == 0xFF & ord("q"):
        cv2.destroyAllWindows()