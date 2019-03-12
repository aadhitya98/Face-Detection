import cv2

facedetect=cv2.CascadeClassifier(r'F:\haarcascade_frontalface_default.xml')
eyesdetect=cv2.CascadeClassifier(r'F:\haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
#image=cv2.imread(r'F:\rohit.PNG')
while True:
    ret,image=cap.read()
  #cap=cv2.imread()
    #image=cv2.imread(r'F:\rohit.PNG')
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        facesgrey=gray[y:y+h,x:x+w]
        facecolor=image[y:y+h,x:x+w]
        
        eye=eyesdetect.detectMultiScale(facesgrey)
        for(ex,ey,ew,eh) in eye:
        
         cv2.rectangle(facecolor,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    cv2.imshow('Image',image)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.waitKey(0)

    
#if k==113:
    #break
    
cap.release()
cv2.destroyAllWindows()
       
        
        
    
    