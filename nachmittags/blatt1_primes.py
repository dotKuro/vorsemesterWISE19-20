correctNumber = False

while not correctNumber:
    try:
        userNumber = int(input("Geb mir eine Zahl:\n"))
        correctNumber = True
    except ValueError:
        print("Gib das nächste Mal bitte eine Zahl ein.")

if userNumber > 1:
    for number in range(2, userNumber):
        isPrim = True
        for smallerNumber in range(2, number):
            if(number % smallerNumber == 0):
                isPrim = False
        # Hier wissen wir dann ob number prim ist oder nicht
        if isPrim:
            print(number)
else:
    print("Es gibt keine Primzahlen bis {}.".format(userNumber))
