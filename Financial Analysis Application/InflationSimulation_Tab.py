from tkinter import  *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Calculate_Inflation import Inflation_Simulation


class Inflation_Simulation_Tab(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")
        # initial values the user will enter
        self.initial_salary = None
        self.inflation_rate = None
        self.salary_growth_rate = None
        self.years = None
        self.explanation = None
        self.inflation_simulator_tab() # kickstart the simulation process

    def inflation_simulator_tab(self):

        Label(self, text="Inflation Simulator", fg="white", bg="black", font=("Rockwell", 38, "bold")).pack(
            pady=20)

        self.explanation = Text(self, width=70, height=2, font=("Rockwell", 15, "bold"), borderwidth=5)
        self.explanation.pack(pady=10)
        self.explanation.insert(END, "View how your salary will change over the next years...")

        # input frame, inside the simulation tab (frame)
        simulate = Frame(self, bg="black")
        simulate.pack(pady=10)
        # All the entry widgets... TK layout
        Label(simulate, text=" Initial salary £ ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=1, column=0)
        Label(simulate, text=" Inflation rate % ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=2, column=0)
        Label(simulate, text=" Salary growth rate % ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=3, column=0)
        Label(simulate, text=" Years ", fg="white", bg="black",
              font=("Rockwell", 20, "bold")).grid(row=4, column=0)

        self.initial_salary = Entry(simulate, borderwidth=5, font=("Rockwell", 12, "bold"))
        self.initial_salary.grid(row=1, column=1, columnspan=1, pady=5)

        self.inflation_rate = Entry(simulate, borderwidth=5, font=("Rockwell", 12, "bold"))
        self.inflation_rate.grid(row=2, column=1, columnspan=1, pady=5)

        self.salary_growth_rate = Entry(simulate, borderwidth=5, font=("Rockwell", 12, "bold"))
        self.salary_growth_rate.grid(row=3, column=1, columnspan=1, pady=5)

        self.years = Entry(simulate, borderwidth=5, font=("Rockwell", 12, "bold"))
        self.years.grid(row=4, column=1, columnspan=2, pady=8)
        Button(simulate, text="Submit", font=("Rockwell", 12, "bold"),
               command=lambda: self.submit_button()).grid(row=5, column=1)



    def submit_button(self):
        try: # VALIDATION OF USER ENTRIES HERE
            initial_salary = float(self.initial_salary.get())
            inflation_rate = float(self.inflation_rate.get())
            salary_growth_rate = float(self.salary_growth_rate.get())
            years = int(self.years.get())

            if initial_salary <= 0 or years <= 0:
                messagebox.showinfo("Error", "Initial salary & years must be positive")
            elif salary_growth_rate < 0:
                messagebox.showinfo("Error", "Salary growth rate must be positive")
            # after validation has checked, then takes to the simulator
            self.run_simulation(initial_salary, inflation_rate, salary_growth_rate, years)

        except ValueError:
            # if the inputs can't be converted into its required datatypes
            messagebox.showerror("Error", "Invalid entries")


    def run_simulation(self, initial_salary, inflation_rate, salary_growth_rate, years):

        if hasattr(self, "graph_frame") and self.graph_frame.winfo_exists():
            self.graph_frame.destroy()  # Remove old graphs
        self.explanation.delete("1.0", END)

        self.graph_frame = Frame(self)
        self.graph_frame.pack(pady=18, fill="both", expand=True)

        # passes into the class simulator
        simulate = Inflation_Simulation(initial_salary, inflation_rate, salary_growth_rate, years)
        # calculate the inflation values
        simulate.calculating_nominal_salary()
        simulate.calculating_real_salary()
        simulate.simulate_years()
        # Take difference of last figures calculated
        end_value_nominal = round(simulate.nominal_salaries[-1],2)
        end_value_real = round(simulate.real_salaries[-1],2)
        difference = round(end_value_nominal - end_value_real,2)

        figure = Figure(figsize=(6, 4))
        matplotlib = figure.add_subplot(111)
        # Begin plotting the data...
        matplotlib.plot(simulate.plot_against_years, simulate.nominal_salaries, marker="o", label="Your Nominal salary")
        matplotlib.plot(simulate.plot_against_years, simulate.real_salaries, marker="o", label="Your Real salary")
        matplotlib.fill_between(simulate.plot_against_years,simulate.nominal_salaries, simulate.real_salaries,
                                facecolor="red", alpha=0.3, label="Your loss in income value")
        matplotlib.set_xlabel("Years")
        matplotlib.set_ylabel("Salary Value £")
        matplotlib.legend()
        matplotlib.grid(True)

        canvas = FigureCanvasTkAgg(figure, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        # Inserts an explanation each time a graph is made
        explanation = (f"After {int(self.years.get())} years, your nominal salary becomes "
                                     f"£{end_value_real}, whilst your real salary becomes £{end_value_nominal}."
                                     f"Your purchasing power has decreased by £{difference}.")

        self.animate_text(explanation)


    def animate_text(self, explain, index=0):
            if index == 0:
                self.explanation.delete("1.0", END)

            if index >= len(explain):
                return False
            else:
                self.explanation.insert(END, explain[index])
                self.explanation.after(40, self.animate_text, explain, index + 1)
                return True