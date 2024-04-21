from tkinter import ttk
import tkinter as tk
# Creating tkinter my_w
window = tk.Tk()
window.geometry("1000x280") 
window.title("database")  
# Using treeview widget
trv = ttk.Treeview(window, selectmode ='browse')
trv.grid(row=1,column=1,padx=30,pady=20)
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
window.mainloop()