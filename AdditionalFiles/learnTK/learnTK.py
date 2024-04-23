from tkinter import *
from ttkbootstrap import *
def convert():
    mile = entry_var.get()
    kms = mile*1.615
    output_string.set(f"The converted value to kms is: {kms}")

# window = Tk()
window = Window(themename="darkly")

window.title("Miles to Kimomters")
window.geometry("800x400")

title_label = Label(master=window, text="Miles to Kilometers", font= "Calibri 24 bold")
title_label.pack()

input_frame = Frame(master= window)
entry_var = IntVar()
entry = Entry(master=input_frame, textvariable=entry_var)
button = Button(master= input_frame, command=convert, text= "Convert")
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady= 20)

output_string = StringVar()
output_label = Label(master= window, textvariable=output_string, font="Calibri 30 bold")
output_label.pack()
window.mainloop()