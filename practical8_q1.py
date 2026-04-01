# Program to read a file and write contents in uppercase

# Taking file names from user
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    # Open source file in read mode
    with open(source_file, 'r') as f1:
        content = f1.read()

    # Convert content to uppercase
    upper_content = content.upper()

    # Open destination file in write mode
    with open(destination_file, 'w') as f2:
        f2.write(upper_content)

    print("\nContent successfully copied in UPPERCASE!")

except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("Error:", e)