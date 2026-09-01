from matplotlib import pyplot as plt


class Inflation_Simulation:

     def __init__(self, given_initial_salary: float, given_inflation_rate: float,
                 given_salary_growth_rate: float, given_years: int):
         self.initial_salary = given_initial_salary
         self.inflation_rate = given_inflation_rate/100 # convert %s to decimals
         self.salary_growth_rate = given_salary_growth_rate/100
         self.years = given_years
         self.nominal_salaries = [] # list of today's wages (no inflation deduction)
         self.real_salaries = []  # list of inflation deducted wages (shows true purchasing power)
         self.plot_against_years = []  # plot nominal & real salaries against the years.


     def calculating_nominal_salary(self):
         # GEOMETRIC FORMULA --> initialSalary x (1 + salary-growth-rate)^ number-of-years

         growth_rate = 1 + self.salary_growth_rate  # assign it to variable (for simplicity)

         for t in range(self.years + 1):  # include last year
             value = self.initial_salary * (growth_rate ** t)
             self.nominal_salaries.append(value)
         return self.nominal_salaries


     def calculating_real_salary(self):
         # GEOMETRIC FORMULA --> initialSalary x (1 + salary-growth-rate/ 1 + inflation-rate)^ number-of-years

         growth_rate = 1 + self.salary_growth_rate  # assign it to variable (for simplicity)
         inflation_rate = 1 + self.inflation_rate

         for t in range(self.years + 1):
             value = self.initial_salary * (growth_rate / inflation_rate) ** t
             self.real_salaries.append(value)
         return self.real_salaries


     def simulate_years(self):
         # function simply to generate a list of years, to plot the nominal & real salaries against
         y = self.years + 1
         for i in range(y):
             self.plot_against_years.append(i)
         return self.plot_against_years

     def plotting_graph(self):
         # generate lists
         self.calculating_nominal_salary()
         self.calculating_real_salary()
         self.simulate_years()

         plt.figure(figsize=(10, 6))  # Set plot size (& create figure first)
         plt.title("Your Nominal Salary & Inflation deducted (Real) Salary over Years ")
         plt.xlabel("Year")
         plt.ylabel("Value £")
         # Plot the lists
         plt.plot(self.plot_against_years, self.nominal_salaries, color="k", marker="o",
                  label="Your Nominal Salaries")
         plt.plot(self.plot_against_years, self.real_salaries, color="b", marker="o",
                  label="Real Salaries (Your true purchasing power)")

         plt.legend()  # is what acc puts the labels on
         plt.grid(True)  # puts a grid d on

         plt.show()



if __name__ == "__main__":
         Inflation_Simulation =Inflation_Simulation(10000,2, 3, 20)
         Inflation_Simulation.plotting_graph()