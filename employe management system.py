from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image
import mysql.connector



class employe():
    def __init__(self,root):
        self.root=root
        self.root.config(bg="white")
        self.root.geometry("1350x680+0+0")
        self.root.title("Employe managment system")

      #=================veriables====================
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_deginition=StringVar()
        self.var_mail=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_Id_Type=StringVar()
        self.var_Id_prof_comb=StringVar()
        self.var_Id_prof_entry=StringVar()
        self.var_gndr=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        self.var_srch_comb=StringVar()
        self.var_srch_entry=StringVar()
 

        #back main frame
        lbl_frame1=LabelFrame(self.root,width=1320,height=670,bg="white")
        lbl_frame1.place(x=15,y=0)

        #main Title
        lbl=Label(lbl_frame1,text="EMPLOYE MANAGMENT SYSTEM",font="arial 25 bold",bg="white",fg="dark blue")
        lbl.place(x=440,y=10)


        #employe info frame
        lbl_frame=LabelFrame(self.root,text="Employe Information",fg="red",font="arial 10 bold",width=1310,height=230,bg="white")
        lbl_frame.place(x=19,y=160)

        # #student image

        img1=Image.open(r"E:\python projects\Employe managment system\data\imm1.jpg")
        img1=img1.resize((300,200),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img1)

        lbl_1= Label(lbl_frame,image=self.photo)
        lbl_1.place(x=1000,y=0,height=200,width=300)


        # #employe managment top pics 1

        img2=Image.open(r"E:\python projects\Employe managment system\data\4380.jpg")
        img2=img2.resize((300,130),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img2)

        self.img2 = Label(lbl_frame1,image=self.photo1).place(x=100,y=50,height=130,width=300)

        # #employe managment top pics 2

        img3=Image.open(r"E:\python projects\Employe managment system\data\5236.jpg")
        img3=img3.resize((300,120),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img3)

        self.img2 = Label(lbl_frame1,image=self.photo2).place(x=550,y=50,height=120,width=300)

        # #employe managment top pics 3

        img4=Image.open(r"E:\python projects\Employe managment system\data\imgg.jpg")
        img4=img4.resize((300,130),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img4)

        self.img4 = Label(lbl_frame1,image=self.photo3).place(x=1000,y=50,height=130,width=300)



         #employe info frame table
        #lbl_frame=LabelFrame(self.root,text="Employe Information Table",fg="red",font="arial 10 bold",width=1310,height=270,bg="white")
        #lbl_frame.place(x=19,y=390)

        #employe search info
        lbl_frame=LabelFrame(self.root,text="Employe Search Information",fg="red",font="arial 8 bold",width=1310,height=70,bg="white")
        lbl_frame.place(x=19,y=390)

        #employe data information  department
        lbl_info=Label(self.root,text="Department:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=180)

        #employe data information designition
        lbl_info=Label(self.root,text="Designition:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=220)

        #employe data information Address
        lbl_info=Label(self.root,text="Address:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=260)

        #employe data information DOB
        lbl_info=Label(self.root,text="D-O-B:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=300)

        #employe data information name
        lbl_info=Label(self.root,text="Name:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=180)

        #employe data information mail
        lbl_info=Label(self.root,text="E.mail:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=220)

        #employe data information marid status
        lbl_info=Label(self.root,text="Married Status:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=260)

        #employe data information Date of joining
        lbl_info=Label(self.root,text="D-O-J:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=300)

        #employe data information gender
        lbl_info=Label(self.root,text="Gender:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=340)

        #employe data information phone
        lbl_info=Label(self.root,text="Phone No:",font="arial 13 bold",bg="white")
        lbl_info.place(x=695,y=180)

        #employe data information country
        lbl_info=Label(self.root,text="Country:",font="arial 13 bold",bg="white")
        lbl_info.place(x=695,y=220)

        #employe data information salary ctc
        lbl_info=Label(self.root,text="Salary (CTC):",font="arial 13 bold",bg="white")
        lbl_info.place(x=695,y=260)


        #employe info Entry box of designition
        ent=Entry(self.root,textvariable=self.var_deginition,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=220)

         #employe info Entry box of address
        ent=Entry(self.root,textvariable=self.var_address,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=260)

        
         #employe info Entry box of date of birth
        ent=Entry(self.root,textvariable=self.var_dob,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=300)

        #employe info Entry box of id proof
        ent=Entry(self.root,textvariable=self.var_Id_prof_entry,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=340)

        #employe info Entry box of name
        ent=Entry(self.root,textvariable=self.var_name,width=20,font=20,bg="#f0f8ff")
        ent.place(x=500,y=180)

        #employe info Entry box of mail
        ent=Entry(self.root,textvariable=self.var_mail,width=20,font=20,bg="#f0f8ff")
        ent.place(x=500,y=220)

        #employe info Entry box of Date of joining
        ent=Entry(self.root,textvariable=self.var_doj,width=20,font=20,bg="#f0f8ff")
        ent.place(x=500,y=300)

        #employe info Entry box of  phone
        ent=Entry(self.root,textvariable=self.var_phone,width=20,font=20,bg="#f0f8ff")
        ent.place(x=810,y=180)

        #employe info Entry box of country
        ent=Entry(self.root,textvariable=self.var_country,width=20,font=20,bg="#f0f8ff")
        ent.place(x=810,y=220)

        #employe info Entry box of salary ctc
        ent=Entry(self.root,textvariable=self.var_salary,width=20,font=20,bg="#f0f8ff")
        ent.place(x=810,y=260)

        #employe info combo_box of department
        box=ttk.Combobox(self.root,textvariable=self.var_dep,width=27,values=["Select Department","Abid Motors","Abid Filling Station","Abasia Town"],state="readonly")
        box.place(x=160,y=180)
        box.current(0)

         #employe info combo_box of ID proff
        box=ttk.Combobox(self.root,textvariable=self.var_Id_prof_comb,width=15,values=["Select ID Proff","CNIC","pasport","Drivig licince"],state="readonly")
        box.place(x=30,y=340)
        box.current(0)

         #employe info combo_box of marid status
        box=ttk.Combobox(self.root,textvariable=self.var_married,width=27,values=["Select Option","Married","Un-Married"],state="readonly")
        box.place(x=500,y=260)
        box.current(0)

         #employe info combo_box of gender
        box=ttk.Combobox(self.root,textvariable=self.var_gndr,width=27,values=["Select Option","Male","Female"],state="readonly")
        box.place(x=500,y=340)
        box.current(0)

        #employe info button of save

        btn=Button(self.root,command=self.add_data,text="save",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=720,y=300,width=130)

         #employe info button of update

        btn=Button(self.root,command=self.up_date,text="Update",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=860,y=300,width=130)

        #employe info button of delete

        btn=Button(self.root,command=self.dlt,text="Delete",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=720,y=345,width=130)

        #employe info button of reset

        btn=Button(self.root,command=self.rst,text="Reset",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=860,y=345,width=130)

        #employe table frame


        #employe search lable

        Label(self.root,text="Search By:",font="arial 14 bold",fg="white",bg="red").place(x=50,y=420)

         #employe search info combo_box
        box=ttk.Combobox(self.root,textvariable=self.var_srch_comb,width=27,font="arial 10 bold",values=["Select Option ","Phone","Name"],state="readonly")
        box.place(x=200,y=420)
        box.current(0)

        #employe info table entry of search

        Entry(self.root,textvariable=self.var_srch_entry,width=25,font=20,bg="#f0f8ff").place(x=450,y=420)

         #employe info table search button of "search" or "show all"

         #search button
        btn=Button(self.root,command=self.search_data,text="Search",font="arial 13 bold",fg="white",bg="dark blue")
        btn.place(x=720,y=415,width=130)

          #show all button
        btn=Button(self.root,command=self.fetch_data,text="Show All",font="arial 13 bold",fg="white",bg="dark blue")
        btn.place(x=860,y=415,width=130)

        #================  Employe data table ================

           #employe save frame table
        table_frame=LabelFrame(self.root,bg="darkgreen",font="arial 10 bold")
        table_frame.place(x=20,y=465,width=1310,height=200)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employe_table=ttk.Treeview(table_frame,columns=("dep","nme","degi","mail","adrs","marid","dob","doj","id_prof_comb","idprof","gndr","phn","cntry","slry",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employe_table.xview)
        scroll_y.config(command=self.employe_table.yview)

        self.employe_table.heading('dep',text="Department")
        self.employe_table.heading('nme',text="Name")
        self.employe_table.heading('degi',text="Deginition")
        self.employe_table.heading('mail',text="E.mail")
        self.employe_table.heading('adrs',text="Address")
        self.employe_table.heading('marid',text="Married")
        self.employe_table.heading('dob',text="D-O-B")
        self.employe_table.heading('doj',text="D-O-J")
        self.employe_table.heading('id_prof_comb',text="ID-proff")
        self.employe_table.heading('idprof',text="ID-No")
        self.employe_table.heading('gndr',text="Gender")
        self.employe_table.heading('phn',text="Phone No")
        self.employe_table.heading('cntry',text="Country")
        self.employe_table.heading('slry',text="Salary")

        self.employe_table['show']='headings'
        self.employe_table.column("dep",width=100)
        self.employe_table.column("nme",width=100)
        self.employe_table.column("degi",width=100)
        self.employe_table.column("mail",width=100)
        self.employe_table.column("adrs",width=100)
        self.employe_table.column("marid",width=100)
        self.employe_table.column("dob",width=100)
        self.employe_table.column("doj",width=100)
        self.employe_table.column("id_prof_comb",width=100)
        self.employe_table.column("idprof",width=100)
        self.employe_table.column("gndr",width=100)
        self.employe_table.column("phn",width=100)
        self.employe_table.column("cntry",width=100)
        self.employe_table.column("slry",width=100)
        


        self.employe_table.pack(fill=BOTH,expand=1)
        self.employe_table.bind('<ButtonRelease>', self.get_query)

        self.fetch_data()     #calling for fetch data

##############################################################################################

#======================================Add Data Query=====================================

    def add_data(self):
      if(
        self.var_dep.get()=="Select Department"
        or self.var_name.get()==""
        or self.var_deginition.get()=="" 
        or self.var_mail.get()=="" 
        or self.var_address.get()=="" 
        or self.var_married.get()=="Select Option" 
        or self.var_dob.get()=="" 
        or self.var_doj.get()=="" 
        or self.var_Id_prof_comb.get()=="Select ID Proff"
        or self.var_Id_prof_entry.get()==""
        or self.var_gndr.get()=="Select Option" 
        or self.var_phone.get()=="" 
        or self.var_country.get()=="" 
        or self.var_salary.get()==""
      ):
        messagebox.showerror("Error","All Fields are Required")
      else:

        try:

          con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="employe")
          cur=con.cursor()

          query = ("INSERT INTO new_table SET "
                   "department=%s, "
                   "name=%s, "
                   "deginition=%s, "
                   "Email=%s, "
                   "address=%s, "
                   "married=%s, "
                   "DOB=%s, "
                   "DOJ=%s,"
                   "ID_Type=%s, "
                   "ID_No=%s, "
                   "gender=%s, "
                   "phone=%s, "
                   "country=%s, "
                   "salary=%s")
          data = (
                self.var_dep.get(),
                self.var_name.get(),
                self.var_deginition.get(),
                self.var_mail.get(),
                self.var_address.get(),
                self.var_married.get(),
                self.var_dob.get(),
                self.var_doj.get(),
                self.var_Id_prof_comb.get(),
                self.var_Id_prof_entry.get(),
                self.var_gndr.get(),
                self.var_phone.get(),
                self.var_country.get(),
                self.var_salary.get(),
          )
          cur.execute(query, data)
          con.commit()
          self.fetch_data()
          con.close()

          messagebox.showinfo("Success","Employe details Add Successfilly")
        except Exception as e:
          messagebox.showerror("Error",f"Error:{str(e)}")

######################################Fetch Data########################################
    def fetch_data(self):
        try:
            con = mysql.connector.connect(host="localhost", username="root", password="h@Roon#123Abc", database="employe")
            cur = con.cursor()
            cur.execute("SELECT * FROM new_table")
            data = cur.fetchall()
            self.employe_table.delete(*self.employe_table.get_children())

            if len(data) != 0:
                for i in data:
                    self.employe_table.insert("", END, values=i)

            con.close()
        except Exception as e:
          messagebox.showerror("Error",f"Error:{str(e)}")

##############################Get Function################################

    def get_query(self,event=""):
      cursor_focus=self.employe_table.focus()
      content=self.employe_table.item(cursor_focus)
      data1=content["values"]
      self.var_dep.set(data1[0])
      self.var_name.set(data1[1])
      self.var_deginition.set(data1[2])
      self.var_mail.set(data1[3])
      self.var_address.set(data1[4])
      self.var_married.set(data1[5])
      self.var_dob.set(data1[6])
      self.var_doj.set(data1[7])
      self.var_Id_prof_comb.set(data1[8])
      self.var_Id_prof_entry.set(data1[9])
      self.var_gndr.set(data1[10])
      self.var_phone.set(data1[11])
      self.var_country.set(data1[12])
      self.var_salary.set(data1[13])      
          
#==================================update function==============================          
          
    def up_date(self):
      if(
        self.var_dep.get()=="Select Department"
        or self.var_name.get()==""
        or self.var_deginition.get()=="" 
        or self.var_mail.get()=="" 
        or self.var_address.get()=="" 
        or self.var_married.get()=="Select Option" 
        or self.var_dob.get()=="" 
        or self.var_doj.get()=="" 
        or self.var_Id_prof_comb.get()=="Select ID Proff"
        or self.var_Id_prof_entry.get()==""
        or self.var_gndr.get()=="Select Option" 
        or self.var_phone.get()=="" 
        or self.var_country.get()=="" 
        or self.var_salary.get()==""
      ):
        messagebox.showerror("Error","All Fields are required")
      else:
        try:
          updt=messagebox.askyesno("update","Do you want to update!!!")
          if updt>0:
            con = mysql.connector.connect(host="localhost", username="root", password="h@Roon#123Abc", database="employe")
            cur = con.cursor()

            query= (
                    "UPDATE new_table SET "
                    "department=%s, "
                    "name=%s, "
                    "deginition=%s, "
                    "Email=%s, "
                    "address=%s, "
                    "married=%s, "
                    "DOB=%s, "
                    "DOJ=%s,"
                    "ID_Type=%s, "
                    "gender=%s, "
                    "phone=%s, "
                    "country=%s, "
                    "salary=%s"
                    "WHERE ID_No=%s"

                               )

            data= (
                  self.var_dep.get(),
                  self.var_name.get(),
                  self.var_deginition.get(),
                  self.var_mail.get(),
                  self.var_address.get(),
                  self.var_married.get(),
                  self.var_dob.get(),
                  self.var_doj.get(),
                  self.var_Id_prof_comb.get(),
                  self.var_gndr.get(),
                  self.var_phone.get(),
                  self.var_country.get(),
                  self.var_salary.get(),
                  self.var_Id_prof_entry.get()

            )

            cur.execute(query, data)
            con.commit()
            self.fetch_data()
            con.close()

            messagebox.showinfo("Success", "Employe details successfully updated")

          else:
                          # If the user clicks 'No', do nothing
            return
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)





# ==================================Delete Function==============================

    def dlt(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_deginition.get() == ""
            or self.var_mail.get() == ""
            or self.var_address.get() == ""
            or self.var_married.get() == "Select Option"
            or self.var_dob.get() == ""
            or self.var_doj.get() == ""
            or self.var_Id_prof_comb.get() == "Select ID Proff"
            or self.var_Id_prof_entry.get() == ""
            or self.var_gndr.get() == "Select Option"
            or self.var_phone.get() == ""
            or self.var_country.get() == ""
            or self.var_salary.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                dlt1 = messagebox.askyesno("Result", "Do you want to delete")
                if dlt1:
                    con = mysql.connector.connect(
                        host="localhost", username="root", password="h@Roon#123Abc", database="employe"
                    )
                    cur = con.cursor()

                    sql = "delete from new_table where ID_No=%s "
                    val = (self.var_Id_prof_entry.get(),)
                    cur.execute(sql, val)
                    con.commit()
                    con.close()
                    self.fetch_data()

                    messagebox.showinfo("Info", "Data Deleted Successfully")

                else:
                    if not dlt1:
                        return

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")


#==================================reset function===============================

    def rst(self):
      if(
        self.var_dep.get()=="Select Department"
        or self.var_name.get()==""
        or self.var_deginition.get()=="" 
        or self.var_mail.get()=="" 
        or self.var_address.get()=="" 
        or self.var_married.get()=="Select Option" 
        or self.var_dob.get()=="" 
        or self.var_doj.get()=="" 
        or self.var_Id_prof_comb.get()=="Select ID Proff"
        or self.var_Id_prof_entry.get()==""
        or self.var_gndr.get()=="Select Option" 
        or self.var_phone.get()=="" 
        or self.var_country.get()=="" 
        or self.var_salary.get()==""
      ):   
        messagebox.showerror("Error","All fields are required")
      
      self.var_dep.set("Select Department")
      self.var_name.set("")
      self.var_deginition.set("") 
      self.var_mail.set("")
      self.var_address.set("") 
      self.var_married.set("Select Option") 
      self.var_dob.set("") 
      self.var_doj.set("") 
      self.var_Id_prof_comb.set("Select ID Proff")
      self.var_Id_prof_entry.set("")
      self.var_gndr.set("Select Option") 
      self.var_phone.set("") 
      self.var_country.set("") 
      self.var_salary.set("")


#===============================search query==========================
    def search_data(self):
        if self.var_srch_comb.get() == "Select Option" or self.var_srch_entry.get() == "":
            messagebox.showerror("Error", "Select valid search criteria and enter search value.")
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost", username="root", password="h@Roon#123Abc", database="employe"
                )
                cur = con.cursor()

                # Modify the SQL query based on the selected search criteria
                if self.var_srch_comb.get() == "Name":
                    query = "SELECT * FROM new_table WHERE name LIKE %s"
                elif self.var_srch_comb.get() == "Phone":
                    query = "SELECT * FROM new_table WHERE phone LIKE %s"

                search_value = f"%{self.var_srch_entry.get()}%"
                cur.execute(query, (search_value,))
                data = cur.fetchall()

                self.employe_table.delete(*self.employe_table.get_children())

                if len(data) != 0:
                    for i in data:
                        self.employe_table.insert("", END, values=i)

                con.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")







if __name__=="__main__":
    root=Tk()
    obj=employe(root)
    root.mainloop()
