# The goal is to create a notebook, so that when the user successfully
# logs in the other tabs will create (instantiate designated classes)

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook # import necessary libraries
from Calculate_Inflation import Inflation_Simulation
from Login_Register_Tab import Login_Register_Tab
from InflationSimulation_Tab import Inflation_Simulation_Tab


class Main_Control(Tk):

    def __init__(self):
        super().__init__() # use su
        self.title("Financial Analysis Application")
        self.geometry("500x500")
        # override default Tkinter Notebook design
        design = ttk.Style()
        design.theme_use("default")
        design.configure("TNotebook", background="dark blue")
        design.configure("TNotebook", background="dark blue", foreground="white")
        design.map("TNotebook.Tab", background=[("selected", "dark blue")], foreground=[("selected", "white")])
        design.configure("TFrame", background="dark blue")
        design.configure("TLabel", background="dark blue", foreground="white")
        design.configure("TButton", background="dark blue", foreground="white")
        #define the NOTEBOOK
        self.notebook = Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        # Instantiating each tab (calling each of their classes)
        self.login_page = Login_Register_Tab(self.notebook, on_login=self.create_other_tabs)
        self.notebook.add(self.login_page, text="Login/Register Your Account")


    def create_other_tabs(self):
        # if user logs in correctly
        self.simulation_tab = Inflation_Simulation_Tab(self.notebook)
        self.notebook.add(self.simulation_tab, text="Inflation Simulation")  # Adding each tab to the notebook


if __name__ == "__main__":
    app = Main_Control()
    app.mainloop()