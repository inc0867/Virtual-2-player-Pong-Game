
import cv2 
import mediapipe
import numpy
import HandTrackingModule as htm
import time


hız = 45 #30 is the best speed
cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,1920)
detec = htm.FindHands()
detec2 = htm.FindHands()
x,y = (600,300)
ix = 18
iy = 18
pot1 = (1220,500)
pot2 = (1270,200)
potx , Poty = pot1 
potx2 , poty2 = pot2
iyart = 18
potuın = 18
newy = 500
newys = 200
artma = 18
artci = 500
artci2 = 200
Pscore = 0
Cscore = 0

while True:
    isTrue , kare = cam.read()

 
    alan = kare[0:1000 , 610:1280]

    alan2 = kare[0:1000 , 0:610] #sag

    zaaa = detec.getPosition(alan , (6,8))

    print("ilk ayrı"+str(zaaa))

    azzz = detec2.getPosition(alan2 , (10,12))

    

    print("ikinci yarı"+str(azzz))
    
    
    
    HposLL = detec.getPosition(kare , (6,8),draw=False)

    cv2.putText(kare,'Player:'+str(Pscore)+'|||||'+'Player2:'+str(Cscore),(450,30),cv2.FONT_HERSHEY_COMPLEX , 1.0 , (255,0,0) , 1)
    cv2.line(kare , (610,0) , (610,1000) , (255,0,0) , 3 )
    try:
        aax , aay = azzz[1]
        print("girdiö")
        if aay > 345:
            if artci > 720:
                artma = -hız
            else:
                artma = hız
        if aay < 345:
            if 0 > artci2:
                artma = hız
            else:
                artma = -hız
        
    except:pass
    

    cv2.circle(kare , (x,y) , 30 , (255,255,255) , cv2.FILLED)
    if x > 1280:
        x , y = (600,300)
        Pscore += 1
        
    if 0 >= x:
        x , y = (600,300)
        Cscore += 1
    

    if y > 720:
        iy = -hız
    if 0 > y:
        iy = hız 
    if artci>=y>=artci2 and 70>=x>=20:
        ix = hız
        #print("bana çarptı")
    if newy>=y>=newys and 1270>=x>=1220:
        #print("sana çarptı")
        ix = -hız
        
    if Pscore or Cscore == 10:
        if Pscore == 10:
            print("Player kazandı")
            break
        if Cscore == 10:
            print("Player2 kazandı")
            break

    
    cv2.rectangle(kare , (20,artci) , (70,artci2) , (255,255,255) , cv2.FILLED)
    cv2.rectangle(kare , (1220,newy) , (1270,newys) , (255,255,255) , cv2.FILLED)

    newy = newy + iyart
    newys = newys + iyart

    artci = artci + artma
    artci2 = artci2 + artma
    try:
        kx , ky = zaaa[1]
        if ky > 345:
            if newy > 720:
                iyart = -hız
            else:
                iyart = hız
        if 345 > ky:
            if 0 > newys:
                iyart = hız
            else:
                iyart = -hız
    except:pass

    
    if artci > 720:
        artma = -hız
    if 0 > artci2:
        artma = hız
    if newy > 720:
        iyart = -hız
    if 0 > newys:
        iyart = hız

    


    y = y + iy
    x = x + ix
    

    


    #try:
        #print("1.",Hposi[1])
        #print("2.",Hposl[1])
    #except:
        #pass
    cv2.imshow('nncjncjnc',alan2)

    cv2.imshow('ddhdhdhhd',alan)
    cv2.imshow('MAIN',kare)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break


cam.release()
cv2.destroyAllWindows()

