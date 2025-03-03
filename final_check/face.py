import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
from datetime import date
import pymysql


todaysdate=date.today()
with open(f'final_check/Attendance_{todaysdate}.csv','w') as f:
    pass
path = 'final_check/student_images'

images = []
classNames = []
if os.path.exists(path):
    mylist = os.listdir(path)
else:
    print("Doesn't exist")
    exit(0)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    # if curImg is not None:
    images.append(curImg)
    # images.insert(0,curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        if not (img is None):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images)

def markAttendance(name):
    with open(f'final_check/Attendance_{todaysdate}.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'\n{name}, {time}, {date}')
    con = pymysql.connect(host="localhost",user= "root",password="omdevansh24", db="studentmanagementsystem1")
    cursor = con.cursor()
    cursor.execute("select * from studentattendance1")
    output = cursor.fetchall()
    if len(output)==0:
        now = datetime.now()
        time = now.strftime('%I:%M:%S:%p')
        date = now.strftime('%d-%B-%Y')
        # print(f"insert into studentattendance1(id, numOfClasses, lastClassAttended) values('{name}','1','{str(time)}-{str(date)}')")
        cursor.execute(f"insert into studentattendance1(id, numOfClasses, lastClassAttended) values('{name}','1','{str(time)}_{str(date)}')")
        con.commit()
        cursor = con.cursor()
        cursor.execute("select * from studentattendance1")
        output = cursor.fetchall()
    # print(name)
    for record in output:
        if (name) == record[0]:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            cursor.execute(f"select numOfClasses from studentattendance1 where id = '{name}'")
            num = cursor.fetchone()
            num = num[0]
            cursor.execute(f"select lastClassAttended from studentattendance1 where id = '{name}'")
            prevDate = cursor.fetchone()
            prevDate = prevDate[0]
            prevDate = (prevDate.split("_"))[1]
            if not date == prevDate:
                cursor.execute(f"update studentattendance1 set lastClassAttended = '{time}_{date}',numOfClasses= '{int(num)+1}' where id ='{name}'")
                con.commit()
                cursor.execute("select * from studentattendance1")
                output = cursor.fetchall()
                return
            else:
                cursor.execute(f"update studentattendance1 set lastClassAttended = '{time}_{date}',numOfClasses= '{int(num)}' where id ='{name}'")
                con.commit()
                cursor.execute("select * from studentattendance1")
                output = cursor.fetchall()
                return
    else:
        # print(record[0])
        now = datetime.now()
        time = now.strftime('%I:%M:%S:%p')
        date = now.strftime('%d-%B-%Y')
        
        cursor.execute(f"insert into studentattendance1 values('{name}','{1}','{time}_{date}')")
        con.commit()
        cursor.execute("select * from studentattendance1")
        output = cursor.fetchall()
    con.close()
        

cap  = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        print(matchIndex)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper().lower()
            name = classNames[matchIndex+1].upper().lower()
            y1,x2,y2,x1 = faceloc
            # since we scaled down by 4 times
            y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # con.close()