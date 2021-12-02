import cv2
import osworks as ow
import mymodul as md

video = md.filepath("video",".mp4")

cap = cv2.VideoCapture(video)

if cap.isOpened():

    suc, folder = ow.createfolder()
    if suc:
        success, img = cap.read()
        if success:
            numofimg =0
            winname= "Current image"
            while True:
                
                end, img= cap.read()
                if end == False:
                    cv2.putText(Limg,"Finish. press 'q' for exit.",(10,30),cv2.FONT_ITALIC,1,(255,0,0),2)
                    cv2.destroyWindow(winname)
                    md.cshow("Done!", cv2.cvtColor(Limg, cv2.COLOR_BGR2RGB))

                    break
                md.cshow(winname, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                md.cwait(1)
                cv2.imwrite("{}\\img{}.jpg".format(folder,numofimg),img)
                print("image {}".format(numofimg))
                numofimg+=1
                Limg=img
            print("Finis")
            print("çıkmak  için 'q' ye basın.")
            md.cwait()
        else:
            print("videodan resim okunamadı")
    else:
        print("Dosya oluşturulamadı!")

else:
    print("Video bulunamadı!")