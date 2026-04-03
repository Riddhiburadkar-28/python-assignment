import matplotlib.pyplot as plt 
companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','Atos','Amdocs']
recruitments = [120,150,180,100,90,110,80,95]

plt.figure()
plt.bar(companies, recruitments)
plt.title("Company Recruitment")
plt.xlabel("Companies")
plt.ylabel("Number of Hires")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

explode = [0.1 if c == 'Amazon' else 0 for c in companies]

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')

# Draw circle for doughnut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

plt.title("Doughnut Chart")
plt.show()

names = ['IBM','Amdocs']
values = [100,95]

plt.figure()
plt.bar(names, values)
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Number of Hires")
plt.show()