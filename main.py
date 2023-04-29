import cv2
import os
from cvzone.HandTrackingModule import HandDetector
def call(st):
        width=1280
        height=720
        path=st
        cap = cv2.VideoCapture(0)
        cap.set(3,width)
        cap.set(4,height)
        imgslist=sorted(os.listdir(path),key=len)
        sn=0
        hs,ws=120,213
        lineth=300
        button=False
        bcnt=0
        bdelay=20
        detector=HandDetector(detectionCon=0.8, maxHands=1)
        annt=[[]]
        aflag=-1
        astart=False
        color=[(0,255,0),(255,0,0),(0,0,255)]
        c=0
        while True:
            success,img=cap.read()
            img=cv2.flip(img,1)
            imgpath=os.path.join(path,imgslist[sn])
            imgcur= cv2.imread(imgpath)
            imgcur=cv2.resize(imgcur,(1000,600))
            hands,img=detector.findHands(img)
            #cv2.line(img,(0,lineth),(width,lineth),(0,0,255),10)
            if hands and button is False:
                hand=hands[0]
                fingers=detector.fingersUp(hand)
                cx,cy=hand['center']
                lmlist=hand['lmList']
                inf=lmlist[8][0],lmlist[8][1]
                #Left 1
                if fingers==[1, 0, 0, 0, 0]:
                        print("left")
                        if sn>0:
                            button=True
                            sn=sn-1
                            annt=[[]]
                            aflag=-1
                            astart=False
                    #right move
                if fingers==[0,0,0,0,1]:
                        print("right")
                        if sn<len(imgslist)-1:
                            button=True
                            sn=sn+1
                            annt=[[]]
                            aflag=-1
                            astart=False
                    #close
                if fingers == [1,1,0,0,1]:
                    c+=1
                    c=c%3    
                #undo
                if fingers == [0,1,1,1,1]:
                    if(len(annt)!=0):
                        annt.pop()
                        aflag-=1
                #pointer
                if fingers == [0,1,1,0,0]:
                        cv2.circle(imgcur,inf,10,color[c],cv2.FILLED)
                #drwing
                if fingers == [0,1,0,0,0]:
                        if astart==False:
                            astart=True
                            aflag+=1
                            annt.append([])
                        cv2.circle(imgcur,inf,10,color[c],cv2.FILLED)
                        if(aflag>=0):
                            annt[aflag].append(inf)
                else:
                    astart=False
            if button:
                bcnt+=1
                if bcnt> bdelay:
                    bcnt=0
                    button=False
            for i in range(len(annt)):
                for j in range(len(annt[i])):
                    if j!=0:
                        cv2.line(imgcur,annt[i][j-1],annt[i][j],color[c],10)
            if hands and button is False:             
                if fingers == [1,1,1,1,1]:
                        #print(imgpath)
                        #cv2.imshow("1",imgcur)
                        cv2.imwrite(imgpath,imgcur)
            tutor=cv2.resize(img,(ws,hs))
            h,w,_=imgcur.shape
            imgcur[0:hs,0:ws] = tutor
            #cv2.imshow("Tutor",img)
            cv2.imshow("Slide",imgcur)
            key=cv2.waitKey(1)
            if key== ord('q'):
                break