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
                else:
                    if os.path.exists(row["imagepath"]):
                        os.remove(row["imagepath"])
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
    
    db = Database("final_check/database.csv")

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
        dest = "final_check/student_images"
        entryImgPathVar.set(filename)

        # Use os.system to execute the cp shell command
        # os.system(f"cp {src} {dest}")
        shutil.copy(src, dest)
        split_about_slash = filename.split("/")
        entryImgPathVar.set(dest +"/" +split_about_slash[-1])
        os.rename(entryImgPathVar.get(), dest +"/" + entryRollVar.get()+".jpg")
        entryImgPathVar.set(os.path.relpath("final_check/student_images"+f"/{entryRollVar.get()}.jpg"))
        # os.path.abspath() for absolute path

    filebrowserButton = Button(master= add_stu_win, text="Choose Image File", command=browseFiles)
    filebrowserButton.pack()


    def done():
        db.insert({"name":entryNameVar.get(),"rollno":entryRollVar.get(),"imagepath":entryImgPathVar.get()})
        
        add_stu_win.destroy()

    done_button = Button(master= add_stu_win, text="Done", command=done)
    done_button.pack()
    add_stu_win.mainloop()


def delete():
    db = Database("final_check/database.csv")
    del_stu_win = Tk()
    del_stu_win.geometry("600x600")

    entryFrameRoll = Frame(master= del_stu_win)
    RollNo = Label(master= entryFrameRoll, text="Roll Number: ")
    delRollVar = StringVar(master=del_stu_win)
    RollEntry = Entry(master=entryFrameRoll, textvariable=delRollVar)
    RollNo.pack(side="left")
    RollEntry.pack(padx=10)
    entryFrameRoll.pack(pady=10)

    def done():
        db.delete(delRollVar.get())
        del_stu_win.destroy()

    done_button = Button(master= del_stu_win, text="Done", command=done)
    done_button.pack()
    del_stu_win.mainloop()


window = Tk()
window.geometry("1000x800")
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
trv = ttk.Treeview(window, selectmode ='browse')
trv.grid(row=1,column=0,padx=30,pady=20)
import csv
file = open('final_check/database.csv') # Path of CSV data file
csvreader = csv.reader(file)
l1 = []
l1 = next(csvreader) # column headers as first row 
r_set = [row for row in csvreader]
# Data Sources to create header list and row of data is over. 
# Adding headers and columns using lists 
#l1=['id','Name','Class','Mark','Gender'] # sample list for testing
trv['height']=10 # Number of rows to display, default is 10
trv['show'] = 'headings' 
# column identifiers 
trv["columns"] = l1
# Defining headings, other option in tree
# width of columns and alignment 
for i in l1:
    trv.column(i, width = 300, anchor ='c')
	# Headings of respective columns
    trv.heading(i, text =i)

## Adding data to treeview 
for dt in r_set:  
    v=[r for r in dt] # creating a list from each row 
    trv.insert("",'end',iid=v[0],values=v) # adding row
#data=[1,'Alex','Four',45,'Male'] # sample data to insert 
#trv.insert("",'end',iid=1,values=data)


def refresh():
    window = Tk()
    window.geometry("1000x800")

    trv = ttk.Treeview(window, selectmode ='browse')
    trv.grid(row=1,column=0,padx=30,pady=20)
    import csv
    file = open('final_check/database.csv') # Path of CSV data file
    csvreader = csv.reader(file)
    l1 = []
    l1 = next(csvreader) # column headers as first row 
    r_set = [row for row in csvreader]
    # Data Sources to create header list and row of data is over. 
    # Adding headers and columns using lists 
    #l1=['id','Name','Class','Mark','Gender'] # sample list for testing
    trv['height']=10 # Number of rows to display, default is 10
    trv['show'] = 'headings' 
    # column identifiers 
    trv["columns"] = l1
    # Defining headings, other option in tree
    # width of columns and alignment 
    for i in l1:
        trv.column(i, width = 300, anchor ='c')
        # Headings of respective columns
        trv.heading(i, text =i)

    ## Adding data to treeview 
    for dt in r_set:  
        v=[r for r in dt] # creating a list from each row 
        trv.insert("",'end',iid=v[0],values=v) # adding row
    #data=[1,'Alex','Four',45,'Male'] # sample data to insert 
    #trv.insert("",'end',iid=1,values=data)
    button = Button(master= window, text="Add a new student", command=add_student)
    button.grid(row=2)

    refreshButton = Button(master=window, text="Refresh", command=lambda: [window.destroy(),refresh()])
    refreshButton.grid(row=3)

    delButton = Button(master= window, text="Delete student", command=delete)
    delButton.grid(row= 4)
    window.mainloop()



button = Button(master= window, text="Add a new student", command=add_student)
button.grid(row=2)

refreshButton = Button(master=window, text="Refresh", command=lambda: [window.destroy(),refresh()])

refreshButton.grid(row=3)

delButton = Button(master= window, text="Delete student", command=delete)
delButton.grid(row=4)

window.mainloop()