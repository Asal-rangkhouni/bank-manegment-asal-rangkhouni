'''





'''

import tkinter as tk 
from tkinter import messagebox, ttk
from core import AdminPanel

class AdminGUI:

    def __init__(self,bank_system):
        self.bank= bank_system 
        self.root=tk.TK()
        self.root.title('Bank Management System')
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.show_login_window()
        self.root.mainloop()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_window(self):
        self.clear()
        self.root.configure(bg="#20252b")

        #manitor vasat atm
        screen = tk.Frame(self.root , bg= "#1b2a34", bd=8, relief="ridge")
        screen.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
        #onvan
        tk.Label(
            screen,
            text="ADMIN AUTHENTICATION" ,
            font = ("Consolas", 18, "bold") ,
            bg="#1b2a34",
            fg="#00ff99"
        ).pack(pady=15)

        #form frame
        form = tk.Frame(screen , bg= "#1b2a34")
        form.pack(pady = 10) 

        #username
        tk.Label(form, text="Username:", font=("Consolas", 12), bg="#1b2a34", fg="#cfd8dc").pack(anchor="w")
        self.username_entry = tk.Entry(form, width=30, font=("Consolas", 12), bg="#263238", fg="white", insertbackground="white")
        self.username_entry.pack(pady=5)

        #passwors
        tk.Label(form , text="Password:" ,font=("Consolas" , 12)  , bg="#1b2a34", fg="#cfd8dc").pack(anchor="w")
        self.password_entry = tk.Entry(form , width=30, font=("Consolas", 12), show="*", bg="#263238", fg="white", insertbackground="white")
        self.password_entry.pack(pady=5)

        #dokme login
        tk.Button(
        screen,
        text="LOGIN",
        font=("Consolas", 12, "bold"),
        width=20,
        height=1,
        bg="#009688",
        fg="white",
        activebackground="#00796b",
        cursor="hand2",
        command=self.login
    ).pack(pady=20)
        
        #navar vaziat
        self.status_label = tk.Label(
        self.root,
        text="READY | Please enter admin credentials...",
        font=("Consolas", 10),
        bg="#20252b",
        fg="#90a4ae"
    )
        
        self.status_label = tk.Label(self.root, text="READY | Please enter admin credentials...",
                             font=("Consolas", 10),
                             bg="#20252b",
                             fg="#90a4ae")
        self.status_label.pack(side="bottom", fill="x")

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        # For demo, hardcoded admin credentials

        if not username or not password:
            self.status_label.config(text="ERROR | Username and password required.")
            messagebox.showerror("Login Error", "Username and password are required.")
            return

        if username == "admin" and password == "1234":
            self.status_label.config(text="ACCESS GRANTED | Loading dashboard...")
            self.show_dashboard()
        else:
            self.status_label.config(text="ACCESS DENIED | Invalid credentials.")
            messagebox.showerror("Error", "Invalid credentials")


    def show_dashboard(self):

        self.clear()
        #rang koli paszamine
        self.root.configure(bg= "#20252b")

        #frame safhe namayesh
        screen = tk.Frame(self.root , bg= "#1b2a34", bd=8 , relief= "ridge" )
        screen.place(relx=0.5, rely=0.5 , anchor= "center" , width=600 , height= 400)

        # esm baka screen
        tk.Label(
            screen ,
            text = "BAKN ADMIN TERMINAL " , 
            font= ("Consolas" , 18 , " bold"),
            bg= "#1b2a34" ,
            fg = "#00ff99"
        ).pack(pady=10)

        #tozih zir onvan
        tk.Label(
            screen ,
            text= "Select an operation:" , 
            font = ("Consolas" , 12) ,
            bg = "#1b2a34" ,
            fg= "#cfd8dc"       
        ).pack(pady=5)

        #frame dokme
        btn_frame = tk.Frame(screen , bg = "#1b2a34")
        btn_frame.pack(expand=True, fill="both", pady=10)

        #dokme samt chap
        left_frame = tk.Frame(btn_frame , bg = "#1b2a34")
        left_frame.pack(side="left", expand=True, fill="both", padx=10)

        #dokme samt rast
        right_frame = tk.Frame(btn_frame , bg = "#1b2a34")
        right_frame.pack(side="right", expand=True, fill="both", padx=10)

        #style dokme
        btn_style = {
        "font": ("Consolas", 11, "bold"),
        "width": 20,
        "height": 2,
        "bg": "#263238",
        "fg": "#eceff1",
        "activebackground": "#37474f",
        "activeforeground": "#ffffff",
        "bd": 2,
        "relief": "raised",
        "cursor": "hand2"
    }

        #dokme samt chap
        tk.Button(left_frame, text="Create Customer", command=self.gui_create_customer, **btn_style).pack(pady=8)
        tk.Button(left_frame, text="Create Account", command=self.gui_create_account, **btn_style).pack(pady=8)
        tk.Button(left_frame, text="View Accounts", command=self.gui_view_accounts, **btn_style).pack(pady=8)

        #dokme samt rast
        tk.Button(right_frame, text="View Transactions", command=self.gui_view_transactions, **btn_style).pack(pady=8)
        tk.Button(right_frame, text="Delete Account", command=self.gui_delete_account, **btn_style).pack(pady=8)
        tk.Button(
        right_frame,
        text="Logout",
        command=self.show_login_window,
        **btn_style,
        bg="#b71c1c",
        activebackground="#d32f2f"
    ).pack(pady=8)


        #payam atm
        status = tk.Label(
        self.root,
        text="READY | Insert admin command...",
        font=("Consolas", 10),
        bg="#20252b",
        fg="#90a4ae"
    )
        status.pack(side="bottom", fill="x")



    #-----OPTIONALLLLL-----
    def gui_create_customer(self):
        self.clear()
        tk.Label(self.root , text="Creat New Customer" , font=("Arial" , 18 , "bold")).pack(pady=20)

        #frame vorodi
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        lbl1 = ["Name" , "Last name" , "Email" , "Phone" , "Address"]
        self.entrise = {}

        for label in lbl1 :
            tk.Label(frame , text= label + ":" , anchor="w" ).pack()
            entry = tk.Entry(frame, width=40)
            entry.pack(pady=5)
            self.entries[label.lower()] = entry

        #dokme moshtari
        tk.Button(self.root , text="Creat Customer" , bg="green" , fg="white" , width=20 , command=self.create_customer_action).pack(pady=20)
        tk.Button(self.root , text="Back" , command= self.show_dashboard)

        #dokme submit
        def create_customer_action():
            name = self.entries["name"].get()
            last_name = self.entrise["Last_name"].get()
            email = self.entrise["email"].get()
            phone = self.entrise["phone"].get()
            address = self.entrise["address"].get()

            if not name or not email:
                messagebox.showerror("Error", "Name and Email are required!")
                return
            
            try:
                self.bank.create_customer(name, last_name, email, phone, address)
                messagebox.showinfo("Success", "Customer created successfully!")
                self.show_dashboard()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    
    def gui_create_account(self):
        pass
    def gui_view_accounts(self):
        pass
    def gui_view_transactions(self):
        pass
    def gui_delete_account(self):
        pass

