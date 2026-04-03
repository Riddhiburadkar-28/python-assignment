import pandas as pd

# Create data
data = {
    "State": ["Maharashtra", "Gujarat", "Karnataka", "Rajasthan", "Punjab"],
    "Area": [307713, 196244, 191791, 342239, 50362],  # in sq km
    "Population": [124000000, 70000000, 68000000, 81000000, 30000000]
}

df = pd.DataFrame(data)

# a) Complete info
print("State Information:\n")
print(df)

# b) Largest area
largest_area = df.loc[df["Area"].idxmax()]
print("\nState with Largest Area:", largest_area["State"])

# c) Largest population
largest_pop = df.loc[df["Population"].idxmax()]
print("State with Largest Population:", largest_pop["State"])

# d) Population density
df["Density"] = df["Population"] / df["Area"]
print("\nPopulation Density:\n")
print(df[["State", "Density"]])

# e) Highest density
highest_density = df.loc[df["Density"].idxmax()]
print("\nState with Highest Density:", highest_density["State"])