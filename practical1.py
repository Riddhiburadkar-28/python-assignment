# Program to store employee details and calculate salary

# Taking employee details as input
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculating allowances
DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary

# LIC deduction
LIC = 500

# Calculating Gross Salary
gross_salary = basic_salary + DA + HRA + TA

# Calculating Net Salary
net_salary = gross_salary - LIC

# Displaying Employee Details and Salary
print("\n----- Employee Details -----")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)

print("\n----- Salary Details -----")
print("Basic Salary:", basic_salary)
print("DA (92%):", DA)
print("HRA (58%):", HRA)
print("TA (30%):", TA)
print("LIC Deduction:", LIC)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)