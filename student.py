from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=====variables======
        self.var_dep=StringVar()
        self.var_course=StringVar() 
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_seat_no=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #bg img
        img=Image.open("/Users/mufida/Desktop/mini project_Images/bg.jpeg")
        img=img.resize((1500,900),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=900)
        
        #lable
        title_lbl = Label(bg_img,text="Student Details",font=("times new roman",40,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=50,width=1500,height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=115,width=1400,height=750)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",20,"bold"))
        left_frame.place(x=10,y=10,width=660,height=700)


        #current Course Information
        CCI_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"))
        CCI_frame.place(x=13,y=5,width=632,height=130)

        #department
        dep_label= Label(CCI_frame,text="Department:",font=("times new roman",15,"bold"))
        dep_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        dep_combobox= ttk.Combobox(CCI_frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),width=20,state="readonly")
        dep_combobox["values"]=("Select Department","Comps","IT","Instru","Extc","Etrx")
        dep_combobox.current(0)
        dep_combobox.grid(row=0,column=1,padx=2,pady=15,sticky=W)


        #Course
        course_label= Label(CCI_frame,text="Course:",font=("times new roman",15,"bold"))
        course_label.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        course_combobox= ttk.Combobox(CCI_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),width=20,state="readonly")
        course_combobox["values"]=("Select Course","FE","SE","TE","BE")
        course_combobox.current(0)
        course_combobox.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label= Label(CCI_frame,text="Year:",font=("times new roman",15,"bold"))
        year_label.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        year_combobox= ttk.Combobox(CCI_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),width=20,state="readonly")
        year_combobox["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combobox.current(0)
        year_combobox.grid(row=1,column=1,padx=2,pady=10,sticky=W)



        #sem
        sem_label= Label(CCI_frame,text="Semester:",font=("times new roman",15,"bold"))
        sem_label.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        sem_combobox= ttk.Combobox(CCI_frame,textvariable=self.var_sem,font=("times new roman",15,"bold"),width=20,state="readonly")
        sem_combobox["values"]=("Select Semester","SEM-1","SEM-2","SEM-3","SEM-4")
        sem_combobox.current(0)
        sem_combobox.grid(row=1,column=3,padx=2,pady=10,sticky=W)






        #student class Information
        SCI_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Class Information",font=("times new roman",10,"bold"))
        SCI_frame.place(x=13,y=145,width=632,height=520)

        #roll No.
        roll_label= Label(SCI_frame,text="Roll No. :",font=("times new roman",15,"bold"))
        roll_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        roll_entry = ttk.Entry(SCI_frame,textvariable=self.var_roll_no,width = 20,font=("times new roman",15,"bold"))
        roll_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        


        #Name
        name_label= Label(SCI_frame,text="Name:",font=("times new roman",15,"bold"))
        name_label.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        name_entry = ttk.Entry(SCI_frame,textvariable=self.var_std_name,width = 20,font=("times new roman",15,"bold"))
        name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # Division
        Div_label= Label(SCI_frame,text="Division:",font=("times new roman",15,"bold"))
        Div_label.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        Div_combobox= ttk.Combobox(SCI_frame,textvariable=self.var_div,font=("times new roman",15,"bold"),width=19,state="readonly")
        Div_combobox["values"]=("Select Division","A","B","C","D")
        Div_combobox.current(0)
        Div_combobox.grid(row=1,column=1,padx=2,pady=10,sticky=W)



        #Seat No.
        sem_label= Label(SCI_frame,text="Seat No. :",font=("times new roman",15,"bold"))
        sem_label.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        name_entry = ttk.Entry(SCI_frame,textvariable=self.var_seat_no,width = 20,font=("times new roman",15,"bold"))
        name_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Gender
        Gen_label= Label(SCI_frame,text="Gender:",font=("times new roman",15,"bold"))
        Gen_label.grid(row=2,column=0,padx=10,pady=15,sticky=W)

        Gen_combobox= ttk.Combobox(SCI_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),width=19,state="readonly")
        Gen_combobox["values"]=("Select Gender","Male","Female","Other")
        Gen_combobox.current(0)
        Gen_combobox.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #DOB
        DOB_label= Label(SCI_frame,text="DOB :",font=("times new roman",15,"bold"))
        DOB_label.grid(row=2,column=2,padx=10,pady=15,sticky=W)

        DOB_entry = ttk.Entry(SCI_frame,textvariable=self.var_dob,width = 20,font=("times new roman",15,"bold"))
        DOB_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)


        #Email
        email_label= Label(SCI_frame,text="Email ID :",font=("times new roman",15,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=15,sticky=W)

        email_entry = ttk.Entry(SCI_frame,textvariable=self.var_email,width = 20,font=("times new roman",15,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #Phone number
        phone_label= Label(SCI_frame,text="Phone No. :",font=("times new roman",15,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=15,sticky=W)

        phone_entry = ttk.Entry(SCI_frame,textvariable=self.var_phone,width = 20,font=("times new roman",15,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)


         #Address
        Add_label= Label(SCI_frame,text="Address :",font=("times new roman",15,"bold"))
        Add_label.grid(row=4,column=0,padx=10,pady=15,sticky=W)

        Add_entry = ttk.Entry(SCI_frame,textvariable=self.var_address,width = 20,font=("times new roman",15,"bold"))
        Add_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        #teachers name
        teacher_label= Label(SCI_frame,text="Teachers Name :",font=("times new roman",15,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=15,sticky=W)

        teacher_entry = ttk.Entry(SCI_frame,textvariable=self.var_teacher,width = 20,font=("times new roman",15,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        #Radio button frame
        button_frame=LabelFrame(SCI_frame)
        button_frame.place(x=0,y=265,width=620,height=30)

        #Radio button
        self.var_radio1=StringVar()
        radiobutton1 = Radiobutton(button_frame,variable=self.var_radio1,text= "Take Photo Sample", value="Yes")
        radiobutton1.grid(row=6,column=0)

        
        radiobutton2 = Radiobutton(button_frame,variable=self.var_radio1,text= "No Photo Sample", value="No")
        radiobutton2.grid(row=6,column=1)

        #button frame
        button_frame=LabelFrame(SCI_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=300,width=625,height=70)

        #save button
        save_btn=Button(button_frame,text="Save",command=self.add_data,width=15,font=("times new roman",15,"bold"),bg='blue',fg="black")
        save_btn.grid(row=0,column=0)

        #Update button
        update_btn=Button(button_frame,text="Update",command=self.update_data,width=15,font=("times new roman",15,"bold"),bg='blue',fg="black")
        update_btn.grid(row=0,column=1)

        #Delete button
        delete_btn=Button(button_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",15,"bold"),bg='blue',fg="black")
        delete_btn.grid(row=0,column=2)

        #Reset button
        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",15,"bold"),bg='blue',fg="black")
        reset_btn.grid(row=0,column=3)

        #button frame 2
        button_frame2=LabelFrame(button_frame,bd=2,relief=RIDGE)
        button_frame2.place(x=0,y=30,width=620,height=30)

        add_photo_btn=Button(button_frame2,command=self.generate_data,text="Take Photo",width=35,font=("times new roman",15,"bold"),bg='blue',fg="black")
        add_photo_btn.grid(row=0,column=1)

        update_photo_btn=Button(button_frame2,text="Update Photo",width=35,font=("times new roman",15,"bold"),bg='blue',fg="black")
        update_photo_btn.grid(row=0,column=2)

        
        #Left image
        img_Left=Image.open("/Users/mufida/Desktop/mini project_Images/rightimage.jpeg")
        img_Left=img_Left.resize((650,130),Image.ANTIALIAS)
        self.photoimg_Left=ImageTk.PhotoImage(img_Left)

        f_lbl= Label(SCI_frame,image= self.photoimg_Left)
        f_lbl.place(x=3,y=375,width=640,height=130)

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
        Right_frame.place(x=700,y=10,width=660,height=700)

        img_right=Image.open("/Users/mufida/Desktop/mini project_Images/rightimage.jpeg")
        img_right=img_right.resize((640,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl= Label(Right_frame,image= self.photoimg_right)
        f_lbl.place(x=5,y=0,width=640,height=130)
         
        #search frame
        SearchBar_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",10,"bold"))
        SearchBar_frame.place(x=13,y=145,width=630,height=70)
        
        Search_label= Label(SearchBar_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red")
        Search_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        Search_combobox= ttk.Combobox(SearchBar_frame,font=("times new roman",15,"bold"),width=15,state="readonly")
        Search_combobox["values"]=("Select","Roll No.","Phone No.")
        Search_combobox.current(0)
        Search_combobox.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(SearchBar_frame,width = 15,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        search_btn=Button(SearchBar_frame,text="Search",width=10,font=("times new roman",15,"bold"),bg='blue',fg="black")
        search_btn.grid(row=0,column=3)

        showALL_btn=Button(SearchBar_frame,text="Show All",width=10,font=("times new roman",15,"bold"),bg='blue',fg="black")
        showALL_btn.grid(row=0,column=4)

        
        #tabel frame
        tabel_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        tabel_frame.place(x=13,y=220,width=630,height=300)

        scroll_x = ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.student_tabel = ttk.Treeview(tabel_frame,column=("Department","Course","Year","Sem","Id","Name","Div","Roll No.","Gender","DOB","Email","Phone No.","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        self.student_tabel.heading("Department",text="Department")
        self.student_tabel.heading("Course",text="Course")
        self.student_tabel.heading("Year",text="Year")
        self.student_tabel.heading("Sem",text="Sem")
        self.student_tabel.heading("Id",text="Id")
        self.student_tabel.heading("Name",text="Name")
        self.student_tabel.heading("Div",text="Div")
        self.student_tabel.heading("Roll No.",text="Roll No.")
        self.student_tabel.heading("Gender",text="Gender")
        self.student_tabel.heading("DOB",text="DOB")
        self.student_tabel.heading("Email",text="Email")
        self.student_tabel.heading("Phone No.",text="Phone No.")
        self.student_tabel.heading("Address",text="Address")
        self.student_tabel.heading("Teacher",text="Teacher")
        self.student_tabel.heading("Photo",text="Photo")
        self.student_tabel["show"]="headings"


        self.student_tabel.column("Department",width=100)
        self.student_tabel.column("Course",width=100)
        self.student_tabel.column("Year",width=100)
        self.student_tabel.column("Sem",width=100)
        self.student_tabel.column("Id",width=100)
        self.student_tabel.column("Name",width=100)
        self.student_tabel.column("Div",width=100)
        self.student_tabel.column("Roll No.",width=100)
        self.student_tabel.column("Gender",width=100)
        self.student_tabel.column("DOB",width=100)
        self.student_tabel.column("Email",width=100)
        self.student_tabel.column("Phone No.",width=100)
        self.student_tabel.column("Address",width=100)
        self.student_tabel.column("Teacher",width=100)
        self.student_tabel.column("Photo",width=150)



        self.student_tabel.pack(fill=BOTH,expand=1)
        self.student_tabel.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    


    

    #======function declaration========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_seat_no.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="root@123",db="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   self.var_dep.get(),
                                                                                                   self.var_course.get(), 
                                                                                                   self.var_year.get(),
                                                                                                   self.var_sem.get(),
                                                                                                   self.var_seat_no.get(),
                                                                                                   self.var_std_name.get(),
                                                                                                   self.var_div.get(),
                                                                                                   self.var_roll_no.get(),
                                                                                                   self.var_gender.get(),
                                                                                                   self.var_dob.get(),
                                                                                                   self.var_email.get(),
                                                                                                   self.var_phone.get(),
                                                                                                   self.var_address.get(),
                                                                                                   self.var_teacher.get(),
                                                                                                   self.var_radio1.get() 

                                                                                             ))
                                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


      #=====fetch data======         
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="root@123",db="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("",END,values=i)
            conn.commit()
        conn.close()


    
    #========get cursor========
    def get_cursor(self,event=""):
        cursor_focus=self.student_tabel.focus()
        content=self.student_tabel.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_seat_no.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


#updat data function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_seat_no.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="root@123",db="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set `dep`=%s,`course`=%s,`year`=%s,`sem`=%s,`std_name`=%s,`div`=%s,`roll_no`=%s,`gender`=%s,`dob`=%s,`email`=%s,`phone`=%s,`address`=%s,`teacher`=%s,`photoSampple`=%s where `seat_no`=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(), 
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_sem.get(),                                                                                                                                                                                     
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll_no.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),  
                                                                                                                                                                                        self.var_seat_no.get()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                     ))
                                                                  
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

# delete function
    def delete_data(self):
        if self.var_seat_no.get()=="":
            messagebox.showerror("Error","Seat number is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="root@123",db="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where seat_no=%s"
                    val=(self.var_seat_no.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()      
                messagebox.showinfo("Deleted","Successfuly deleted student details",parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

# reset fun
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"), 
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_seat_no.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll_no.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("") 

#Generate data set or Take photo sample
    
    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_seat_no.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:             
                conn=mysql.connector.connect(host="localhost",user="root",passwd="root@123",db="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set `dep`=%s,`course`=%s,`year`=%s,`sem`=%s,`std_name`=%s,`div`=%s,`roll_no`=%s,`gender`=%s,`dob`=%s,`email`=%s,`phone`=%s,`address`=%s,`teacher`=%s,`photoSampple`=%s where `seat_no`=%s",(
                                                                                                               
                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                          self.var_course.get(), 
                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                          self.var_sem.get(),
                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                          self.var_roll_no.get(),
                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                          self.var_seat_no.get()== id+1                                           
                                                                                                                                                                                     ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predifiend data on face frontals from opencv==== 

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3  
                    # Minimum neighbor =5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
 
               
                cap=cv2.VideoCapture(0)
                img_id=0
                # detector = cv2.CascadeClassifier(harcascadePath)
                while True:
                    ret,my_frame=cap.read() 
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        # img = cv2.imread(file_path)
                        cv2.imwrite(file_path,my_frame)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            
            
        





if __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()