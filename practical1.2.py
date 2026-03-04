# Program to store vendor details and generate annual purchase report

# Taking vendor details as input
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Reading monthly purchases
monthly_purchases = []

print("\nEnter purchase amount for each month:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    monthly_purchases.append(amount)

# Calculating total annual purchase
annual_total = sum(monthly_purchases)

# Displaying Report
print("\n----- Vendor Details -----")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)

print("\n----- Annual Purchase Report -----")
for i in range(12):
    print(f"Month {i+1} Purchase: {monthly_purchases[i]}")

print("\nTotal Annual Purchase:", annual_total)