#face detection in video
import cv2
import vlc
i=cv2.VideoCapture(0)
f=cv2.CascadeClassifier('C:/Users/hp/Desktop/Techienest/haarcascade_frontalface_default.xml')
player = vlc.MediaPlayer("C:/Users/hp/Downloads/WhatsApp Audio 2019-07-22 at 23.19.14.mpeg")
p=0
while(1):
    b,image=i.read()
    img1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    l=f.detectMultiScale(img1,1.3,7)
    print(l)
    print(len(l))
    if(len(l)>0 and p==0):
        player.play()
        p=1
        for (x,y,w,h) in l:     #x,y coordinates of top left corner
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),10)  #x+w,y+h coordinates of bottom right corner
            cv2.imshow("Video",img1)
    elif(len(l)<1 and p==1):
        player.pause()
        p=0

            
        
    # cv2.rectangle(image,(l[0][0],l[0][1]),(l[0][0]+l[0][2],l[0][1]+l[0][3]),(0,0,255),10)
    #cv2.imshow("Video",image)
    z=cv2.waitKey(1)
    if(z==ord('q')):
        player.stop()
        break
i.release()
cv2.destroyAllWindows()
