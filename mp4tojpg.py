import cv2
import osworks as ow
import mymodul as md

video = md.filepath("video",".mp4")

cap = cv2.VideoCapture(video)

if cap.isOpened() ==  False:

    folder = ow.createfolder()

    
