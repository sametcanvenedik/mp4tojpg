import cv2
import osworks as ow
import mymodul as md

source_list = ow.sourcepaths()


# Önizleme göster
view = False
# boyutu küçült, halihazır 50/100 lakin fonk. 20/100 ile çağrıldı, video çok büyük.
resize = True
# her x karede 1 alınacak kare
circ = 5 # x = circ


for video in source_list:
    
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
                        print(video)
                        print(source_list[len(source_list)-1])
                        if video == source_list[len(source_list)-1]:
                            cv2.putText(Limg,"Finish. press 'q' for exit.",(10,30),cv2.FONT_ITALIC,1,(255,0,0),2)
                            if view:
                                cv2.destroyWindow(winname)
                            md.cshow("Done!", cv2.cvtColor(Limg, cv2.COLOR_BGR2RGB))
                            print("Finis")
                            print("çıkmak  için 'q' ye basın.")
                            md.cwait()
                        else:
                            print("Next...")
                        break
                    if resize:
                        img = cv2.resize(img,md.reshape(img,20)) # özel değer,  video çook büyük olduğu için 20, standart 50
                    if view:
                        md.cshow(winname, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                        md.cwait(1)
                    if numofimg % circ == 0:
                        cv2.imwrite("{}\\img{}.jpg".format(folder,numofimg),img)
                    print("image {}".format(numofimg))
                    numofimg+=1
                    Limg=img
                
            else:
                print("videodan resim okunamadı")
        else:
            print("Dosya oluşturulamadı!")

    else:
        print("Video bulunamadı!")