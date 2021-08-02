# import OpenCV
import cv2    
#load the classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Select video source = computer cam
detect = cv2.VideoCapture(0)
 
while True:
     _, frame = detect.read()

     frame = cv2.cvtColor(frame,0)

     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     detection = face_cascade.detectMultiScale(gray, 1.1, 4) #convert into gray-scale because it is easy to process.

     if(len(detection) >0):
     	(x,y,z,h) = detection[0]
     	frame = cv2.rectangle(frame,(x,y),(x+z,y+h),(128, 0, 128), 2)

     # Dispaly the frame
     cv2.imshow('frame', frame)
     q = cv2.waitKey(1) & 0xFF #add delay for 1ms
     if q==27:
       break


detect.release()
cv2.destroyAllWindows() 