import face_recognition

class Human:
    serialNumber=0
    def __init__(self, fName , lName):
        self.fName = fName
        self.lName = lName

        Human.serialNumber +=1

        self.email = str(Human.serialNumber)+ "_" + fName+lName + "@nitkkr.ac.in"

    def fullname(self):
        return "{0} {1}".format(self.fName, self.lName)


class Teacher(Human):
    def __init__(self, fName, lName, dept, listClasses):
        super().__init__(fName, lName)

        self.dept = dept
        self.listClasses = listClasses# this variable would have a list of classes the Teacher is assigned for eg. MC-A


class Student(Human):
    def __init__(self, fName, lName, dept, fees, image, attendance): # this attendance variable would update as soon as the function updateAttendace is called which will update when the student attendes the class which can be updated manually or using biometrics
        super().__init__(fName, lName)
        self. dept = dept
        self.fees=fees
        self.image=image
        self.attendance=attendance
    
    def updateAttendace(self):
        self.attendance+=1

