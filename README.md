# SAP-Group-3-Assignment
Smart Water Management
To my teammates :
    Once you've finished your code, dont forget to push and make a pull request so i may merge it into the main code
    if sect==1:
        print("\n                     UPDATE SYSTEM PARAMETERS")
print("\n--------------------------------------------------------------------")

# Validate residents
while True:
    try:
        res = int(input("\nEnter the new number of residents: "))
        if res > 0:
            break
        print("Error: Number of residents must be greater than 0. Try again.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

# Validate tank capacity
while True:
    try:
        tankcap = float(input("Enter the new maximum tank capacity (L): "))
        if tankcap > 0:
            break
        print("Error: Tank capacity must be greater than 0. Try again.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Validate water level
while True:
    try:
        watlvl = float(input("Enter the new water level (L): "))
        if 0 <= watlvl <= tankcap:
            break
        print(f"Error: Water level must be between 0 and {tankcap}L. Try again.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Validate daily consumption
while True:
    try:
        dlyconsump = float(input("Enter the new average daily consumption per person (L): "))
        if dlyconsump >= 0:
            break
        print("Error: Consumption cannot be negative. Try again.")
    except ValueError:
        print("Error: Please enter a valid number.")

print("\n--------------------------------------------------------------------")
print("\nAll parameters successfully updated and verified!")
