# Program to copy python file without comments

# Taking file names from user
source_file = input("Enter source Python file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as f1:
        lines = f1.readlines()

    with open(destination_file, 'w') as f2:
        for line in lines:
            stripped_line = line.strip()

            # Skip single-line comments and empty lines
            if stripped_line.startswith('#') or stripped_line == "":
                continue

            # Remove inline comments
            if '#' in line:
                line = line.split('#')[0] + '\n'

            f2.write(line)

    print("\nFile copied without comments successfully!")

    # Print source file content
    print("\n--- Source File Content ---")
    with open(source_file, 'r') as f1:
        print(f1.read())

    # Print destination file content
    print("\n--- Destination File Content ---")
    with open(destination_file, 'r') as f2:
        print(f2.read())

except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("Error:", e)