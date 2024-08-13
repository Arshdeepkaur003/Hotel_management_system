from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
from report import report


class HotelManagementSystem:
     # call the constructor
     def __init__(self,root):
        # initialize the root
        self.root = root
        self.root.title("Hotal Management System")
        self.root.geometry("1550x800+0+0")
        
        # first image 
        img1 = Image.open("images\hotel1.png")
        img1 = img1.resize((1550, 160), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labeling = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labeling.place(x=0,y=0,width=1550,height=160)
        
        #logo
        img2 = Image.open("images\logo.png")
        img2 = img2.resize((230, 160), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labeling = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labeling.place(x=0,y=0,width=230 ,height=160)

        # title
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="#CD853F",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=160,width=1550,height=50)

        # main frame
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=210,width=1550,height=620)

        # menu
        lbl_menu = Label(
         main_frame,text="MENU",font=("Helvetica", 20, "bold"),
         bg="black",  fg="#CD853F", bd=6,
         relief=RIDGE,padx=10,  pady=10)
        lbl_menu.place(x=0, y=0, width=230, height=40)
        
        #btn frame
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn = Button(btn_frame,text="CUSTOMER",command=self.cust_details, width=22,font=("times new roman",14,"bold"),bg="black",fg="#CD853F",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,text="ROOM",command=self.roombooking, width=22,font=("times new roman",14,"bold"),bg="black",fg="#CD853F",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame,text="DETAILS",command=self.DetailsRoom,width=22,font=("times new roman",14,"bold"),bg="black",fg="#CD853F",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn = Button(btn_frame,text="REPORT",command=self.report,width=22,font=("times new roman",14,"bold"),bg="black",fg="#CD853F",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="#CD853F",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #RIGHT SIDE IMAGE
        img3 = Image.open("images\slide3.png")
        img3 = img3.resize((1300,550), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        labelingimg1 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        labelingimg1.place(x=225,y=0,width=1300 ,height=550)

         #RIGHT SIDE IMAGE
        img4 = Image.open("images\image5.png")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)
        
        #label name
        lbl_name = Label(main_frame, text="Created by Arsh", font=(
            "Times new roman", 18, "bold"), bg="black", fg="#CD853F", bd=4, relief=RIDGE)
        lbl_name.place(x=0, y=420, width=230, height=65)

     def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)
   
     def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)


     def DetailsRoom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

     def report(self):
        self.new_window = Toplevel(self.root)
        self.app = report(self.new_window)
    

 
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()   
 
