print("====================================================================")
print("\n                        H Y D R O X U S")
print("                           G U A R D")
print("\n====================================================================")
print("\n                            Welcome.")

#Getting data from User1

status = True
while status:
    try:
        res=int(input("\nEnter the number of residents: "))
        tankcap=float(input("Enter the maximum tank capacity (L): "))
        watlvl=float(input("Enter the current water level (L): "))
        dlyconsump=float(input("Enter the average daily consumption per day (L):"))

        #Validating if the data is viable or not

        if tankcap<watlvl:
            print("\n====================================================================")
            print("\n                         Invalid data.")
            print("       Water level cannot be higher than tank capacity.")
            print("                  Enter the data value again.")
            print("\n====================================================================")

        else:
            status = False

    except ValueError:
        print("\n====================================================================")
        print("\n                           Invalid data.")
        print("                        Enter a valid number.")
        print("\n====================================================================")


sect=0

while sect!=6:
    print("\n====================================================================")
    print("\nResidents           : ",res)
    print("Max tank capacity   : ",tankcap,"L")
    print("Current water level : ",watlvl,"L")
    print("Daily consumption   : ",dlyconsump,"L")
    print("\n--------------------------------------------------------------------")
    print("\n[1] Update system parameters")
    print("[2] Analyse water consumption")
    print("[3] Check rainwater collection")
    print("[4] Activate conservation mode")
    print("[5] Future water simulation")
    print("[6] Exit")
    sect=int(input("\nEnter the desired numbered Section : "))
    print("\n====================================================================")

    #Section Function

    #Roza
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
    #Azfar Hariz
    elif sect==2:
        water_used = tankcap - watlvl
        print("\nAn amount of", f"{water_used:.2f}", "L has been used")

        days_left = watlvl / dlyconsump
        water_percentage = watlvl / tankcap * 100

        def progress_bar(water_percentage):
            print("\n0% |||" + ("/" * int(water_percentage // 2)) + (" " * (50 - int(water_percentage // 2))) + "||| 100%\n")

        if 30 < water_percentage <= 50:
            print("Current Water level is moderate")
            print("Water percentage:", f"{water_percentage:.2f}" + "%")
            progress_bar(water_percentage)
        elif 10 < water_percentage <= 30:
            print("Current Water level is low")
            print("Water percentage:", f"{water_percentage:.2f}" + "%")
            progress_bar(water_percentage)
        elif 0 <= water_percentage <= 10:
            print("WARNING! WARNING! WARNING!")
            print("Current water level is extremely low!")
            print("Water percentage:", f"{water_percentage:.2f}" + "%")
            progress_bar(water_percentage)
            print("Actions are recommended.")
        else:
            print("Current Water level is high")
            print("Water percentage:", f"{water_percentage:.2f}" + "%")
            progress_bar(water_percentage)

        print("Days left before water level reaches 0 liters: ", round(days_left), "days.\n")

    #Kashif
    elif sect==3:
        print("\nTo calculate the amount of rainwater collected please enter the required information: ")

        runoff_coeficient = 0.85
        roof_area = float(input("Enter the roof area of your house in sqm : "))
        rainfall = float(input("enter the amount of rainfall in mm:"))
        collected_rainwater = roof_area * rainfall * runoff_coeficient

        print(f"The amount of rainfall collected in your household is: {collected_rainwater}L ")
        if collected_rainwater + watlvl > tankcap:
          print("ALERT! ALERT! TOO MUCH WATER COLLECTED! YOUR TANK IS OVERFLOWING! ")
        elif collected_rainwater + watlvl > (tankcap * 0.9):
          print(f"Watch out! Your tank has reached {watlvl + collected_rainwater} L. Make sure you tank doesnt overflow.")
        else:
          print(f"Your water level has increased by {collected_rainwater} L and is now {watlvl + collected_rainwater} L")
    #Asyraf
    elif sect==4:
        print("=== CONSERVATION MODE ACTIVATED ===")
        if dlyconsump == 0:
            print("No consumption recorded. Nothing to conserve.")
        else:
            day_left = watlvl / dlyconsump
        if day_left <= 3:
            status = "critical"
            saving_rate = 0.6
        elif day_left <=7:
            status = "warning"
            saving_rate = 0.4
        elif day_left <=10:
            status = "moderate"
            saving_rate = 0.2
        else:
            status = "safe"
            saving_rate = 0

        saving_perc = saving_rate * 100
        water_save = dlyconsump * saving_rate
        after_saving = dlyconsump - water_save
        new_day_left = watlvl / after_saving
        extra_day = new_day_left - day_left
        average = after_saving / res

        print("Status               :",status)
        print("Days left (normal)   :",day_left,"days")
        print(f"Saving target        : {saving_perc:.0f}%")
        print(f"Water saved          : {water_save:.2f} L/day")
        print(f"Usage after saving   : {after_saving:.2f} L/day")
        print(f"Days left (conserve) : {new_day_left:.2f} days")
        print(f"Extra days gained    : {extra_day:.2f} days")
        print(f"Usage per resident   : {average:.2f} L/day")

    #Someone
    elif sect==5:
        print("num5")
    elif sect==6:
        print("\nTerminating program.")
    else:
        print("\nInvalid input.")
        print("Try again.")
        print("")