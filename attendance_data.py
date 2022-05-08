from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog
import cv2


mydata=[] #global variable
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")





        #bg img
        img=Image.open("/Users/mufida/Desktop/mini project_Images/bg.jpeg")
        img=img.resize((1500,900),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=900)
        
        #lable
        title_lbl = Label(bg_img,text="Attendance Sheet",font=("times new roman",40,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=50,width=1500,height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=115,width=1400,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Information",font=("times new roman",20,"bold"))
        left_frame.place(x=15,y=10,width=660,height=550)

        img_right=Image.open("/Users/mufida/Desktop/mini project_Images/attendance.png")
        img_right=img_right.resize((650,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl= Label(left_frame,image= self.photoimg_right)
        f_lbl.place(x=13,y=0,width=640,height=150)

        #student attendance Information frame
        SAI_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times new roman",10,"bold"))
        SAI_frame.place(x=13,y=145,width=632,height=350)

        #Seat No.
        sem_label= Label(SAI_frame,text="Seat No. :",font=("times new roman",15,"bold"))
        sem_label.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        name_entry = ttk.Entry(SAI_frame,width = 20,font=("times new roman",15,"bold"))
        name_entry.grid(row=1,column=2,padx=2,pady=10,sticky=W)



        #roll No.
        roll_label= Label(SAI_frame,text="Roll No. :",font=("times new roman",15,"bold"))
        roll_label.grid(row=1,column=3,padx=10,pady=15,sticky=W)

        roll_entry = ttk.Entry(SAI_frame,width = 20,font=("times new roman",15,"bold"))
        roll_entry.grid(row=1,column=4,padx=2,pady=10,sticky=W)

        #Name
        name_label= Label(SAI_frame,text="Name:",font=("times new roman",15,"bold"))
        name_label.grid(row=2,column=1,padx=10,pady=15,sticky=W)

        name_entry = ttk.Entry(SAI_frame,width = 20,font=("times new roman",15,"bold"))
        name_entry.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        #Department
        department_label= Label(SAI_frame,text="Department:",font=("times new roman",15,"bold"))
        department_label.grid(row=2,column=3,padx=10,pady=15,sticky=W)

        department_entry = ttk.Entry(SAI_frame,width = 20,font=("times new roman",15,"bold"))
        department_entry.grid(row=2,column=4,padx=2,pady=10,sticky=W)
        
        #Time
        time_label= Label(SAI_frame,text="Time:",font=("times new roman",15,"bold"))
        time_label.grid(row=3,column=1,padx=10,pady=15,sticky=W)

        time_entry = ttk.Entry(SAI_frame,width = 20,font=("times new roman",15,"bold"))
        time_entry.grid(row=3,column=2,padx=2,pady=10,sticky=W)
        
        #Date
        date_label= Label(SAI_frame,text="Time:",font=("times new roman",15,"bold"))
        date_label.grid(row=3,column=3,padx=10,pady=15,sticky=W)

        date_entry = ttk.Entry(SAI_frame,width = 20,font=("times new roman",15,"bold"))
        date_entry.grid(row=3,column=4,padx=2,pady=10,sticky=W)

        # Attendance status
        Attendance_label= Label(SAI_frame,text="Attendance Status:",font=("times new roman",15,"bold"))
        Attendance_label.grid(row=4,column=1,padx=10,pady=15,sticky=W)

        Attendance_combobox= ttk.Combobox(SAI_frame,font=("times new roman",15,"bold"),width=19,state="readonly")
        Attendance_combobox["values"]=("Present","Absent")
        Attendance_combobox.current(0)
        Attendance_combobox.grid(row=4,column=2,padx=2,pady=10,sticky=W)
        
        #button frame
        button_frame_SAI=LabelFrame(SAI_frame,bd=2,relief=RIDGE)
        button_frame_SAI.place(x=0,y=250,width=625,height=35)

        #save button
        import_btn=Button(button_frame_SAI,text="Import csv",command=self.import_Cvs,width=15,font=("times new roman",15,"bold"),bg='blue',fg="black")
        import_btn.grid(row=0,column=0)

        #Update button
        update_btn=Button(button_frame_SAI,text="Export csv",width=15,font=("times new roman",15,"bold"),bg='blue',fg="black")
        update_btn.grid(row=0,column=1)

        #Delete button
        delete_btn=Button(button_frame_SAI,text="Update",width=15,font=("times new roman",15,"bold"),bg='blue',fg="black")
        delete_btn.grid(row=0,column=2)

        #Reset button
        reset_btn=Button(button_frame_SAI,text="Reset",width=14,font=("times new roman",15,"bold"),bg='blue',fg="black")
        reset_btn.grid(row=0,column=3)








        #Right label frame
        Right_SAIframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",20,"bold"))
        Right_SAIframe.place(x=700,y=10,width=660,height=550)


        #tabel frame
        Sroll_BarTabel=Frame(Right_SAIframe,bd=2,relief=RIDGE)
        Sroll_BarTabel.place(x=13,y=10,width=630,height=500)

        scroll_x = ttk.Scrollbar(Sroll_BarTabel,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Sroll_BarTabel,orient=VERTICAL)

        self.student_attendance_tabel = ttk.Treeview(Sroll_BarTabel,column=("seat_no","std_name","roll_no","div","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_attendance_tabel.xview)
        scroll_y.config(command=self.student_attendance_tabel.yview)

        self.student_attendance_tabel.heading("seat_no",text="Seat no.")
        self.student_attendance_tabel.heading("std_name",text="Name")
        self.student_attendance_tabel.heading("roll_no",text="Roll No.")
        self.student_attendance_tabel.heading("div",text="Div")
        self.student_attendance_tabel.heading("time",text="Time")
        self.student_attendance_tabel.heading("date",text="Date")
        self.student_attendance_tabel.heading("attendance",text="Attendance")
        self.student_attendance_tabel["show"]="headings"


        self.student_attendance_tabel.column("seat_no",width=100)
        self.student_attendance_tabel.column("std_name",width=100)
        self.student_attendance_tabel.column("roll_no",width=100)
        self.student_attendance_tabel.column("div",width=100)
        self.student_attendance_tabel.column("time",width=100)
        self.student_attendance_tabel.column("date",width=100)
        self.student_attendance_tabel.column("attendance",width=100)
        



        self.student_attendance_tabel.pack(fill=BOTH,expand=1)
        # self.student_attendance_tabel.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()

#=========fetch data==========
    def fetchData():
        self.student_attendance_tabel.delete(*self.student_attendance_tabel.get_children())
        for i in rows:
            self.student_attendance_tabel.insert("",END,values=i)

    
    def import_Cvs(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetype=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)



if __name__ == "__main__":
    root = Tk()
    obj=Attendance(root)
    root.mainloop()