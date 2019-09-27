def frage_passwort():
    """ Das Passwort Abfrage programm, verbessert als Funktion"""
    SECRET_PASSWORD = "passwort1"

    triesLeft = 3
    correctPassword = False

    while triesLeft > 0 and not correctPassword:
        user_input = input("Geben Sie hier ihr Passwort ein:\n")
        if(user_input == SECRET_PASSWORD):
            print("Authentifizierung erfolgreich!")
            correctPassword = True
        else:
            triesLeft -= 1
            if triesLeft == 0:
                print("Zugriff verweigert!")
            elif triesLeft == 1:
                print("Du hast nur noch einen Versuch.")
            else:
                print("Du hast noch {} Versuche.".format(triesLeft))


if __name__ == "__main__":
    # Wird nicht beim impotieren ausgeführt
    frage_passwort()
