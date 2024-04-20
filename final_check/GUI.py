from tkinter import *
from ttkbootstrap import *
from tkinter import filedialog
import os
import shutil
import csv
# import pandas as pd

class Database:
    def __init__(self, file_path):
        # self.file_path = file_path
        # self.data = pd.read_csv(file_path)
        self.file_path = file_path
        self.firstrow=["name", "rollno", "imagepath"]

    def insert(self, record):
        # self.data = self.data.append(record, ignore_index=True)
        # self.data = pd.concat([self.data, pd.DataFrame([record])], ignore_index=True)
        # self.data.to_csv(self.file_path, index=False)
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
        data.append(record)
        with open(self.file_path, "w") as file:
            writer = csv.DictWriter(file, fieldnames=self.firstrow)
            writer.writeheader()
            writer.writerows(data)

    def update(self, rollno, new_record):
        # self.data.loc[index] = new_record
        # self.data.to_csv(self.file_path, index=False)
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                if(row["rollno"]!=rollno):
                    data.append(row)
                else:
                    data.append(new_record)
        with open(self.file_path, "w") as file:
            writer = csv.DictWriter(file, fieldnames=self.firstrow)
            writer.writeheader()
            writer.writerows(data)
            

    def delete(self, rollno):
        # self.data.drop(index, inplace=True)
        # self.data.to_csv(self.file_path, index=False)
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                if(row["rollno"]!=rollno):
                    data.append(row)
        with open(self.file_path, "w") as file:
            writer = csv.DictWriter(file, fieldnames=self.firstrow)
            writer.writeheader()
            writer.writerows(data)

    def query(self, rollno):
        # result = self.data.query(query_string)
        # return result
        with open(self.file_path, "r") as file:
            data = dict()
            read_val = csv.DictReader(file)
            for row in read_val:
                if(row["rollno"]==rollno):
                    return row
        
        return data



def add_student():
    add_stu_win = Tk()
    add_stu_win.geometry("600x600")
    
    db = Database("final_check\database.csv")

    entryFrame = Frame(master= add_stu_win)
    nameLabel = Label(master= entryFrame, text="Name: ")
    entryNameVar = StringVar(master=add_stu_win)
    nameEntry = Entry(master=entryFrame, textvariable=entryNameVar)
    nameLabel.pack(side="left")
    nameEntry.pack(padx=10)
    entryFrame.pack(pady=10)

    entryFrameRoll = Frame(master= add_stu_win)
    RollNo = Label(master= entryFrameRoll, text="Roll Number: ")
    entryRollVar = StringVar(master=add_stu_win)
    RollEntry = Entry(master=entryFrameRoll, textvariable=entryRollVar)
    RollNo.pack(side="left")
    RollEntry.pack(padx=10)
    entryFrameRoll.pack(pady=10)


    entryImgPathVar = StringVar(master=add_stu_win)
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Image Files",
                                                            "*.jpg*"),
                                                        ("all files",
                                                            "*.*")))
        
        src =filename
        dest = "final_check\student_images"
        entryImgPathVar.set(filename)

        # Use os.system to execute the cp shell command
        # os.system(f"cp {src} {dest}")
        shutil.copy(src, dest)

    filebrowserButton = Button(master= add_stu_win, text="Choose Image File", command=browseFiles)
    filebrowserButton.pack()


    def done():
        db.insert({"name":entryNameVar.get(),"rollno":entryRollVar.get(),"imagepath":entryImgPathVar.get()})
        
        add_stu_win.destroy()

    done_button = Button(master= add_stu_win, text="Done", command=done)
    done_button.pack()
    add_stu_win.mainloop()


window = Tk()
window.geometry("800x800")

with open("final_check/database.csv", "r") as fobj:
    read_val = csv.DictReader(fobj)
    data_listed = []
    for row in read_val:
        data_listed.append(row)

FrameHead = Frame(master=window)
labelHeadName = Label(master=FrameHead, text="Name")
labelRollName = Label(master=FrameHead, text="Roll Number")
labelPathImgName = Label(master=FrameHead, text="Image Path")
labelHeadName.pack(side="left")
labelRollName.pack(side="left")
labelPathImgName.pack(side="right")
FrameHead.pack()

if(len(data_listed)!=0):
    labelHeadName = Label(master=window, text="No Students")
    labelHeadName.pack()
else:
    for data_row in data_listed:
        FrameHead = Frame(master=window)
        labelHeadName = Label(master=FrameHead, text=data_row["name"])
        labelRollName = Label(master=FrameHead, text=data_row["rollno"])
        labelPathImgName = Label(master=FrameHead, text=data_row["imagepath"])
        labelHeadName.pack(side="left")
        labelRollName.pack(side="left")
        labelPathImgName.pack(side="right")
        FrameHead.pack()



button = Button(master= window, text="Add a new student", command=add_student)
button.pack()

window.mainloop()