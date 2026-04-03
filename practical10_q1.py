import pandas as pd

# Read CSV file
df = pd.read_csv(r"C:\Users\User\Desktop\books.csv")

# a) Complete report
print("Complete Book Report:\n")
print(df)

# b) Books by given author
author = input("\nEnter author name: ")
print("\nBooks by Author:")
print(df[df["Author"] == author])

# c) Books by publisher
publisher = input("\nEnter publisher name: ")
print("\nBooks by Publisher:")
print(df[df["Publisher"] == publisher])

# d) Cheapest & Costliest books
cheapest = df.loc[df["Price"].idxmin()]
costliest = df.loc[df["Price"].idxmax()]

print("\nCheapest Book:", cheapest["Title"])
print("Costliest Book:", costliest["Title"])

# e) Sort by year
print("\nBooks sorted by Year:")
print(df.sort_values(by="Year"))