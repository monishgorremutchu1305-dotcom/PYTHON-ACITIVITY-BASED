distance = float(input("Enter distance in km: "))
passengers = int(input("Enter number of passengers: "))
travel_class = input("Enter class (sleeper/ac): ").lower()

age = int(input("Enter passenger age: "))

if distance < 0 or passengers <= 0:
    print("Invalid input")
else:
    if travel_class == "sleeper":
        rate = 2
    elif travel_class == "ac":
        rate = 4
    else:
        rate = 0

    if rate == 0:
        print("Invalid travel class")
    else:
        fare = distance * rate

        if age >= 60:
            fare = fare * 0.80

        total = (fare + 50) * passengers

        print("Total railway fare: Rs.", total)