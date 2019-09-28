# Hier soll der User eine natürliche Zahl eingeben, solange bis er eine gültige
# Eingabe gemacht hat. Die Zahlen 1, 2, 3 und 5 sollen verdoppelt ausgegeben
# werden, die Zahlen 4, 6 und 7 sollen vervierfacht ausgegeben werden. Alle
# restlichen Zahlen sollen einfach ausgegeben werden. Auch hier gebe ich wieder
# die Empfehlung die Kommentare der vorherigen Aufgaben zu überfliegen, da
# bereits erklärte Konzepte nicht unbedingt wiederholt werden.


correct_input = False

while not correct_input:
    try:
        user_number = int(input("Sag mir eine natürliche Zahl!\n"))
    except ValueError:
        print("Das war keine Zahl!")
        continue

    # Der User kann auch negative Zahlen eingeben. Das sollen wir nicht
    # zulassen.
    if user_number < 0:
        print("Natürliche Zahlen sind positive, ganze Zahlen.")
    else:
        correct_input = True

# In diesem Fall sollen die Zahlen verdoppelt werden.
if user_number in [1, 2, 3, 5]:
    user_number = user_number * 2
# In diesem Fall sollen Zahlen vervierfacht werden.
elif user_number in [4, 6, 7]:
    user_number = user_number * 4

# Als letztes soll die Zahl ausgegeben werden.
print(user_number)
