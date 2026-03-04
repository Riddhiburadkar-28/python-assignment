# Program to calculate grade of steel

# Taking input from user
hardness = float(input("Enter Hardness: "))
carbon = float(input("Enter Carbon Content: "))
tensile = float(input("Enter Tensile Strength: "))

# Checking conditions
cond1 = hardness > 50
cond2 = carbon < 0.7
cond3 = tensile > 5600

# Determining grade
if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5

# Display result
print("Grade of Steel:", grade)