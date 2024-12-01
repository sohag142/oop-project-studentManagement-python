from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+200+250")
        self.root.config(bg="white")
        self.root.focus_force()

        #------------- title --------------
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #----------- variables ------------
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_NID=StringVar()
        self.var_a_date=StringVar()
        self.var_country=StringVar()
        self.var_city=StringVar()
        self.var_zip=StringVar()

        #------------- widgets -----------------
        #--------- column 1 ---------------
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_country=Label(self.root,text="Country",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        txt_country=Entry(self.root,textvariable=self.var_country,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=220,width=150)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=380,y=220,width=100)
        lbl_zip=Label(self.root,text="Zip",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)
        txt_zip=Entry(self.root,textvariable=self.var_zip,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=560,y=220,width=120)

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=260)

        #------------ entry fields -------------
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)

        #--------- column 2 ---------------
        lbl_dob=Label(self.root,text="D.O.B.",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)
        lbl_NID=Label(self.root,text="NID",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        #------------ entry fields -------------
        #self.course_list=[""]
        #self.fetch_course()
        # function call to update the list
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=140,width=200)
        txt_NID=Entry(self.root,textvariable=self.var_NID,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=180,width=200)
        #self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        #self.txt_course.place(x=480,y=180,width=200)
        #self.txt_course.set("Select")

        #------------ TexT Address -----------------
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,width=540,height=100)

        #----------------- buttons ----------------
        self.btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2")
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2")
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2")
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #-------------- search panel -----------------
        self.var_search=StringVar()

        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)

        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1070,y=60,width=120,height=28)

        #---------------- content -------------------
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.StudentTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","NID","country","city","zip","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)
        self.StudentTable.heading("roll",text="Roll No.")
        self.StudentTable.heading("name",text="Name")
        self.StudentTable.heading("email",text="Email")
        self.StudentTable.heading("gender",text="Gender")
        self.StudentTable.heading("dob",text="D.O.B.")
        self.StudentTable.heading("contact",text="Contact")
        self.StudentTable.heading("admission",text="Admission")
        self.StudentTable.heading("NID",text="NID")
        self.StudentTable.heading("country",text="Country")
        self.StudentTable.heading("city",text="City")
        self.StudentTable.heading("zip",text="Zip")
        self.StudentTable.heading("address",text="Address")
        self.StudentTable["show"]='headings'
        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("email",width=100)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("admission",width=100)
        self.StudentTable.column("NID",width=100)
        self.StudentTable.column("country",width=100)
        self.StudentTable.column("city",width=100)
        self.StudentTable.column("zip",width=100)
        self.StudentTable.column("address",width=200)
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#-----------------------------------------------------------------------------------------------------------

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll Number akready present",parent=self.root)
                else:
                    cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,NID,country,city,zip,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_NID.get(),
                        self.var_country.get(),
                        self.var_city.get(),
                        self.var_zip.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                self.StudentTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.StudentTable.focus()
        content=self.StudentTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_NID.set(row[7])
        self.var_country.set(row[8])
        self.var_city.set(row[9])
        self.var_zip.set(row[10])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,NID=?,country=?,city=?,zip=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_NID.get(),
                        self.var_country.get(),
                        self.var_city.get(),
                        self.var_zip.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_NID.set("")
        self.var_country.set("")
        self.var_city.set("")
        self.var_zip.set("")
        self.var_search.set("")
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.root)
            else:
                # Check if the student exists in the database
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                student_row = cur.fetchone()
                if student_row is None:
                    messagebox.showerror("Error", "Please select a valid student from the list", parent=self.root)
                else:
                    # Confirm deletion
                    op = messagebox.askyesno("Confirm", "Do you really want to delete the student and their results?",
                                             parent=self.root)
                    if op:
                        # Delete student from the 'student' table
                        cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
                        # Delete related results from the 'result' table
                        cur.execute("DELETE FROM result WHERE roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student and their results deleted successfully",
                                            parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally: 
            con.close()

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()