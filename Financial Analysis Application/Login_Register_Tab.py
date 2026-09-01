from tkinter import  *
from tkinter import messagebox
import hashlib
from RegEx_Validation import RegEx_validation
from Users_Database import User_Database

class Login_Register_Tab(Frame):

    def __init__(self, parent, on_login):
        super().__init__(parent, bg="black")
        self.login_success = on_login
        self.display()

    def display(self):
        Log_Reg_Frame = Frame(self, bg="black")
        Log_Reg_Frame.pack(pady=20)
        # All the entry widgets... TK layout

        # REGISTER Layout... #######################################################################################
        Label(Log_Reg_Frame, text="Register Account ", fg="white", bg="black",
              font=("Rockwell", 38, "bold")).grid(row=0, column=0, padx=(0, 100), pady=5)

        Label(Log_Reg_Frame, text=" Input Email Address ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=1, column=0, padx=(0, 100), pady=5)
        self.reg_email_address = Entry(Log_Reg_Frame, borderwidth=5, font=("Rockwell", 15, "bold"))
        self.reg_email_address.grid(row=2, column=0, columnspan=1, padx=(0, 100), pady=5)

        Label(Log_Reg_Frame, text=" Input Phone Number ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=3, column=0, padx=(0, 100), pady=5)
        self.reg_phone_number = Entry(Log_Reg_Frame, borderwidth=5, font=("Rockwell", 15, "bold"))
        self.reg_phone_number.grid(row=4, column=0, columnspan=1, padx=(0, 100), pady=5)

        Label(Log_Reg_Frame, text=" Create Password ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=5, column=0, padx=(0, 100), pady=8)
        Label(Log_Reg_Frame, text=" Ensure your password is 8 or more characters long,\nand has "
                                  "1 or more special characters", fg="white", bg="black",
              font=("Rockwell", 15, "bold")).grid(row=6, column=0, padx=(0, 100))
        self.reg_password = Entry(Log_Reg_Frame, borderwidth=5, font=("Rockwell", 15, "bold"))
        self.reg_password.grid(row=7, column=0, columnspan=1, padx=(0, 100), pady=5)

        Button(Log_Reg_Frame, text="Create Account", font=("Rockwell", 12, "bold"),
               command=self.submit_register).grid(row=8, padx=(0, 100), pady=10, column=0)

        # LOGIN Layout... ########################################################################################
        Label(Log_Reg_Frame, text="Login ", fg="white", bg="black",
              font=("Rockwell", 38, "bold")).grid(row=0, column=1, pady=10, padx=(90, 0))
        Label(Log_Reg_Frame, text=" Already Have an Account?\nLets get started:  ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=1, column=1, padx=(100, 0), pady=10)

        Label(Log_Reg_Frame, text=" Input Email Address ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=2, column=1, padx=(90, 0), pady=10)
        self.log_email_address = Entry(Log_Reg_Frame, borderwidth=5, font=("Rockwell", 15, "bold"))
        self.log_email_address.grid(row=3, column=1, columnspan=1, padx=(90, 0), pady=10)

        Label(Log_Reg_Frame, text=" Input Password ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=4, column=1, padx=(90, 0), pady=10)
        self.log_password = Entry(Log_Reg_Frame, borderwidth=5, font=("Rockwell", 15, "bold"))
        self.log_password.grid(row=5, column=1, columnspan=1, padx=(90, 0), pady=10)

        Button(Log_Reg_Frame, text="Submit", font=("Rockwell", 12, "bold"), command=self.submit_login).grid(row=6,
                                                                                        padx=(90, 0), pady=25,column=1)

    def submit_login(self):
        email_address = self.log_email_address.get()
        password = self.log_password.get()
        # Firstly passes into class to validate format
        validate = RegEx_validation(email_address, password, given_phone_number=None)

        if validate.login_validation():
            hashed_password = hashlib.sha256(password.encode()).hexdigest()  # hashes da password

            Database = User_Database("./Users.db")  # pass in the location for database instantiating the class
            Database.create_users_table()

            if Database.verify_login(email_address, hashed_password):
                messagebox.showinfo("Success", "You have successfully logged in")
                self.login_success()
            else:
                messagebox.showerror("Error", "Error entering credentials, are you sure\nyou have an account?")
                return

        else:
            messagebox.showerror("Error", "Invalid Email Address or Password")


    def submit_register(self):
        email_address = self.reg_email_address.get()
        phone_number = self.reg_phone_number.get()
        password = self.reg_password.get()
        # Firstly passes into class to validate format
        validate = RegEx_validation(email_address, password, phone_number)
        # if correct validation...
        if validate.register_validation():
            hashed_password = hashlib.sha256(password.encode()).hexdigest()  # hashes da password

            Database = User_Database("./Users.db")  # pass in the location for database instantiating the class
            Database.create_users_table()
            Database.insert_into_users_table(email_address, hashed_password, phone_number)

            messagebox.showinfo("Success", "Your account has been successfully registered")
        else:
            messagebox.showerror("Error", "Invalid entries")





