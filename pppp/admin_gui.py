import tkinter as tk 
from tkinter import messagebox, ttk
from core import AdminPanel


class AdminGUI:

    def __init__(self,bank_system):
        self.bank=bank
        self.root=tk.TK()
        self.root.title('Bank Management System')
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.show_login_window()
        self.root.mainloop()

    def show_login_window(self):
        self.clear()
        tk.Label(self.root, text="Admin Login", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", bg="blue", fg="white", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # For demo, hardcoded admin credentials
        if username == "admin" and password == "1234":
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")


    def show_dashboard(self):

        self.clear()
        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Button(self.root, text="Create Customer", width=25, command=self.gui_create_customer).pack(pady=5)
        tk.Button(self.root, text="Create Account", width=25, command=self.gui_create_account).pack(pady=5)
        tk.Button(self.root, text="View Accounts", width=25, command=self.gui_view_accounts).pack(pady=5)
        tk.Button(self.root, text="View Transactions", width=25, command=self.gui_view_transactions).pack(pady=5)
        tk.Button(self.root, text="Delete Account", width=25, command=self.gui_delete_account).pack(pady=5)
        tk.Button(self.root, text="Logout", width=25, bg="red", fg="white", command=self.show_login_window).pack(pady=20)


    #-----OPTIONALLLLL-----
    def gui_create_customer(self):
        pass
    def gui_create_account(self):
        pass
    def gui_view_accounts(self):
        pass
    def gui_view_transactions(self):
        pass
    def gui_delete_account(self):
        pass

