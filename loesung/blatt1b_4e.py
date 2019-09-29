# Hier sollen wieder alle Kombinationen von 1 bis zu einer bestimmten Zahl
# paarweise multipliziert werden. Hier soll jedoch die Obergrenze vom User
# abgefragt werden.

correct_input = False

while not correct_input:
    try:
        user_number = int(input("Gib eine positive Zahl ein.\n"))
    except ValueError:
        print("Das war keine Zahl.")
        continue

    if user_number > 0:
        correct_input = True
    else:
        print("Das war keine positive Zahl.")

for factor1 in range(1, user_number+1):
    for factor2 in range(1, user_number+1):
        print("{} * {} = {}".format(factor1, factor2, factor1*factor2))
