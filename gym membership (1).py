from tkinter import *
from tkinter.ttk import Combobox, Scrollbar
import tkinter.ttk as ttk
import  datetime
import mysql.connector as mysql


class GymManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("GYM MANAGEMENT PROJECT")
        self.root.geometry("1300x660+0+0")



        self.memberid_var=StringVar()
        self.name_var=StringVar()
        self.Phnno_var=StringVar()
        self.Gender_var=StringVar()
        self.Address1_var=StringVar()
        self.Address2_var=StringVar()
        self.Height_var=StringVar()
        self.Weight_var=StringVar()
        self.Datejoining=StringVar()
        self.Dateexpired=StringVar()
        self.Identification=StringVar()
        self.BloodG=StringVar()
        self.Fees=StringVar()
        self.Paid=StringVar()
        self.Balance=StringVar()
        self.Referral=StringVar()


        def savedata():
            conn = mysql.connect(user='root', password='root', host='localhost', database="gymdb")
            cur = conn.cursor()

            cur.execute("insert into gym_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.memberid_var.get(), self.name_var.get(), self.Phnno_var.get(),
                         self.Gender_var.get(), self.Address1_var.get(),
                         self.Address2_var.get(), self.Height_var.get(),
                         self.Weight_var.get(), self.Datejoining.set(datetime.datetime.today()), self.Dateexpired.set(datetime.datetime.today()+datetime.timedelta(days=90))
                         , self.Identification.get(), self.BloodG.get(),
                         self.Fees.get(), self.Paid.get(),
                         self.Balance.get(), self.Referral.get()))

            print("Data inserted...")
            conn.commit()
            fetch_data()
            conn.close()
        def showData():
            self.txtBox.delete("1.0", 'end')
            self.txtBox.insert(END, "MemberId\t\t" + self.memberid_var.get() + "\n")
            self.txtBox.insert(END, "Name\t\t" + self.name_var.get() + "\n")
            self.txtBox.insert(END, "Phnno\t\t" + self.Phnno_var.get() + "\n")
            self.txtBox.insert(END, "Gender\t\t" + self.Gender_var.get() + "\n")
            self.txtBox.insert(END, "Address1\t\t" + self.Address1_var.get() + "\n")
            self.txtBox.insert(END, "Address2\t\t" + self.Address2_var.get() + "\n")
            self.txtBox.insert(END, "Height\t\t" + self.Height_var.get() + "\n")
            self.txtBox.insert(END, "Weight\t\t" + self.Weight_var.get() + "\n")
            self.txtBox.insert(END, "Datejoining\t\t" + self.Datejoining.get() + "\n")
            self.txtBox.insert(END, "Dateexpired\t\t" + self.Dateexpired.get() + "\n")
            self.txtBox.insert(END, "Identification\t\t" + self.Identification.get() + "\n")
            self.txtBox.insert(END, "BloodG\t\t" + self.BloodG.get() + "\n")
            self.txtBox.insert(END, "Fees\t\t" + self.Fees.get() + "\n")
            self.txtBox.insert(END, "Paid\t\t" + self.Paid.get() + "\n")
            self.txtBox.insert(END, "Balance\t\t" + self.Balance.get() + "\n")
            self.txtBox.insert(END, "Referral\t\t" + self.Referral.get() + "\n")
        def update_data():
            conn = mysql.connect(user='root', password='root', host='localhost', database="gymdb")
            cur = conn.cursor()

            cur.execute(
                "update gym_table set name=%s,Phnno=%s,Gender=%s,Address1=%s,Address2=%s,Height=%s,Weight=%s,Datejoining=%s,Dateexpired=%s,Identification=%s,BloodG=%s,Fees=%s,Paid=%s,Balance=%s,Referral=%s where memberid=%s",
                (self.name_var.get(), self.Phnno_var.get(),
                 self.Gender_var.get(), self.Address1_var.get(),
                 self.Address2_var.get(), self.Height_var.get(),
                 self.Weight_var.get(), self.Datejoining.get(), self.Dateexpired.get()
                 , self.Identification.get(), self.BloodG.get(),
                 self.Fees.get(), self.Paid.get(),
                 self.Balance.get(), self.Referral.get(),self.memberid_var.get()))

            print("Data updated...")
            conn.commit()
            fetch_data()
            conn.close()

        def delete_Data():
            conn = mysql.connect(user='root', password='root', host='localhost', database="gymdb")
            cur = conn.cursor()
            cur.execute("delete from gym_table where memberid=%s", (self.memberid_var.get(),))
            print("Data Deleted...")
            conn.commit()
            reset_data()
            fetch_data()
            conn.close()
        def reset_data():
            self.txtBox.delete("1.0", 'end')
            self.memberid_var.set("")
            self.name_var.set("")
            self.Phnno_var.set("")
            self.Gender_var.set("")
            self.Address1_var.set("")
            self.Address2_var.set("")
            self.Height_var.set("")
            self.Weight_var.set("")
            self.Datejoining.set("")
            self.Dateexpired.set("")
            self.Identification.set("")
            self.BloodG.set("")
            self.Fees.set("")
            self.Paid.set("")
            self.Balance.set("")
            self.Referral.set("")
        def ext():
            self.root.destroy()
        def fetch_data():
            conn = mysql.connect(user='root', password='root', host='localhost', database="gymdb")
            cur = conn.cursor()
            cur.execute("select * from gym_table")
            rows = cur.fetchall()

            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("", END, values=i)
                conn.commit()
            else:
                self.library_table.delete(*self.library_table.get_children())

            conn.close()
        def get_cursor(event=""):
            cur_row=self.library_table.focus()
            content=self.library_table.item(cur_row)
            row=content['values']
            self.memberid_var.set(row[0])
            self.name_var.set(row[1])
            self.Phnno_var.set(row[2])
            self.Gender_var.set(row[3])
            self.Address1_var.set(row[4])
            self.Address2_var.set(row[5])
            self.Height_var.set(row[6])
            self.Weight_var.set(row[7])
            self.Datejoining.set(row[8])
            self.Dateexpired.set(row[9])
            self.Identification.set(row[10])
            self.BloodG.set(row[11])
            self.Fees.set(row[12])
            self.Paid.set(row[13])
            self.Balance.set(row[14])
            self.Referral.set(row[15])


        lbltitle = Label(self.root, text="GYM MANAGEMENT SYSTEM", bg="black", fg="white", bd=13,
                         relief=RIDGE, font=("Comic Sans MS", 30), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, bg="#918e86", padx=20)
        frame.place(x=0, y=90, width=1365, height=400)



        #######Left frame########

        DataFrameLeft = LabelFrame(frame, text="Gym membership info", bg="#918e86",
                                   fg="black", bd=10, relief=RIDGE, font=("Cambria", 15, "bold"), padx=2,
                                   pady=6)
        DataFrameLeft.place(x=0, y=3, width=650, height=350)

        lblMember = Label(DataFrameLeft, font=("Cambria", 12), text="Member Id -",bg="#918e86", padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        txtMember = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.memberid_var)
        txtMember.grid(row=0, column=1)

        lblname = Label(DataFrameLeft, font=("Cambria", 12), text="Name -", bg="#918e86", padx=2, pady=6)
        lblname.grid(row=1, column=0, sticky=W)
        txtname = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.name_var)
        txtname.grid(row=1, column=1)

        lblphnno = Label(DataFrameLeft, font=("Cambria", 12), text="Phn no -", bg="#918e86", padx=2, pady=6)
        lblphnno.grid(row=2, column=0, sticky=W)
        txtphnno = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Phnno_var)
        txtphnno.grid(row=2, column=1)

        lblgender = Label(DataFrameLeft, font=("Cambria", 12), text="Gender -", bg="#918e86", padx=2, pady=6)
        lblgender.grid(row=3, column=0, sticky=W)
        txtgender = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Gender_var)
        txtgender.grid(row=3, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("Cambria", 12), text="Address1 -", bg="#918e86", padx=2, pady=6)
        lblAddress1.grid(row=4, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Address1_var)
        txtAddress1.grid(row=4, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("Cambria", 12), text="Address2 -", bg="#918e86", padx=2, pady=6)
        lblAddress2.grid(row=5, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Address2_var)
        txtAddress2.grid(row=5, column=1)

        lblHeight = Label(DataFrameLeft, font=("Cambria", 12), text="Height -", bg="#918e86", padx=2, pady=6)
        lblHeight.grid(row=6, column=0, sticky=W)
        txtHeight = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Height_var)
        txtHeight.grid(row=6, column=1)

        lblWeight = Label(DataFrameLeft, font=("Cambria", 12), text="Weight -", bg="#918e86", padx=2, pady=6)
        lblWeight.grid(row=7, column=0, sticky=W)
        txtWeight = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Weight_var)
        txtWeight.grid(row=7, column=1)

        lblDatejoining = Label(DataFrameLeft, font=("Cambria", 12), text="Datejoining -", bg="#918e86", padx=2, pady=6)
        lblDatejoining.grid(row=0, column=2, sticky=W)
        txtDatejoining = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Datejoining)
        txtDatejoining.grid(row=0, column=3)

        lblDateexpired = Label(DataFrameLeft, font=("Cambria", 12), text="Dateexpired -", bg="#918e86", padx=2, pady=6)
        lblDateexpired.grid(row=1, column=2, sticky=W)
        txtDateexpired = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Dateexpired)
        txtDateexpired.grid(row=1, column=3)

        lblIdentification = Label(DataFrameLeft, font=("Cambria", 12), text="Identification marks -", bg="#918e86", padx=2, pady=6)
        lblIdentification.grid(row=2, column=2, sticky=W)
        txtIdentification = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Identification)
        txtIdentification.grid(row=2, column=3)

        lblBloodG = Label(DataFrameLeft, font=("Cambria", 12), text="BloodGroup -", bg="#918e86",padx=2, pady=6)
        lblBloodG.grid(row=3, column=2, sticky=W)
        txtBloodG = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.BloodG)
        txtBloodG.grid(row=3, column=3)

        lblFees = Label(DataFrameLeft, font=("Cambria", 12), text="Fees -", bg="#918e86", padx=2, pady=6)
        lblFees.grid(row=4, column=2, sticky=W)
        txtFees = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Fees)
        txtFees.grid(row=4, column=3)

        lblPaid = Label(DataFrameLeft, font=("Cambria", 12), text="Paid -", bg="#918e86", padx=2, pady=6)
        lblPaid.grid(row=5, column=2, sticky=W)
        txtPaid = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Paid)
        txtPaid.grid(row=5, column=3)

        lblBalance = Label(DataFrameLeft, font=("Cambria", 12), text="Balance -", bg="#918e86", padx=2, pady=6)
        lblBalance.grid(row=6, column=2, sticky=W)
        txtBalance = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Balance)
        txtBalance.grid(row=6, column=3)

        lblReferral = Label(DataFrameLeft, font=("Cambria", 12), text="Referral -", bg="#918e86", padx=2, pady=6)
        lblReferral.grid(row=7, column=2, sticky=W)
        txtReferral = Entry(DataFrameLeft, font=("Cambria", 12), width=20, textvariable=self.Referral)
        txtReferral.grid(row=7, column=3)

        #######Right frame########

        DataFrameRight = LabelFrame(frame, text="Member Info", bg="#918e86", fg="black", bd=10,
                                    relief=RIDGE, font=("Cambria", 15, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=651, y=3, width=650, height=350)

        self.txtBox = Text(DataFrameRight, font=("Comic Sans MS", 12), width=60, height=12)
        self.txtBox.grid(row=0, column=2,padx=10)



        #####button frame####
        Framebutton = Frame(self.root, bg="#918e86", bd=10, relief=RIDGE, padx=20)
        Framebutton.place(x=0, y=490, width=1365, height=70)
        btnAddData = Button(Framebutton, text='Add data', font=("Comic Sans MS", 10, "bold"), width=26, bg="black",
                            fg="white", command=savedata)
        btnAddData.grid(row=0, column=0,pady=6)

        btnShowData = Button(Framebutton, text='Show data', font=("Comic Sans MS", 10, "bold"), width=26, bg="black",
                             fg="white", command=showData)
        btnShowData.grid(row=0, column=1)

        btnUpdateData = Button(Framebutton, text='Update', font=("Comic Sans MS", 10, "bold"), width=26, bg="black",
                               fg="white", command=update_data)
        btnUpdateData.grid(row=0, column=2)

        btnDeleteData = Button(Framebutton, text='Delete data', font=("Comic Sans MS", 10, "bold"), width=26,bg="black",
                               fg="white", command=delete_Data)
        btnDeleteData.grid(row=0, column=3)

        btnResetData = Button(Framebutton, text='Reset', font=("Comic Sans MS", 10, "bold"), width=26, bg="black",
                              fg="white", command=reset_data)
        btnResetData.grid(row=0, column=5)

        btnExit = Button(Framebutton, text='Exit', font=("Comic Sans MS", 10, "bold"), width=26, bg="black",
                         fg="white",command=ext)
        btnExit.grid(row=0, column=6)

        #####information  frame####
        FrameDetails = Frame(self.root, bg="#918e86", bd=10, relief=RIDGE, padx=20)
        FrameDetails.place(x=0, y=560, width=1365, height=130)

        Table_frame = Frame(FrameDetails, bg="#918e86", bd=5, relief=RIDGE)
        Table_frame.place(x=0, y=5, width=1300, height=100)
        xscroll = Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=("memberid", "name", "Phnno", "Gender", "Address1",
                                                               "Address2", "Height", "Weight", "Datejoining", "Dateexpired",
                                                               "Identification",
                                                               "BloodG", "Fees", "Paid", "Balance",
                                                               "Referral"), xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        self.library_table.heading("memberid", text="MemberID")
        self.library_table.heading("name", text="Name")
        self.library_table.heading("Phnno", text="Phnno")
        self.library_table.heading("Gender", text="Gender")
        self.library_table.heading("Address1", text="Address1")
        self.library_table.heading("Address2", text="Address2")
        self.library_table.heading("Height", text="Height")
        self.library_table.heading("Weight", text="Weight")
        self.library_table.heading("Datejoining", text="Datejoining")
        self.library_table.heading("Dateexpired", text="Dateexpired")
        self.library_table.heading("Identification", text="Identification")
        self.library_table.heading("BloodG", text="BloodG")
        self.library_table.heading("Fees", text="Fees")
        self.library_table.heading("Paid", text="Paid")
        self.library_table.heading("Balance", text="Balance")
        self.library_table.heading("Referral", text="Referral")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)
        fetch_data()
        self.library_table.bind("<ButtonRelease-1>", get_cursor)



if __name__=='__main__':
    root=Tk()
    obj=GymManagementSystem(root)
    root.mainloop()
