print("====================================================================")
print("\n                        H Y D R O X U S")
print("                           G U A R D")
print("\n====================================================================")
print("\n                            Welcome.")

# Getting data from user

flag = True
while flag:
    try:
        res = int(input("\nEnter the number of residents: "))
        tankcap = float(input("Enter the maximum tank capacity (L): "))
        watlvl = float(input("Enter the current water level (L): "))
        dly = float(input("Enter the average daily consumption per day (L): "))

        # Validating if the data is viable or not
        if res <= 0:
            print("\n====================================================================")
            print("\n                         Invalid data.")
            print("       Number of residents must be greater than zero.")
            print("                  Enter the data value again.")
            print("\n====================================================================")
        elif tankcap <= 0:
            print("\n====================================================================")
            print("\n                         Invalid data.")
            print("       Tank capacity must be greater than zero.")
            print("                  Enter the data value again.")
            print("\n====================================================================")
        elif watlvl < 0:
            print("\n====================================================================")
            print("\n                         Invalid data.")
            print("       Water level cannot be less than zero.")
            print("                  Enter the data value again.")
            print("\n====================================================================")
        elif tankcap < watlvl:
            print("\n====================================================================")
            print("\n                         Invalid data.")
            print("       Water level cannot be higher than tank capacity.")
            print("                  Enter the data value again.")
            print("\n====================================================================")
        elif dly < 0:
            print("\n====================================================================")
            print("\n                         Invalid data.")
            print("       Daily consumption cannot be negative.")
            print("                  Enter the data value again.")
            print("\n====================================================================")
        else:
            flag = False

    except ValueError:
        print("\n====================================================================")
        print("\n                           Invalid data.")
        print("                        Enter a valid number.")
        print("\n====================================================================")


sect = 0

while sect != 6:
    print("\n====================================================================")
    print("\nResidents           : ", res)
    print("Max tank capacity   : ", tankcap, "L")
    print("Current water level : ", watlvl, "L")
    print("Daily consumption   : ", dly, "L")
    print("\n--------------------------------------------------------------------")
    print("\n[1] Update system parameters")
    print("[2] Analyse water consumption")
    print("[3] Check rainwater collection")
    print("[4] Conservation mode")
    print("[5] Environmental risk simulation")
    print("[6] Exit")

    try:
        sect = int(input("\nEnter the desired numbered Section : "))
    except ValueError:
        print("\nInvalid input.")
        print("Try again.\n")
        continue

    print("\n====================================================================")

    # Section Function

    # Roza
    if sect == 1:
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
                dly = float(input("Enter the new average daily consumption per day (L): "))
                if dly >= 0:
                    break
                print("Error: Consumption cannot be negative. Try again.")
            except ValueError:
                print("Error: Please enter a valid number.")

        print("\n--------------------------------------------------------------------")
        print("\nAll parameters successfully updated and verified!")

    # Azfar Hariz
    elif sect == 2:
        print("\n                    WATER CONSUMPTION ANALYSIS")
        print("\n--------------------------------------------------------------------")

        water_used = tankcap - watlvl
        print("\nAn amount of", f"{water_used:.2f}", "L has been used")

        if dly > 0:
            day_left = watlvl / dly
        else:
            day_left = 0

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

        if dly > 0:
            print("Days left before water level reaches 0 liters: ", round(day_left), "days.\n")
        else:
            print("Days left before water level reaches 0 liters: Not available.\n")

    # Kashif
    elif sect == 3:
        print("\n                       RAINWATER COLLECTION")
        print("\n--------------------------------------------------------------------")
        print("\nTo calculate the amount of rainwater collected please enter the required information: \n")

        runoff_coef = 0.85
        roof_area = float(input("Enter the roof area of your house (sqm) : "))
        rain = float(input("Enter the amount of rainfall (mm) : "))
        rain_col = roof_area * rain * runoff_coef
        watlvl += rain_col

        print(f"\nThe amount of rainfall collected in your household is: {rain_col:.2f}L ")
        if rain_col + watlvl > tankcap:
            print("\nALERT! ALERT! TOO MUCH WATER COLLECTED! YOUR TANK IS OVERFLOWING! ")
        elif rain_col + watlvl > (tankcap * 0.9):
            print(f"\nWatch out! Your tank has reached {watlvl + rain_col:.2f} L. Make sure your tank doesn't overflow.")
        else:
            print(f"\nYour water level has increased by {rain_col:.2f} L and is now {watlvl + rain_col:.2f} L")

    # Asyraf
    elif sect == 4:
        print("\n                        CONSERVATION MODE ")
        print("\n--------------------------------------------------------------------")

        if dly == 0:
            print("\nNo consumption recorded. Nothing to conserve.")
            continue
        else:
            day_left = watlvl / dly

        if day_left <= 3:
            cstat = "critical"
            save_rate = 0.6
        elif day_left <= 7:
            cstat = "warning"
            save_rate = 0.4
        elif day_left <= 10:
            cstat = "moderate"
            save_rate = 0.2
        else:
            cstat = "safe"
            save_rate = 0

        save_perc = save_rate * 100
        water_save = dly * save_rate
        after_save = dly - water_save
        new_day_left = watlvl / after_save if after_save > 0 else 0
        extra_day = new_day_left - day_left
        avg = after_save / res if res > 0 else 0

        print("\nStatus               :", cstat)
        print("Days left (normal)   :", day_left, "days")
        print(f"\nSaving target        : {save_perc:.0f}%")
        print(f"Water saved          : {water_save:.2f} L/day")
        print(f"Usage after saving   : {after_save:.2f} L/day")
        print(f"Days left (conserve) : {new_day_left:.2f} days")
        print(f"Extra days gained    : {extra_day:.2f} days")
        print(f"Usage per resident   : {avg:.2f} L/day")

    # Hafizi
    elif sect == 5:
        print("\n                  ENVIRONMENTAL RISK SIMULATION")
        print("\n--------------------------------------------------------------------\n")

        sim = ["Prolonged Drought", "Tank Leakage", "Flood Contamination"]

        for i in range(3):
            print(f"[{i+1}] {sim[i]}")

        water_level = []

        while True:
            try:
                sim_choice = int(input("\nChoose desired simulation : "))
                if sim_choice == 1:
                    days = int(input("\nEnter simulation duration (Days) : "))
                    surf_area = float(input("Enter your tank's surface area (m²) : "))
                    evap_rate = float(input("Enter the average evaporation rate (mm): "))
                    dly_loss = dly + (surf_area * evap_rate)
                    start_water = watlvl
                    break

                elif sim_choice == 2:
                    days = int(input("\nEnter simulation duration (Days) : "))
                    leak = float(input("Enter daily leakage (L) : "))
                    dly_loss = dly + leak
                    start_water = watlvl
                    break

                elif sim_choice == 3:
                    days = int(input("\nEnter simulation duration (Days) : "))
                    cont = float(input("Enter contaminated water (L) : "))
                    dly_loss = dly
                    start_water = watlvl - cont
                    if 0 <= cont <= watlvl:
                        break
                    else:
                        print("\nInvalid input.")
                        print("Check back the entered data.\n")
                else:
                    print("\nInvalid input.")
                    print("Try again.\n")

            except ValueError:
                print("\nEnter a valid number.\n")
            except ZeroDivisionError:
                print("\nInvalid input.")
                print("Check back the entered data.\n")

        water_level.append(start_water)
        for i in range(days):
            start_water -= dly_loss
            if start_water < 0:
                water_level.append(0)
            else:
                water_level.append(start_water)

        print("\n------------------------------------------------")
        print("|- - Relative Day - - | - - Water Level (L) - -|")
        print("|---------------------|------------------------|")
        for day in range(0, days + 1):
            print(f"|{day:^21}|{water_level[day]:^24.1f}|")
        print("------------------------------------------------")

        print(f"\nUsable water after simulation : {water_level[day]:.1f}")

        if dly > 0:
            print(f"Days left after simulation    : {water_level[day] / dly}")
        else:
            print("Days left after simulation    : Not applicable")

        if water_level[day] <= 0:
            print("\nPlease take precautions.")

    elif sect == 6:
        print("\nTerminating program.\n")
    else:
        print("\nInvalid input.")
        print("Try again.\n")
