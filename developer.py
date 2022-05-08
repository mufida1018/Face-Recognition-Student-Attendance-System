from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image,ImageTk
from tkinter import messagebox

class Developer_code:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #bg img
        img=Image.open("/Users/mufida/Desktop/mini project_Images/developer.png")
        img=img.resize((1500,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=900)
    



if __name__ == "__main__":
    root = Tk()
    obj=Developer_code(root)
    root.mainloop()