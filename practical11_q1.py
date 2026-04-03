import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace with CSV file)
data = {
    'month': [1,2,3,4,5,6,7,8,9,10,11,12],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
    'toothpaste': [5200,5100,4550,5870,6100,5800,6000,6500,6200,6100,6300,6400],
    'bathingsoap': [9200,9100,9550,8870,9000,9100,9200,9300,9400,9500,9600,9700],
    'shampoo': [1200,2100,3550,1870,1560,1780,1890,2100,2300,2400,2000,2200],
    'moisturizer': [1500,1800,1600,1700,1900,2000,2100,2200,2300,2400,2500,2600]
}

df = pd.DataFrame(data)

# Total profit (example calculation)
df['total_profit'] = df.iloc[:,1:].sum(axis=1)

plt.figure()
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

plt.figure()

for column in df.columns[1:-1]:
    plt.plot(df['month'], df[column], label=column)

plt.title("Sales Data of All Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

import numpy as np

x = np.arange(len(df['month']))

plt.figure()
plt.bar(x - 0.2, df['facecream'], width=0.4, label='Face Cream')
plt.bar(x + 0.2, df['facewash'], width=0.4, label='Face Wash')

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Cream vs Face Wash Sales")
plt.xticks(x, df['month'])
plt.legend()
plt.show()

total_sales = df.iloc[:,1:-1].sum()

plt.figure()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()