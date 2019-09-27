SECRET_PASSWORD = "passwort1"
correct_password = False
tries_left = 3

while not correct_password and tries_left > 0:
    user_input = input("Geben Sie ihr Passwort ein.\n")
    if(SECRET_PASSWORD == user_input):
        print("Authentifizierung erfolgreich!")
        correct_password = True
    else:
        print("Falsches Passwort")
        tries_left -= 1
        print("Du hast noch {} Versuche.".format(tries_left))

    if(tries_left == 0):
        print("Zugriff verweigert!")
