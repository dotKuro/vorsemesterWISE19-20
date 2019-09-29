# Hier sollen alle ungerade Zahlen von 1 bis 100 ausgegeben werden. Einmal
# benutzen wir eine for Schleife und einmal eine while Schleife.

# Starte bei 1 und betrachte jede zweite Zahl bis 100
for odd_number in range(1, 100, 2):
    print(odd_number)

# Die selbe Logik gilt hier.
odd_number = 1
while odd_number < 100:
    print(odd_number)
    odd_number += 2
