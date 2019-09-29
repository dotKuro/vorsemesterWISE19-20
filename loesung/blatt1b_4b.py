# Hier sollen 5 Zahlen abgefragt werden und dann soll der Mittelwert dieser
# Zahlen berechnet werden.

# Diese Variable wird benutzt um zu tracken, wie viele korrekte Zahlen wir
# bereits erhalten haben.
correct_input_count = 0
# Diese Variable ist die Summe der gesammelten Inputs
input_sum = 0

while correct_input_count < 5:
    try:
        input_number = int(
            input(
                "Gib mir eine ganze Zahl. ({}/5)\n"
                .format(correct_input_count + 1)
            )
        )
        input_sum += input_number
        correct_input_count += 1
    except ValueError:
        print("Das war keine ganze Zahl.")

print("Der Mittelwert deiner Zahlen ist {}.".format(input_sum/5))
