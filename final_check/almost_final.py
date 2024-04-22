import pymysql 
# from pymysql import *
import pandas
import shutil
import os
import face

def addstudent():
    def submitadd():
        id= idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get() 
        addedtime= time.strftime("%H:%M:%S")
        addeddate= time.strftime("%d/%m/%Y")
        try:
            strr= 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id{} Name{} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot) 
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications','Id already exist try another id....',parent=addroot)
        strr= 'select * from studentdata1'
        mycursor.execute(strr)
        datas= mycursor.fetchall()
        # studenttable.delete(studenttable.get_children())
        for child in studenttable.get_children():
            studenttable.delete(child)
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
            studenttable.insert('',END,values=vv)       
        
    addroot = Toplevel(master=Dataentryframe)
    addroot.grab_set()
    addroot.geometry('530x530+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='wheat')
    addroot.iconbitmap('Webalys-Kameleon.pics-Student-3.512 (1).ico')
    addroot.resizable(False,False)
    #-------------------------------------------add student labels
    idlabel= Label(addroot,text='Enter Id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel= Label(addroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    mobilelabel= Label(addroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel= Label(addroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    addresslabel= Label(addroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel= Label(addroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    doblabel= Label(addroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    
    ##--------------------------------------------------Add student Entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    entryImgPathVar = StringVar()
    
    identry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    dobentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

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
        os.rename(entryImgPathVar.get(), dest +"/" + idval.get()+".jpg")
        entryImgPathVar.set(os.path.relpath("final_check/student_images"+f"/{idval.get()}.jpg"))
    ################----------------------------add button
    fileAdd= Button(addroot,text='Add Image',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=browseFiles)
    fileAdd.place(x=150,y=420)

    submitbtn= Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=470)
    addroot.mainloop()
    
def searchstudent():
    def search():
        id= idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get() 
        addeddate= time.strftime("%d/%m/%Y")
        if(id !=''):
            strr= 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(name !=''):
            strr= 'select * from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(mobile !=''):
            strr= 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(email !=''):
            strr= 'select * from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(address !=''):
            strr= 'select * from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(gender !=''):
            strr= 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas= mycursor.fetchall()
            studenttable.delete(studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(dob !=''):
            strr= 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
        elif(addeddate !=''):
            strr= 'select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas= mycursor.fetchall()
            # studenttable.delete(studenttable.get_children())
            for child in studenttable.get_children():
                studenttable.delete(child)
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
                studenttable.insert('',END,values=vv) 
             
    searchroot = Toplevel(master=Dataentryframe)
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='wheat') #firebrick1
    searchroot.iconbitmap('Webalys-Kameleon.pics-Student-3.512 (1).ico')
    searchroot.resizable(False,False)
    searchroot.grab_set()
    #-------------------------------------------search student labels
    idlabel= Label(searchroot,text='Enter Id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel= Label(searchroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    mobilelabel= Label(searchroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel= Label(searchroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    addresslabel= Label(searchroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel= Label(searchroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    doblabel= Label(searchroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    datelabel= Label(searchroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    
    ##--------------------------------------------------search student Entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    
    identry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    dobentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    ################----------------------------search button
    submitbtn= Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=150,y=480)
    searchroot.mainloop()
# def deletestudent():
#     cc= studenttable.focus()
#     content= studenttable.item(cc)
#     pp= content['values'][0]
#     strr= 'delete from studentdata1 where id =%s'
#     mycursor.execute(strr,(pp, ))
#     con.commit()
#     messagebox.showinfo('Notifications','Id{} deleted sucessfully...'.format(pp))
#     strr= 'select * from studentdata1'
#     mycursor.execute(strr)
#     datas= mycursor.fetchall()
#     studenttable.delete(studenttable.get_children())
#     for i in datas:
#             vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
#             studenttable.insert('',END,values=vv) 
def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id = %s'
    mycursor.execute(strr, (pp,))  # Corrected here
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully...'.format(pp))
    # strr = 'select * from studentdata1'
    # mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(cc)
    imgPath = f"final_check/student_images/{pp}.jpg"
    if os.path.exists(imgPath):
        os.remove(imgPath)
    
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def updatestudent():
    def update():
        id= idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get() 
        addeddate= dateval.get()
        addedtime= timeval.get()
        
        strr='update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,addeddate=%s,addedtime=%s where id=%s'  
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,addeddate,addedtime,id))
        con.commit()
        messagebox.showinfo('Notifications','Id{} modified sucessfully...'.format(id),parent=updateroot)
        strr= 'select * from studentdata1'
        mycursor.execute(strr)
        datas= mycursor.fetchall()
        # studenttable.delete(studenttable.get_children())
        for child in studenttable.get_children():
            studenttable.delete(child)
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
            studenttable.insert('',END,values=vv) 
    updateroot = Toplevel(master=Dataentryframe)
    updateroot.geometry('470x670+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='wheat')
    updateroot.iconbitmap('Webalys-Kameleon.pics-Student-3.512 (1).ico')
    updateroot.resizable(False,False)
    updateroot.grab_set()
    #-------------------------------------------update student labels
    idlabel= Label(updateroot,text='Enter Id:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel= Label(updateroot,text='Enter Name:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    mobilelabel= Label(updateroot,text='Enter Mobile:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel= Label(updateroot,text='Enter Email:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    addresslabel= Label(updateroot,text='Enter Address:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel= Label(updateroot,text='Enter Gender:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    doblabel= Label(updateroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    datelabel= Label(updateroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    
    timelabel= Label(updateroot,text='Enter Time:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
    ##--------------------------------------------------update student Entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()
    entryImgPathVar = StringVar()

    identry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    dobentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    timeentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)
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
        os.rename(entryImgPathVar.get(), dest +"/" + idval.get()+".jpg")
        entryImgPathVar.set(os.path.relpath("final_check/student_images"+f"/{idval.get()}.jpg"))
    ################----------------------------add button
    fileAdd= Button(updateroot,text='Add Image',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=browseFiles)
    fileAdd.place(x=150,y=540)
    ################----------------------------update button
    submitbtn= Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=150,y=590)
    cc= studenttable.focus()
    content= studenttable.item(cc)
    pp= content['values']
    if(len(pp) !=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()

def showstudent():
    strr= 'select * from studentdata1'
    mycursor.execute(strr)
    datas= mycursor.fetchall()
    # studenttable.delete(studenttable.get_children())
    for child in studenttable.get_children():
        studenttable.delete(child)
    for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]] 
            studenttable.insert('',END,values=vv) 
def exportstudent():
    ff= filedialog.asksaveasfilename()
    gg= studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime= [],[],[],[],[],[],[],[],[]
    for i in gg:
        content =  studenttable.item(i)
        pp= content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd= ['Id','Name','Mobile','Email','Adress','Gender','D.O.B','Addeddate','Addedtime']
    df= pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths= '{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student data is saved{}',format(paths))
def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res== True):
        root.destroy()
################################################################################# Connection of database
def connectdb():
    def submitdb():
        global con,mycursor
        host= "localhost" #hostval.get()
        user= "root"#userval.get()
        password= "omdevansh24"#passwordval.get()
        try:
            con= pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again')
            return
        try:
            strr= 'create database studentmanagementsystem1'
            mycursor.execute(str)
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            strr='create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr= 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected to the database...',parent=dbroot)
        except:
            
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database...',parent=dbroot)
        dbroot.destroy()
            
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.iconbitmap('Webalys-Kameleon.pics-Student-3.512 (1).ico')
    dbroot.resizable(False,False)
    dbroot.geometry('470x250+800+230')
    dbroot.config(bg='wheat')
    # idlabel=Label(root)
    idlabel=Label(dbroot,text='Enter Host : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor="w")
    idlabel.place(x=10,y=10)
    
    userlabel=Label(dbroot,text='Enter User : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor="w")
    userlabel.place(x=10,y=70)
    
    passwordlabel=Label(dbroot,text='Enter Password : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor="w")
    passwordlabel.place(x=10,y=130)
    
    #############----------------connectentry 
    hostval=StringVar()
    # hostval.set("Hello")
    userval=StringVar()
    passwordval=StringVar()
    
    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
    
    userentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwordentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    
    #-------------------------------------------------Connectdb button
    # submitbutton=Button(root,text="Submit",font=('roman',15,"bold",width=20))
    submitbutton= Button(dbroot,text='Submit',width=20,font=('roman',15,"bold"),bd=5,bg='red',relief=RIDGE,borderwidth=4,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)
    
    dbroot.mainloop()

def show_attendance():
    showAttendanceRoot = Toplevel(master=root)
    showAttendanceRoot.geometry("800x600")
    attendaceLabel = Label(master=showAttendanceRoot, text="Attendance", borderwidth=5, font=('times', 30, 'bold'),relief="ridge", background="#694A38",foreground="wheat") 
    attendaceLabel.place(x=300, y=10)
    attDataFrame=Frame(master=showAttendanceRoot,bg='white',relief=GROOVE,borderwidth=5)
    attDataFrame.place(x=80,y=80,width=650,height=520)

    ##--------------------------------------------Show data frame
    attstyle= ttk.Style()
    attstyle.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='black') #blue
    attstyle.configure('Treeview',font=('times',15,'bold'),foreground='black',background='wheat')
    att_scroll_x= Scrollbar(attDataFrame,orient=HORIZONTAL)
    att_scroll_y= Scrollbar(attDataFrame,orient=VERTICAL)
    attstudenttable=Treeview(attDataFrame,columns=('Id','Name','Last Attended', 'Total Attended'),yscrollcommand=scroll_y.set,xscrollcommand=att_scroll_x.set)
    att_scroll_x.pack(side=BOTTOM,fill=X)
    att_scroll_y.pack(side=RIGHT,fill=Y)
    att_scroll_x.config(command=attstudenttable.xview)
    att_scroll_y.config(command=attstudenttable.yview)
    attstudenttable.heading('Id',text='Id')
    attstudenttable.heading('Name',text='Name')
    attstudenttable.heading('Last Attended',text='Last Attended')
    attstudenttable.heading('Total Attended',text='Total Attended')
    attstudenttable['show']='headings'
    attstudenttable.column('Id',width=100)
    attstudenttable.column('Name',width=200)
    attstudenttable.column('Last Attended',width=150)
    attstudenttable.column('Total Attended',width=150)
    attstudenttable.pack(fill=BOTH,expand=1)

    strr= 'SELECT studentattendance1.id, studentdata1.name, studentattendance1.lastClassAttended, studentattendance1.numOfClasses from studentattendance1 join studentdata1 on studentattendance1.id = studentdata1.id;'
    mycursor.execute(strr)
    datas= mycursor.fetchall()
    # studenttable.delete(studenttable.get_children())
    for child in attstudenttable.get_children():
        attstudenttable.delete(child)
    for i in datas:
            dataForColumns=[i[0],i[1],i[2],i[3]] 
            attstudenttable.insert('',END,values=dataForColumns)

def mark_att():
    # os.system("final_check/face.py")
    face.mainFunction()

def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    # print(time_string,date_string)
    clock.config(text="Date :"+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)
#################################################################### Intro Slider
import random
colors=['red','green','blue','yellow','pink','red2','gold2']
def introlabelcolorpicker():
    fg= random.choice(colors)
    # print(fg)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,introlabelcolorpicker)
def introlabel():
    global count,text
    if(count>=len(ss)):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
    count+=1
    SliderLabel.after(200,introlabel)

from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
# import pandas
# import pymysql
from pandas import *
from pymysql import *
import time
import random

root=Tk()
root.title("Student Management System")
root.config(bg='#694A38') # 694A38 #2C3531
root.geometry('1274x730+200+50')
root.iconbitmap('Webalys-Kameleon.pics-Student-3.512 (1).ico')
root.resizable(False,False)
#################################################################### frames
##------------------------------------ dataentry frame 

Dataentryframe=Frame(master=root,bg='wheat',relief=GROOVE,borderwidth=5)
Dataentryframe.place(x=10,y=80,width=500,height=600)
frontlabel = Label(Dataentryframe, text='-------------Welcome---------------',width=30, font= ('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(Dataentryframe,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(Dataentryframe,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(Dataentryframe,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(Dataentryframe,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(Dataentryframe,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(Dataentryframe,text='6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(Dataentryframe,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
##------------------------------------Show data frame
Showdataframe=Frame(master=root,bg='white',relief=GROOVE,borderwidth=5)
Showdataframe.place(x=550,y=80,width=620,height=600)

##--------------------------------------------Show data frame
style= ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='black') # blue
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='#F6DEB3') #cyan
scroll_x= Scrollbar(Showdataframe,orient=HORIZONTAL)
scroll_y= Scrollbar(Showdataframe,orient=VERTICAL)
studenttable=Treeview(Showdataframe,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)
#################################################################### Slider
ss= 'Welcome To Student Management System'
count=0
text =''
###################################################################
SliderLabel=Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='#0E1C36') # bg = 'cyan'
SliderLabel.place(x=160,y=0)
introlabel()
introlabelcolorpicker()
##################################################################### clock
clock=Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='wheat')#lawn green
clock.place(x=0,y=0)
tick()
################################################################ Button to connect database
connectbutton= Button(root,text='Connect to Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',activebackground='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)

showAttendanceButton = Button(master=root, text="Show Attendance", width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4, command=show_attendance)
showAttendanceButton.place(x=930, y=690)

markAttendanceButton = Button(master=root, text="Mark Attendance", width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4, command=mark_att)
markAttendanceButton.place(x=560, y=690)

root.mainloop()

