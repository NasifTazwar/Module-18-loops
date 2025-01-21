print("Select your ride: ")
print("1. Bike")
print("2. Car")

ride_choice = int(input("Enter your choice: "))

if ride_choice == 1:  
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")
    
    bike_choice = int(input("Enter your choice: "))
    if bike_choice == 1:
        print("You have selected a Scooty.")
    else:
        print("You have selected a Scooter.")
        
elif ride_choice == 2:  
    print("What type of car?")
    print("1. Sedan")
    print("2. SUV")
    
    car_choice = int(input("Enter your choice: "))
    if car_choice == 1:
        print("You have selected a Sedan.")
    else:
        print("You have selected an SUV.")
        
else:
    print("Invalid choice. Please select either 1 or 2.")

