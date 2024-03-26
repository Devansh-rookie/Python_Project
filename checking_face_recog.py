import cv2
import numpy as np
import face_recognition

imgelon =face_recognition.load_image_file("F:\CodingFolder(dont_move)\Python_Project\elon.jpg")
imgelon_rgb = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
#----------Finding face Location for drawing bounding boxes-------
face = face_recognition.face_locations(imgelon_rgb)[0]
copy = imgelon.copy()
#-------------------Drawing the Rectangle-------------------------
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)

copy_rgb = cv2.cvtColor(copy,cv2.COLOR_BGR2RGB)

cv2.imshow('copy', copy_rgb)
cv2.imshow('elon',imgelon_rgb)
cv2.waitKey(0)