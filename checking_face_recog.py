# import cv2
import numpy as np
# import face_recognition

# imgelon =face_recognition.load_image_file("load_images/elon.jpg")
# imgelon_rgb = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
# #----------Finding face Location for drawing bounding boxes-------
# face = face_recognition.face_locations(imgelon_rgb)[0]
# copy = imgelon.copy()
# #-------------------Drawing the Rectangle-------------------------
# cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)

# copy_rgb = cv2.cvtColor(copy,cv2.COLOR_BGR2RGB)

# cv2.imshow('copy', copy_rgb)
# cv2.imshow('elon',imgelon_rgb)
# cv2.waitKey(0)

import cv2
import face_recognition

img_elon = face_recognition.load_image_file("load_images/elon.jpg")
img_devansh = face_recognition.load_image_file("load_images/devansh.jpg")

img_devansh = cv2.cvtColor(img_devansh, cv2.COLOR_BGR2RGB)
img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)

# img_devansh_50 = cv2.resize(img_devansh, None, fx = 0.50, fy = 0.50)

height = img_devansh.shape[0] # this is somewhat like a list which has its dimensions where 0 is height and 1 is width
width = img_devansh.shape[1]

new_width = 500
new_height = int(height* new_width/width)

img_devansh_50= cv2.resize(img_devansh, (new_width, new_height))

face_devansh = face_recognition.face_locations(img_devansh_50)[0] # check later in the documentations what is happening in this line of code what kind of data type its returing and how and so on
# copy_devansh = img_devansh.copy()

# cv2.rectangle(img_devansh_50,(face_devansh[3], face_devansh[0]),(face_devansh[1], face_devansh[2]),(255,0,0), 2)

# cv2.imshow("Devansh",img_devansh_50)
# cv2.waitKey(0)
train_devansh_encodings = list()
train_devansh_encodings.append(face_recognition.face_encodings(img_devansh_50)[0])

cap  = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_resized = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img, None, fx=0.25, fy = 0.25)
    faces_in_frame = face_recognition.face_locations(img_resized)#assume that there is only one for this moment
    for encode_face, faceloc in zip(train_devansh_encodings,faces_in_frame):
            matches = face_recognition.compare_faces(train_devansh_encodings, encode_face)
            faceDist = face_recognition.face_distance(train_devansh_encodings, encode_face)
            matchIndex = np.argmin(faceDist)
            print(matchIndex)
            if matches[matchIndex]:
                name = "Devansh"
                y1,x2,y2,x1 = faceloc
                # since we scaled down by 4 times
                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    
    cv2.imshow("WebCam", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



