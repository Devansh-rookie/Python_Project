from tkinter import *
from tkinter import filedialog
from ttkbootstrap import Style
import os
import shutil
import csv

class Database:
    def __init__(self, file_path):
        self.file_path = file_path
        self.firstrow = ["name", "rollno", "imagepath"]

    def insert(self, record):
        with open(self.file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.firstrow)
            writer.writerow(record)

    def update(self, rollno, new_record):
        data = []
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["rollno"] != rollno:
                    data.append(row)
                else:
                    data.append(new_record)
        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.firstrow)
            writer.writeheader()
            writer.writerows(data)

    def delete(self, rollno):
        data = []
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["rollno"] != rollno:
                    data.append(row)
                else:
                    if os.path.exists(row["imagepath"]):
                        os.remove(row["imagepath"])
        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.firstrow)
            writer.writeheader()
            writer.writerows(data)

    def query(self, rollno):
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["rollno"] == rollno:
                    return row
        return {}


def add_student():
    add_stu_win = Tk()
    add_stu_win.geometry("500x300")
    add_stu_win.title("Add Student")

    style = Style(theme='darkly')  # Change theme here if needed

    db = Database("final_check/database.csv")

    def browse_files():
        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(("Image Files", "*.jpg*"), ("all files", "*.*"))
        )
        entry_img_path_var.set(filename)

    entry_frame = Frame(master=add_stu_win)
    entry_frame.pack(pady=10)

    Label(master=entry_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    entry_name_var = StringVar(master=add_stu_win)
    Entry(master=entry_frame, textvariable=entry_name_var).grid(row=0, column=1, padx=5, pady=5)

    Label(master=entry_frame, text="Roll Number:").grid(row=1, column=0, padx=5, pady=5)
    entry_roll_var = StringVar(master=add_stu_win)
    Entry(master=entry_frame, textvariable=entry_roll_var).grid(row=1, column=1, padx=5, pady=5)

    entry_img_path_var = StringVar(master=add_stu_win)
    Button(master=entry_frame, text="Choose Image File", command=browse_files).grid(row=2, column=0, columnspan=2, pady=5)

    def done():
        db.insert({"name": entry_name_var.get(), "rollno": entry_roll_var.get(), "imagepath": entry_img_path_var.get()})
        add_stu_win.destroy()

    Button(master=add_stu_win, text="Done", command=done).pack()

    add_stu_win.mainloop()


def delete():
    db = Database("final_check/database.csv")
    del_stu_win = Tk()
    del_stu_win.geometry("300x150")
    del_stu_win.title("Delete Student")

    def done():
        db.delete(del_roll_var.get())
        del_stu_win.destroy()

    entry_frame = Frame(master=del_stu_win)
    entry_frame.pack(pady=10)

    Label(master=entry_frame, text="Roll Number:").grid(row=0, column=0, padx=5, pady=5)
    del_roll_var = StringVar(master=del_stu_win)
    Entry(master=entry_frame, textvariable=del_roll_var).grid(row=0, column=1, padx=5, pady=5)

    Button(master=del_stu_win, text="Done", command=done).pack()

    del_stu_win.mainloop()


def refresh():
    window.destroy()
    display_students()


def display_students():
    window = Tk()
    window.geometry("800x600")
    window.title("Student Database")

    with open("final_check/database.csv", "r") as fobj:
        reader = csv.DictReader(fobj)
        data_listed = list(reader)

    if len(data_listed) == 0:
        Label(master=window, text="No Students").pack()
    else:
        for data_row in data_listed:
            frame = Frame(master=window)
            frame.pack(anchor="w", pady=5)

            Label(master=frame, text=data_row["name"]).grid(row=0, column=0, padx=10)
            Label(master=frame, text=data_row["rollno"]).grid(row=0, column=1, padx=10)
            Label(master=frame, text=data_row["imagepath"]).grid(row=0, column=2, padx=10)

    Button(master=window, text="Add a new student", command=add_student).pack()
    Button(master=window, text="Refresh", command=refresh).pack()
    Button(master=window, text="Delete student", command=delete).pack()

    window.mainloop()


if __name__ == "__main__":
    display_students()
