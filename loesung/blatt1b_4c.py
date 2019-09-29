# Hier soll der User belibig viele Zahlen eingeben können und dann soll der
# Mittelwert ermittelt werden.

correct_input = False

while not correct_input:
    # Hier soll der User seine Zahlen Komma seperiert eingeben.
    # Die split Funktion wird den String automatisch an den Kommas teilen
    # und diese in eine Liste speichern.
    user_inputs = input("Gib beliebig viele Zahlen mit Komma seperiert ein.\n")
    user_inputs = user_inputs.split(",")
    try:
        # Auf diese Weise kann eine Liste erstellt werden indem eine Aktion
        # auf jedes Element einer anderen Liste angewandt wird.
        user_numbers = [int(number) for number in user_inputs]
        correct_input = True
    except ValueError:
        print("Das waren nicht nur Zahlen.")


# Die eingebaute sum Funktion kann die Summe aller Zahlen einer Liste berechnen.
# https://docs.python.org/3/library/functions.html#sum
input_sum = sum(user_numbers)
# Die eingebaute len Funktion kann die Länge einer Liste bestimmen.
# https://docs.python.org/3/library/functions.html#len
input_length = len(user_numbers)

print("Der Mittelwert dieser Zahlen ist {}.".format(input_sum/input_length))
