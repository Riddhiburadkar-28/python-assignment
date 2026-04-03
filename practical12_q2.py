import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("Employees in Automotive domain:")
print(df[df["Department"] == "Automotive"])

# b) Details of employee by ID
emp_id = int(input("Enter Employee ID: "))
print("\nEmployee Details:")
print(df[df["Employee ID"] == emp_id])

# d) List of Developers
print("\nList of Developers:")
print(df[df["Designation"] == "Developer"])