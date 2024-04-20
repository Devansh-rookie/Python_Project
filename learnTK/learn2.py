from tkinter import *
from ttkbootstrap import *
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    (filename)


def add_student():
    add_stu_win = Tk()
    add_stu_win.geometry("600x600")
    def done():

        add_stu_win.destroy()
    
    done_button = Button(master= add_stu_win, text="Done", command=done)
    done_button.pack()
    add_stu_win.mainloop()


window = Tk()
window.geometry("800x800")
button = Button(master= window, text="Add a new student", command=add_student)
button.pack()

window.mainloop()