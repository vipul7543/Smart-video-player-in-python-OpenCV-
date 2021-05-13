import cv2
import vlc,time

cam=cv2.VideoCapture(0)

#Enter the address of the file you want to play below

fd=cv2.CascadeClassifier(r'C:\Users\DELL\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
v=vlc.MediaPlayer(r'C:\Users\DELL\Documents\AR\Ed.MKV')
v.play()
x=0

while True:
        r,i=cam.read()
        gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        face=fd.detectMultiScale(gray,1.3,7)
        print('number of detected faces are',len(face))
        for(x,y,w,h) in face:
                cv2.rectangle(i,(x,y),(x+w+10,y+h+10),(255,0,0),1)
        cv2.imshow('image',i)
        if(len(face)>0):
                v.play()
                x=1;
        elif(x==1):
                v.pause()
                x=0

                #v.audio_set_volume(100)
        #v.audio_set_volume(60)

        k=cv2.waitKey(5)
        if(k==ord('q')):

                break
v.stop()

cv2.destroyAllWindows()
