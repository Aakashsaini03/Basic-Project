from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1270x800+0+0") 
        #=======================varible========================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()       
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.datesonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
       
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1270,height=400)
        
        #===========================Data Frame Left======================
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=350)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Mamber Type:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblMember.grid(row=0,column=0,sticky=W)
        ComMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width=18,state="readonly")
        ComMember["value"]=("Admin Staff","Student","Lecturer")
        ComMember.grid(row=0,column=1)
        
        lblPNR_NO=Label(DataFrameLeft,bg="powder blue",text="PNR_NO :",padx=2,font=("times new roman",12,"bold"))
        lblPNR_NO.grid(row=1,column=0,sticky=W)
        txtPNR_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=24)
        txtPNR_NO.grid(row=1,column=1)
        
        
        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID_NO :",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.id_var,width=24)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="Frist_Name :",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.firstname_var,width=24)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last_Name:",font=("times new roman",12,"bold"),padx=2,pady=5)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.lastname_var,width=24)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1 :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address1_var,width=24)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2 :",font=("times new roman",12,"bold"),padx=2,pady=7)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address2_var,width=24)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode :",font=("times new roman",12,"bold"),padx=2,pady=8)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.postcode_var,width=24)
        txtPostCode.grid(row=7,column=1)
        
        
        lblMobile_NO=Label(DataFrameLeft,bg="powder blue",text="Mobile_NO :",font=("times new roman",12,"bold"),padx=2,pady=9)
        lblMobile_NO.grid(row=8,column=0,sticky=W)
        txtMobile_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.mobile_var,width=24)
        txtMobile_NO.grid(row=8,column=1)
        
        lblBook_ID=Label(DataFrameLeft,bg="powder blue",text="Book_ID :",font=("times new roman",12,"bold"),padx=2)
        lblBook_ID.grid(row=0,column=2,sticky=W)
        txtBook_ID=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.bookid_var,width=24)
        txtBook_ID.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="BookTitle :",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.booktitle_var,width=24)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Auther :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.author_var,width=24)
        txtAuthor.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed :",font=("times new roman",12,"bold"),padx=2,pady=8)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var,width=24)
        txtDateBorrowed.grid(row=3,column=3)
        
        lblDate_Due=Label(DataFrameLeft,bg="powder blue",text="Date_Due :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblDate_Due.grid(row=4,column=2,sticky=W)
        txtDate_Due=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datedue_var,width=24)
        txtDate_Due.grid(row=4,column=3)
        
        lblDate_onbook=Label(DataFrameLeft,bg="powder blue",text="Date_on_book :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblDate_onbook.grid(row=5,column=2,sticky=W)
        txtDate_onbook=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datesonbook_var,width=24)
        txtDate_onbook.grid(row=5,column=3)
        
        lblLateReturnfine=Label(DataFrameLeft,bg="powder blue",text="Late_Return_fine :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblLateReturnfine.grid(row=6,column=2,sticky=W)
        txtLateReturnfine=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.lateratefine_var,width=24)
        txtLateReturnfine.grid(row=6,column=3)
        
        lbldate_over_due=Label(DataFrameLeft,bg="powder blue",text="date_over_due :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lbldate_over_due.grid(row=7,column=2,sticky=W)
        txtdate_over_due=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=24)
        txtdate_over_due.grid(row=7,column=3)
        
        lblBookPrice=Label(DataFrameLeft,bg="powder blue",text="Book_Price :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblBookPrice.grid(row=8,column=2,sticky=W)
        txtBookPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.finalprice_var,width=24)
        txtBookPrice.grid(row=8,column=3)
        
        #========================= DataFrame Right============================
        
        
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=710,y=5,width=500,height=350)
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        listBooks=['Head Firt book','Learn python the Hard Way','Python Programing','Secrete Rahshy','Pyhton CookBook','Into to Machine Learning','Machine techno','My python','Joss Ellif Guru',
                   'Elite Jungle Python','Jungli Python',
                   'Machine Python','Advance Python','Inton Python','Redchili Python','Ishq Python']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Head Firt book"):
                self.bookid_var.set("BKID001")
                self.booktitle_var.set("Python_manual")
                self.author_var.set("paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.datesonbook_var.set(15)
                self.lateratefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 780")
                
                
                
                
            
           
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=6)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
            
            
        
        
        
        # ====================Button Frame==================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1270,height=62)
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnshow=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnshow.grid(row=0,column=1)
        btnupdate=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnupdate.grid(row=0,column=2)
        btndelete=Button(Framebutton,command=self.delete_data,text="Delete",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btndelete.grid(row=0,column=3)
        btnreset=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnreset.grid(row=0,column=4)
        btnexit=Button(Framebutton,command=self.IExit,text="Exit",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnexit.grid(row=0,column=5)
        
        
         #=========================DEtails Frame========================
         
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1270,height=120)
        
        Table_frame=Frame(FrameDetails,bd=4,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=1,width=1230,height=100)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.libray_table=ttk.Treeview(Table_frame,column=("membertype","prnno","ID","firstname","lastname","address1",
                                                           "address2","postid","mobile","bookid","booktitle","auther",
                                                           "dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),
                                       xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
            
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)
       
        self.libray_table.heading("membertype",text=" Member Type")
        self.libray_table.heading("prnno",text="PRN No.")
        self.libray_table.heading("ID",text="ID")
        self.libray_table.heading("firstname",text="First Name")
        self.libray_table.heading("lastname",text="Last Name")
        self.libray_table.heading("address1",text="Address1")
        self.libray_table.heading("address2",text="Address2")
        self.libray_table.heading("postid",text="Post ID")
        self.libray_table.heading("mobile",text="Mobile Number")
        self.libray_table.heading("bookid",text="Book ID")
        self.libray_table.heading("booktitle",text="Book Title")
        self.libray_table.heading("auther",text="Auther")
        self.libray_table.heading("dateborrowed",text="Date Of Borrowed")
        self.libray_table.heading("datedue",text="date Due")
        self.libray_table.heading("days",text="DaysOnBook")
        self.libray_table.heading("latereturnfine",text="LateReturnFine")
        self.libray_table.heading("dateoverdue",text="DateOverDue")
        self.libray_table.heading("finalprice",text="Final Price")
        
        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH,expand=1)
        self.libray_table.column("membertype",width=100)
        self.libray_table.column("prnno",width=100)
        self.libray_table.column("ID",width=100)
        self.libray_table.column("firstname",width=100)
        self.libray_table.column("lastname",width=100)
        self.libray_table.column("address1",width=100)
        self.libray_table.column("address2",width=100)
        self.libray_table.column("postid",width=100)
        self.libray_table.column("mobile",width=100)
        self.libray_table.column("bookid",width=100)
        self.libray_table.column("booktitle",width=100)
        self.libray_table.column("auther",width=100)
        self.libray_table.column("dateborrowed",width=100)
        self.libray_table.column("datedue",width=100)
        self.libray_table.column("days",width=100)
        self.libray_table.column("latereturnfine",width=100)
        self.libray_table.column("dateoverdue",width=100)
        self.libray_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.libray_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
    def add_data(self):
        try:
            conn= mysql.connector.connect(host="localhost",username="root",password="Aakash@123",database="library_db")   
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO members VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),
                                                                                                             self.prn_var.get(),
                                                                                                             self.id_var.get(),
                                                                                                             self.firstname_var.get(),
                                                                                                             self.lastname_var.get(),
                                                                                                             self.address1_var.get(),
                                                                                                             self.address2_var.get(),
                                                                                                             self.postcode_var.get(),
                                                                                                             self.mobile_var.get(),
                                                                                                             self.bookid_var.get(),
                                                                                                             self.booktitle_var.get(),
                                                                                                             self.author_var.get(),
                                                                                                             self.dateborrowed_var.get(),
                                                                                                             self.datedue_var.get(),
                                                                                                             self.datesonbook_var.get(),
                                                                                                             self.lateratefine_var.get(),
                                                                                                             self.dateoverdue_var.get(),
                                                                                                             self.finalprice_var.get()
                                                                                                           ))
            conn.commit()
            self.fetch_data()
            conn.close()
        
            messagebox.showinfo("Success","Member has been inserted successfully")
        except Exception as e:
            messagebox.showerror("Error",f"Something went wrong:\n{e}")  
            
    def update(self):
         try:
             conn= mysql.connector.connect(host="localhost",username="root",password="Aakash@123",database="library_db")   
             my_cursor=conn.cursor() 
             my_cursor.execute("update members set member_type=%s,id_no=%s,first_name=%s,last_name=%s,address1=%s,address2=%s,postcode=%s,mobile=%s,book_id=%s,book_title=%s,author=%s,date_borrowed=%s,date_due=%s,days_on_book=%s,late_return_fine=%s,date_overdue=%s,final_price=%s where prn_no=%s",(
                                               self.member_var.get(),
                                               self.id_var.get(),
                                               self.firstname_var.get(),
                                               self.lastname_var.get(),
                                               self.address1_var.get(),
                                               self.address2_var.get(),
                                               self.postcode_var.get(),
                                               self.mobile_var.get(),
                                               self.bookid_var.get(),
                                               self.booktitle_var.get(),
                                               self.author_var.get(),
                                               self.dateborrowed_var.get(),
                                               self.datedue_var.get(),
                                               self.datesonbook_var.get(),
                                               self.lateratefine_var.get(),
                                               self.dateoverdue_var.get(),
                                               self.finalprice_var.get(),
                                               self.prn_var.get()
             
                                         ))
             conn.commit()
             self.fetch_data()
             self.reset()
             conn.close()
             
             messagebox.showinfo("Success","Member has been Updated")
           
         except Exception as e:
          messagebox.showerror("Error",f"Something went wrong:\n{e}")     
             
             
             
         
         
         
         
        
               
    
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aakash@123",database="library_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from members")
        row=my_cursor.fetchall()
        
        if len(row)!=0:
            self.libray_table.delete(*self.libray_table.get_children())
            for i in row:
                self.libray_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
    def get_cursor(self,event=""):
        cursor_row=self.libray_table.focus()
        content=self.libray_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.datesonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FristName:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"datedue:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Datesonbook:\t\t"+self.datesonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateRateFine:\t\t"+self.lateratefine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+self.finalprice_var.get()+"\n")
        
    def reset(self):
        self.member_var.set(""), 
        self.prn_var.set(""), 
        self.id_var.set(""), 
        self.firstname_var.set(""), 
        self.lastname_var.set(""), 
        self.address1_var.set(""), 
        self.address2_var.set(""), 
        self.postcode_var.set(""), 
        self.mobile_var.set(""), 
        self.bookid_var.set(""), 
        self.booktitle_var.set(""), 
        self.author_var.set(""), 
        self.dateborrowed_var.set(""), 
        self.datedue_var.set(""),
        self.datesonbook_var.set(""), 
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""), 
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END) 
        
        
    def IExit(self):
        IExit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
        if IExit>0:
            self.root.destroy()
            return
      
    def delete_data(self):
       try:
            if self.prn_var.get()=="" or self.id_var.get()=="":
             messagebox.showinfo("Error","First Select the member")
            else:
             conn= mysql.connector.connect(host="localhost",username="root",password="Aakash@123",database="library_db")   
             my_cursor=conn.cursor()
             query="delete from members where prn_no=%s"
             value=(self.prn_var.get(),)
             my_cursor.execute(query,value)
            
             conn.commit()
             self.fetch_data()
             self.reset()
             conn.close()
            
            messagebox.showinfo("Success","Member has been delete")
            
       except Exception as e:
        messagebox.showerror("Error",f"Something went wrong:\n{e}")       
                
              
             
        
            
        
                          
                         
                                                                                                             
    
    
                
    
                                                                                                        
        
         
         
        
        

if __name__ == "__main__":
    root = Tk()  # 'Tk()', not 'TK()'
    obj = LibraryManagementSystem(root)
    root.mainloop()
