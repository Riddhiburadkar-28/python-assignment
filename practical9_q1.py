class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self, name, age, salary, address):
        super().__init__(name, age, salary, address)


# List to store 10 managers
managers = []

# Input for 10 managers
for i in range(2):   # change to 10 if needed
    print(f"\nEnter details of Manager {i+1}")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    address = input("Enter Address: ")

    m = Manager(name, age, salary, address)
    managers.append(m)

# Display all managers
print("\n--- Manager Details ---")
for i, m in enumerate(managers):
    print(f"\nManager {i+1}:")
    m.display()