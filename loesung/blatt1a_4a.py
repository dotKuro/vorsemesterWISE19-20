# Hier soll der User eine Chance bekommen eine Zahl zu errraten.

# Das hier ist die Zahl, die der User erraten soll. Hier bei handelt es sich um
# eine sogenannte Konstante. Das ist eine Variabele, dessen Wert konstant ist.
# Das heißt deren Wert sich nie verändert und sich auch nie verändern soll.
# Die Abmachung in Python ist, dass Konstanten komplett in Großbuchstaben mit
# Unterstrichen seperiert benannt werden sollen.
SECRET_NUMBER = 87


# Im folgenden Block wird eine Zahl vom User abgefragt. Hierbei ist für Python
# jede Abfrage vom User die wir mit input machen standartmäßig ein String, also
# ein Text und keine Zahl. Mit int können wir Python sagen, dass es sich bei
# dieser Eingabe um eine ganze Zahl handelt. Das kann jedoch zu Fehlern führen,
# da der User ja zum Beispiel trotzdem einfach Text eingeben kann. Das führt
# dann zu einem ValueError. Um das zuverhinden versuchen (try) wir diese Aktion
# auszuführen und falls sie mit einem ValueError abbricht (except ValueError)
# informieren wir den User stattdessen und beenden das Program frühzeitig.
try:
    # Das \n am Ende des Strings sorgt dafür, dass die Eingabe in der nächsten
    # Zeile gemacht wird.
    user_number = int(input("Errate meine Zahl zwischen 1 und 100!\n"))
except ValueError:
    print("Sorry, das ist ja nicht mal eine Zahl.")
    exit()


# Hier wird dann abgefragt, ob die Usereingabe mit der geheimen Zahl
# übereinstimmt und entsprechend eine Ausgabe erzeugt.
if user_number == SECRET_NUMBER:
    print("Richtig!")
else:
    print("Falsch!")
