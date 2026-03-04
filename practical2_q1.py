# Program to calculate current using Ohm's Law
# Ohm's Law: I = V / R

# Taking input from user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

# Checking if resistance is zero
if resistance == 0:
    print("Resistance cannot be zero.")
else:
    # Calculating current
    current = voltage / resistance
    print("Current (I) =", current, "Amperes")

    # Checking nature of current
    if current < 0.5:
        print("Low current")
    elif 0.5 <= current <= 2:
        print("Normal current")
    else:
        print("High current")