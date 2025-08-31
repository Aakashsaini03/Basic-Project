from tkinter import *
from tkinter import ttk


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1270x800+0+0") 
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1270,height=400)
        
        #===========================Data Frame Left======================
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=350)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Mamber Type:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblMember.grid(row=0,column=0,sticky=W)
        ComMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=18,state="readonly")
        ComMember["value"]=("Admin Staff","Student","Lecturer")
        ComMember.grid(row=0,column=1)
        
        lblPNR_NO=Label(DataFrameLeft,bg="powder blue",text="PNR_NO :",padx=2,font=("times new roman",12,"bold"))
        lblPNR_NO.grid(row=1,column=0,sticky=W)
        txtPNR_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtPNR_NO.grid(row=1,column=1)
        
        
        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID_NO :",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="Frist_Name :",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last_Name:",font=("times new roman",12,"bold"),padx=2,pady=5)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1 :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2 :",font=("times new roman",12,"bold"),padx=2,pady=7)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode :",font=("times new roman",12,"bold"),padx=2,pady=8)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtPostCode.grid(row=7,column=1)
        
        
        lblMobile_NO=Label(DataFrameLeft,bg="powder blue",text="Mobile_NO :",font=("times new roman",12,"bold"),padx=2,pady=9)
        lblMobile_NO.grid(row=0,column=2,sticky=W)
        txtMobile_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtMobile_NO.grid(row=0,column=3)
        
        lblBook_ID=Label(DataFrameLeft,bg="powder blue",text="Book_ID :",font=("times new roman",12,"bold"),padx=2)
        lblBook_ID.grid(row=1,column=2,sticky=W)
        txtBook_ID=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtBook_ID.grid(row=1,column=3)
        
        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="BookTitle :",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblBookTitle.grid(row=2,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtBookTitle.grid(row=2,column=3)
        
        lblAuther=Label(DataFrameLeft,bg="powder blue",text="Auther :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=3,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtAuther.grid(row=3,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed :",font=("times new roman",12,"bold"),padx=2,pady=8)
        lblDateBorrowed.grid(row=4,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtDateBorrowed.grid(row=4,column=3)
        
        lblDate_Due=Label(DataFrameLeft,bg="powder blue",text="Date_Due :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblDate_Due.grid(row=5,column=2,sticky=W)
        txtDate_Due=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtDate_Due.grid(row=5,column=3)
        
        lblLateReturnfine=Label(DataFrameLeft,bg="powder blue",text="Late_Return_fine :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblLateReturnfine.grid(row=6,column=2,sticky=W)
        txtLateReturnfine=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtLateReturnfine.grid(row=6,column=3)
        
        lblBookPrice=Label(DataFrameLeft,bg="powder blue",text="Book_Price :",font=("times new roman",12,"bold"),padx=2,pady=10)
        lblBookPrice.grid(row=7,column=2,sticky=W)
        txtBookPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=24)
        txtBookPrice.grid(row=7,column=3)
        
        #========================= DataFrame Right============================
        
        
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=710,y=5,width=500,height=350)
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        listBooks=['Head First book','Learn python the Hard Way','Python Programing','Secrete Rahshy','Pyhton CookBook','Into to Machine Learning','Machine techno','My python','Joss Ellif Guru',
                   'Elite Jungle Python','Jungli Python',
                   'Machine Python','Advance Python','Inton Python','Redchili Python','Ishq Python']
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.grid(row=0,column=0,padx=6)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
            
            
        
        
        
        # ====================Button Frame==================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1270,height=62)
        btnAddData=Button(Framebutton,text="Add Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        btnAddData=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        btnAddData=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        
        
         #=========================DEtails Frame========================
         
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1270,height=120)
        
        Table_frame=Frame(FrameDetails,bd=4,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=1,width=1230,height=100)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.libray_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1",
                                                           "address2","postid","mobile","bookid","booktitle","auther",
                                                           "dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),
                                       xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)
        self.libray_table.heading("membertype",text=" Member Type")
        self.libray_table.heading("prnno",text="PRN No.")
        self.libray_table.heading("title",text="Title")
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
        self.libray_table.column("title",width=100)
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
        
         
         
        
        

if __name__ == "__main__":
    root = Tk()  # 'Tk()', not 'TK()'
    obj = LibraryManagementSystem(root)
    root.mainloop()
