# In dieser Aufgabe wurde ein Zahlentrick beschrieben, in dem sich der gegenber
# eine einstellige Zahl aus denken soll. Dann soll die Person einige Rechnungen
# mit dier Zahl ausführen. Am Ende dieser Rechnungen soll die Zahl immer 5 sein.
# Hier soll ein Programm geschrieben werden, dass eine einstellige Zahl vom User
# abfragt und dann alle besagten Rechnungen ausführt und dann das Ergebniss
# (immer die 5) ausgibt.

correct_number = False

# Frag nach einer einstelligen Zahl bis ein korrekter Input erfasst wurde.
while not correct_number:
    try:
        user_number = int(input("Gib eine einstellige Zahl ein.\n"))
    except ValueError:
        print("Das war keine Zahl.")
        continue

    # Falls die Zahl zwischen 0 und 9 ist, ist sie einstellig.
    if user_number >= 0 and user_number <= 9:
        correct_number = True
    else:
        print("Diese Zahl war nicht einstellig.")

# Die Rechnungen mit der Zahl andwenden.
solution = (user_number + user_number + 10)/2 - user_number

# Die g-Formatierung für den Platzhalter sorgt dafür, dass bei einer Zahl nur
# relevante Stellen angezeigt werden. Durch das Teilen wird die ganze Zahl
# beim Zahlentrick zu einer Kommazahl umgewandelt. Wenn etwas schief gelaufen
# ist und nicht immer 5 rauskommt möchten wir das sehen (deswegen wandeln wir es
# nicht einfach in eine ganze Zahl um), wenn jedoch 5 rauskommt möchten wir
# nicht 5.0 angezeigt bekommen. Dementsprechend ist diese Formatierung genau
# richtig für uns.
print("Nach dem Zahlentrick ist die Zahl {:g}.".format(solution))
