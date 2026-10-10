print("====================================================================")
print("")
print("                        H Y D R O X U S")
print("                           G U A R D")
print("")
print("====================================================================")
print("")
print("                            Welcome.")
print("")
print("")

#Getting data from User1

status = True
while status:
    res=int(input("\nEnter the number of residents: "))
    tankcap=float(input("Enter the maximum tank capacity (L): "))
    watlvl=float(input("Enter the current water level (L): "))
    dlyconsump=float(input("Enter the average daily consumption per day (L):"))
    print("")

    #Validating if the data is viable or not

    if tankcap<watlvl:
        print("====================================================================")
        print("")
        print("                         Invalid data.")
        print("      Water level cannot be higher than tank capacity.")
        print("                 Enter the data value again.")
        print("")
        print("====================================================================")
    else:
        status = False


sect=0

while sect!=6:
  print("====================================================================")
  print("")
  print("Residents           : ",res)
  print("Max tank capacity   : ",tankcap,"L")
  print("Current water level : ",watlvl,"L")
  print("Daily consumption   : ",dlyconsump,"L")
  print("")
  print("--------------------------------------------------------------------")
  print("")
  print("[1] Check water supply")
  print("[2] Analyse water consumption")
  print("[3] Check rainwater collection")
  print("[4] Activate conservation mode")
  print("[5] Future water simulation")
  print("[6] Exit")
  print("")
  sect=int(input("Enter the desired numbered Section : "))
  print("")
  print("====================================================================")
  print("")

#Section Function

  #Roza
  if sect==1:
    print("num1")

  #Azfar Hariz
  elif sect==2:
    water_used = tankcap - watlvl
    print("An amount of", round(water_used,2), "L has been used")

    days_left = watlvl / dlyconsump
    remaining_water_percentage = watlvl / tankcap * 100

    if 30 < remaining_water_percentage <= 50:
      print("Current Water level is moderate")
      print("Water percentage:", str(round(remaining_water_percentage,2)) + "%")
    elif 10 < remaining_water_percentage <= 30:
      print("Current Water level is low")
      print("Water percentage:", str(round(remaining_water_percentage,2)) + "%")
    elif 0 <= remaining_water_percentage <= 10:
      print("WARNING! WARNING! WARNING!")
      print("Current water level is extremely low!")
      print("Water percentage:", str(round(remaining_water_percentage,2)) + "%")
      print("Actions are recommended.")
    else:
      print("Current Water level is high")
      print("Water percentage:", str(round(remaining_water_percentage,2)) + "%")

    print("Days left before water level reaches 0 liters: ", round(days_left,2), "days.\n")

  #Kashif
  elif sect==3:
    print("num3")
  elif sect==4:
    print("num4")
  elif sect==5:
    print("num5")
  elif sect==6:
    print("Terminating program.")
  else:
    print("Invalid input.")
    print("Try again.")
    print("")