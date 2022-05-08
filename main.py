from tkinter import*
from tkinter import Tk
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
import numpy as np
import cv2
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from attendance_data import Attendance
from developer import Developer_code


class Face_Recog_System:
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
        title_lbl = Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",40,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=100,width=1500,height=50)


        #button1
        but1=Image.open("/Users/mufida/Desktop/mini project_Images/students_details.jpeg")
        but1=but1.resize((220,220),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(but1)

        b1=Button(bg_img,image=self.photoimg1,command=self.students_func1,cursor="hand")
        b1.place(x=300,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Students Details",command=self.students_func1,cursor="hand",font=("times new roman",15,"bold"),fg="black")
        b1_1.place(x=300,y=380,width=220,height=40)

        #button2
        but2=Image.open("/Users/mufida/Desktop/mini project_Images/img1.jpeg")
        but2=but2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(but2)

        b2=Button(bg_img,image=self.photoimg2,cursor="hand",command= self.face_recogi)
        b2.place(x=900,y=200,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector",cursor="hand",command= self.face_recogi,font=("times new roman",15,"bold"),fg="black")
        b2_2.place(x=900,y=380,width=220,height=40)

        #button3
        # but3=Image.open("/Users/mufida/Desktop/mini project_Images/attendance.jpeg")
        # but3=but3.resize((220,220),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(but3)

        # b3=Button(bg_img,image=self.photoimg3,cursor="hand")
        # b3.place(x=800,y=200,width=220,height=220)

        # b3_3=Button(bg_img,text="Attendance",cursor="hand",font=("times new roman",15,"bold"),fg="black")
        # b3_3.place(x=800,y=380,width=220,height=40)


        #button4
        # but4=Image.open("/Users/mufida/Desktop/mini project_Images/helpdesk.png")
        # but4=but4.resize((220,220),Image.ANTIALIAS)
        # self.photoimg4=ImageTk.PhotoImage(but4)

        # b4=Button(bg_img,image=self.photoimg4,cursor="hand")
        # b4.place(x=1100,y=200,width=220,height=220)

        # b4_4=Button(bg_img,text="Help Desk",cursor="hand",font=("times new roman",15,"bold"),fg="black")
        # b4_4.place(x=1100,y=380,width=220,height=40)



        #button5
        but5=Image.open("/Users/mufida/Desktop/mini project_Images/traindata.jpeg")
        but5=but5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(but5)

        b5=Button(bg_img,image=self.photoimg5,cursor="hand",command= self.train_classifier)
        b5.place(x=600,y=200,width=220,height=220)

        b5_5=Button(bg_img,text="Train Data",cursor="hand",command= self.train_classifier ,font=("times new roman",15,"bold"),fg="black")
        b5_5.place(x=600,y=380,width=220,height=40)

        #button6
        but6=Image.open("/Users/mufida/Desktop/mini project_Images/photos.png")
        but6=but6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(but6)

        b6=Button(bg_img,image=self.photoimg6,cursor="hand",command= self.open_img)
        b6.place(x=450,y=500,width=220,height=220)

        b6_6=Button(bg_img,text="Photos",cursor="hand",command= self.open_img,font=("times new roman",15,"bold"),fg="black")
        b6_6.place(x=450,y=680,width=220,height=40)

        #button7
        but7=Image.open("/Users/mufida/Desktop/mini project_Images/developer.jpeg")
        but7=but7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(but7)

        b7=Button(bg_img,image=self.photoimg7,cursor="hand",command=self.developer_func2)
        b7.place(x=750,y=500,width=220,height=220)

        b7_7=Button(bg_img,text="Developer",cursor="hand",command=self.developer_func2,font=("times new roman",15,"bold"),fg="black")
        b7_7.place(x=750,y=680,width=220,height=40)


        #button8
        # but8=Image.open("/Users/mufida/Desktop/mini project_Images/logout.jpeg")
        # but8=but8.resize((220,220),Image.ANTIALIAS)
        # self.photoimg8=ImageTk.PhotoImage(but8)

        # b8=Button(bg_img,image=self.photoimg8,cursor="hand")
        # b8.place(x=1100,y=500,width=220,height=220)

        # b8_8=Button(bg_img,text="Logout",cursor="hand",font=("times new roman",15,"bold"),fg="black")
        # b8_8.place(x=1100,y=680,width=220,height=40)
    

    def open_img(self):
        # os.startfile("/Users/mufida/Desktop/MINI PROJECT/data")
        os.system("open data")
        


        # ========function buttons=======

    def students_func1(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    # def attendance_func1(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Attendance(self.new_window)

    def developer_func2(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer_code(self.new_window)
    
    
#=====train data========
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        # for imagePath in path:
        #     if imagePath == "data" + '.DS_Store':
        #         continue
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append (id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train data classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


   




  #====face recog fun======


    def face_recogi(self):
        def draw_boundray(img,classifier,scaleFactor, minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=faceCascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5)
            coord=[]
            for (x,y,w,h) in features:
                
                cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                

                conn=mysql.connector.connect(host="localhost",user="root",passwd="root@123",db="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select std_name from student where seat_no="+str(id))
                i= my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select roll_no from student where seat_no="+str(id))
                r= my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select seat_no from student where seat_no="+str(id))
                s= my_cursor.fetchone()
                s="+".join(s)

                
                my_cursor.execute("select `div` from student where seat_no="+str(id))
                div= my_cursor.fetchone()
                div="+".join(div)

                


                if confidence>77:
                    cv2.putText(img,f"Seat No.:{s}",(x,y-95),cv2. FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-70),cv2. FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-45),cv2. FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3)
                    cv2.putText(img,f"Div:{div}",(x,y-20),cv2. FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3)
                    self.mark_attendance(s,i,r,div)
                   
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2. FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3)
                coord=[x,y,w,h]

            return coord
           
            
        


        def recognize(img,clf,faceCascade):     
            coord=draw_boundray(img,faceCascade,1.1,10, (255,25,255),"Face",clf)
            return img

        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")   

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img= video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Video',img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows() 
        
        
#=====attendance========
    def mark_attendance(self,s,i,r,div):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist= f.read().splitlines()[1:]
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((s not in name_list) and (i not in name_list) and (r not in name_list) and (div not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{i},{r},{div},{dtString},{d1},Present")



if __name__ == "__main__":
    root = Tk()
    obj=Face_Recog_System(root)
    root.mainloop()