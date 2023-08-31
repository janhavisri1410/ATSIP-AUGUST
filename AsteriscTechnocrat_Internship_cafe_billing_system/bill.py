from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing system")
        bg_color="#8B8378"
        # title=Label(self.root,text="TRADER'S CART",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        # self.icon_title=PhotoImage(file="shake.png")
        title=Label(self.root,text="Cafe Billing System",compound=LEFT,bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==================variables====================
        #=============Pasta=============
        self.Pavioli=IntVar()
        self.LiRnguine=IntVar()
        self.Rigatoni=IntVar()
        self.Farfalle=IntVar()
        self.Fusilli=IntVar()
        self.Cannelloni=IntVar()
        #============Burgers==============
        #Turkey burger,Veggie burger,Wild salmon burger,Bean burger,Cheeseburger
        self.Tburger=IntVar()
        self.Vburger=IntVar()
        self.Wburger=IntVar()
        self.Bburger=IntVar()
        self.Cburger=IntVar()
        self.Nburger=IntVar()
        #==============Milkshakes==============
        self.Chocolate=IntVar()
        self.Strawberry=IntVar()
        self.Blueberry=IntVar()
        self.Caramel=IntVar()
        self.Choco_chips=IntVar()
        self.Oreo=IntVar()

        #==============Total Product Price & Tax Variable=============
        self.pasta_price=StringVar()
        self.burger_price=StringVar()
        self.milkshake_price=StringVar()

        self.pasta_tax=StringVar()
        self.burger_tax=StringVar()
        self.milkshake_tax=StringVar()

        #==========Customer================
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #=======================Customer Detail Frame==============================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=12,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=12,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=12,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=8,padx=10,pady=10)

        #===============Pasta Frame=======================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Pasta",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=300,height=360)
        #Penne avioli. ...LiRnguine. ...Rigatoni. ...Farfalle. ...Fusilli. ...Cannelloni.
        Pen_lbl=Label(F2,text="Penne avioli",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Pen_txt=Entry(F2,width=10,textvariable=self.Pavioli,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Lir_lbl=Label(F2,text="LiRnguine",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Lir_txt=Entry(F2,width=10,textvariable=self.LiRnguine,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Rig_lbl=Label(F2,text="Rigatoni",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Rig_txt=Entry(F2,width=10,textvariable=self.Rigatoni,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Far_lbl=Label(F2,text="Farfelle",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Far_txt=Entry(F2,width=10,textvariable=self.Farfalle,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Fusi_lbl=Label(F2,text="Fusilli",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Fusi_txt=Entry(F2,width=10,textvariable=self.Fusilli,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Can_lbl=Label(F2,text="Cannelloni",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Can_txt=Entry(F2,width=10,textvariable=self.Cannelloni,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============Burger Frame=====================
        #Turkey burger,Veggie burger,Wild salmon burger,Bean burger,Cheeseburger
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Burgers",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=310,y=170,width=315,height=360)

        b1_lbl=Label(F3,text="Turkey burger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        b1_txt=Entry(F3,width=10,textvariable=self.Tburger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        b2_lbl=Label(F3,text="Veggie burger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        b2_txt=Entry(F3,width=10,textvariable=self.Vburger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        b3_lbl=Label(F3,text="Wild salmon",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        b3_txt=Entry(F3,width=10,textvariable=self.Wburger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        b4_lbl=Label(F3,text="Bean burger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        b4_txt=Entry(F3,width=10,textvariable=self.Bburger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        b5_lbl=Label(F3,text="Cheeseburger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        b5_txt=Entry(F3,width=10,textvariable=self.Cburger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        b6_lbl=Label(F3,text="Nut Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        b6_txt=Entry(F3,width=10,textvariable=self.Nburger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============Milkshakes Frame=====================
        #Choco shake,Strawberry shake,Blueberry shake,Salted Caramel and Chocolate Chip shake,Chai Tea Latte shake,Oreo shake,Peppermint Bark shake
        
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Milkshakes",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=630,y=170,width=300,height=360)

        b1_lbl=Label(F4,text="Chocolate",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        b1_txt=Entry(F4,width=10,textvariable=self.Chocolate,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        b2_lbl=Label(F4,text="Strawberry",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        b2_txt=Entry(F4,width=10,textvariable=self.Strawberry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        b3_lbl=Label(F4,text="Blueberry",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        b3_txt=Entry(F4,width=10,textvariable=self.Blueberry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        b4_lbl=Label(F4,text="Caramel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        b4_txt=Entry(F4,width=10,textvariable=self.Caramel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        b5_lbl=Label(F4,text="Choco Chips",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        b5_txt=Entry(F4,width=10,textvariable=self.Choco_chips,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        b6_lbl=Label(F4,text="Oreo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        b6_txt=Entry(F4,width=10,textvariable=self.Oreo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================Bill Area=======================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=940,y=170,width=330,height=360)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #==============Button Frame=========================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=530,relwidth=1,height=125)

        m1_lbl=Label(F6,text="Total Pasta Price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.pasta_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Burger Price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.burger_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Milkshake Price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.milkshake_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Pasta Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.pasta_tax,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Burger Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=1,column=2,padx=10,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.burger_tax,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Milkshake Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=2,column=2,padx=10,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable= self.milkshake_tax,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=5,relief=GROOVE)
        btn_F.place(x=620,width=630,height=90)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="black",fg="white",bd=4,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=1)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="black",fg="white",bd=4,pady=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=1)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="black",fg="white",bd=4,pady=15,width=11,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=1)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="black",fg="white",bd=4,pady=15,width=11,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=1)
        self.welcome_bill()

    def total(self):
        self.p_p_p=self.Pavioli.get()*40
        self.p_l_p=self.LiRnguine.get()*60
        self.p_r_p=self.Rigatoni.get()*80
        self.p_far_p=self.Farfalle.get()*100
        self.p_fus_p=self.Fusilli.get()*120
        self.p_c_p=self.Cannelloni.get()*140

        self.total_pasta_price=float(
                                    self.p_p_p+
                                    self.p_l_p+
                                    self.p_r_p+
                                    self.p_far_p+
                                    self.p_fus_p+
                                    self.p_c_p
                                )
        self.pasta_price.set("Rs. "+str(self.total_pasta_price))
        self.p_tax=round((self.total_pasta_price*0.05),2)
        self.pasta_tax.set("Rs. "+str((self.p_tax)))

        self.b_t_p=self.Tburger.get()*50
        self.b_v_p=self.Vburger.get()*60
        self.b_w_p=self.Wburger.get()*90
        self.b_b_p=self.Bburger.get()*110
        self.b_c_p=self.Cburger.get()*125
        self.b_n_p=self.Nburger.get()*145

        self.total_burger_price=float(
                                        self.b_t_p+
                                        self.b_v_p+
                                        self.b_w_p+
                                        self.b_b_p+
                                        self.b_c_p+
                                        self.b_n_p
                                )
        self.burger_price.set("Rs. "+str(self.total_burger_price))
        self.b_tax=round((self.total_burger_price*0.1),2)
        self.burger_tax.set("Rs. "+str(self.b_tax))

        self.m_ch_p=self.Chocolate.get()*50
        self.m_s_p=self.Strawberry.get()*60
        self.m_b_p=self.Blueberry.get()*90
        self.m_c_p=self.Caramel.get()*110
        self.m_cc_p=self.Choco_chips.get()*125
        self.m_o_p=self.Oreo.get()*145

        self.total_milkshake_price=float(
                                        self.m_ch_p+
                                        self.m_s_p+
                                        self.m_b_p+
                                        self.m_c_p+
                                        self.m_cc_p+
                                        self.m_o_p
                                )
        self.milkshake_price.set("Rs. "+str(self.total_milkshake_price))
        self.m_tax=round((self.total_milkshake_price*0.05),2)
        self.milkshake_tax.set("Rs. "+str((self.m_tax)))

        self.Total_bill=float(self.total_pasta_price+
                              self.total_burger_price+
                              self.total_milkshake_price+
                              self.p_tax+
                              self.b_tax+
                              self.m_tax
                            )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcafe Retail\n")
        self.txtarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n====================================")
        self.txtarea.insert(END,f"\n Items\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are necessary!!!")
        elif self.pasta_price.get()=="Rs. 0.0" and self.burger_price.get()=="Rs. 0.0" and self.milkshake_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No order was given.")
        else:
            self.welcome_bill()
            #========pasta===========
            if self.Pavioli.get()!=0:
                self.txtarea.insert(END,f"\n Pavioli \t\t{self.Pavioli.get()}\t{self.p_p_p}")
            if self.LiRnguine.get()!=0:
                self.txtarea.insert(END,f"\n LiRnguine \t\t{self.LiRnguine.get()}\t{self.p_l_p}")
            if self.Rigatoni.get()!=0:
                self.txtarea.insert(END,f"\n Rigatoni \t\t{self.Rigatoni.get()}\t{self.p_r_p}")
            if self.Farfalle.get()!=0:
                self.txtarea.insert(END,f"\n Farfalle \t\t{self.Farfalle.get()}\t{self.p_far_p}")
            if self.Fusilli.get()!=0:
                self.txtarea.insert(END,f"\n Fusilli \t\t{self.Fusilli.get()}\t{self.p_fus_p}")
            if self.Cannelloni.get()!=0:
                self.txtarea.insert(END,f"\n Cannelloni \t\t{self.Cannelloni.get()}\t{self.p_c_p}")

            #========burgers===========

            if self.Tburger.get()!=0:
                self.txtarea.insert(END,f"\n Turkey burger \t\t{self.Tburger.get()}\t{self.b_t_p}")
            if self.Vburger.get()!=0:
                self.txtarea.insert(END,f"\n Veggie burger \t\t{self.Vburger.get()}\t{self.b_v_p}")
            if self.Wburger.get()!=0:
                self.txtarea.insert(END,f"\n Wild Salmon \t\t{self.Wburger.get()}\t{self.b_w_p}")
            if self.Bburger.get()!=0:
                self.txtarea.insert(END,f"\n Bean Burger \t\t{self.Bburger.get()}\t{self.b_b_p}")
            if self.Cburger.get()!=0:
                self.txtarea.insert(END,f"\n Cheeseburger \t\t{self.Cburger.get()}\t{self.b_c_p}")
            if self.Nburger.get()!=0:
                self.txtarea.insert(END,f"\n Nut Burger \t\t{self.Nburger.get()}\t{self.b_n_p}")

            #========milkshakes=============
            if self.Chocolate.get()!=0:
                self.txtarea.insert(END,f"\n Chocolate \t\t{self.Chocolate.get()}\t{self.m_ch_p}")
            if self.Strawberry.get()!=0:
                self.txtarea.insert(END,f"\n Strawberry \t\t{self.Strawberry.get()}\t{self.m_s_p}")
            if self.Blueberry.get()!=0:
                self.txtarea.insert(END,f"\n Blueberry \t\t{self.Blueberry.get()}\t{self.m_b_p}")
            if self.Caramel.get()!=0:
                self.txtarea.insert(END,f"\n Caramel \t\t{self.Caramel.get()}\t{self.m_c_p}")
            if self.Choco_chips.get()!=0:
                self.txtarea.insert(END,f"\n Choco_chips \t\t{self.Choco_chips.get()}\t{self.m_cc_p}")
            if self.Oreo.get()!=0:
                self.txtarea.insert(END,f"\n Oreo \t\t{self.Oreo.get()}\t{self.m_o_p}")

            self.txtarea.insert(END,f"\n------------------------------------")
            if self.pasta_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Pasta Tax\t\t\t{self.pasta_tax.get()}")
            if self.burger_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Burger Tax\t\t\t{self.burger_tax.get()}")
            if self.milkshake_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Milkshake Tax\t\t\t{self.milkshake_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill : \t\t\tRs {self.Total_bill}")
            self.txtarea.insert(END,f"\n------------------------------------")
            self.save_bill()
            
    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()}saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op=messagebox.askyesno("Clear Data","Do you really want to CLEAR DATA?")
        if op>0:
            
            #=============Pasta=============
            self.Pavioli.set(0)
            self.LiRnguine.set(0)
            self.Rigatoni.set(0)
            self.Farfalle.set(0)
            self.Fusilli.set(0)
            self.Cannelloni.set(0)
            #============Burgers==============
            #Turkey burger,Veggie burger,Wild salmon burger,Bean burger,Cheeseburger
            self.Tburger.set(0)
            self.Vburger.set(0)
            self.Wburger.set(0)
            self.Bburger.set(0)
            self.Cburger.set(0)
            self.Nburger.set(0)
            #==============Milkshakes==============
            self.Chocolate.set(0)
            self.Strawberry.set(0)
            self.Blueberry.set(0)
            self.Caramel.set(0)
            self.Choco_chips.set(0)
            self.Oreo.set(0)

            #==============Total Product Price & Tax Variable=============
            self.pasta_price.set("")
            self.burger_price.set("")
            self.milkshake_price.set("")

            self.pasta_tax.set("")
            self.burger_tax.set("")
            self.milkshake_tax.set("")

            #==========Customer================
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit?")
        if op>0:
            self.root.destroy()



root=Tk()
obj=Bill_App(root)
root.mainloop()