# Hier soll Aufgabe 4a nun verbessert werden, indem der User mehr als nur einen
# Versuch bekommt. Hierbei sollen seine Versuche gezählt werden und ihm am Ende
# ausgegeben werden. Außerdem soll dem User ein nach jedem Versuch gesagt werden
# ob die zu erratene Zahl größer oder kleiner ist. Als eigene Verbesserung soll
# die geheim Zahl zusätzlich noch zufällig gewählt werden.
# Es wird empfohlen sich die vorherige Aufgabe zuerst anzuschauen, da
# Erklärungen von dort hier nicht nocheinaml wiederholt werden.

# Von der Pythonerweiterung für Zufall soll die Funktion randint importiert werden
from random import randint

# Eine zufällige ganze Zahl zwischen 1 und 100 inklusive der Grenzen soll
# gewählt werden.
# https://docs.python.org/3/library/random.html?highlight=random#random.randint
# Das hier ist jetzt keine Konstante, auch wenn sich der Wert nicht ändern, weil
# der Wert bei jeder Ausführung des Programmes ein anderer Wert ist. Userinput
# und zufällige Werte sind keine Konstanten.
secret_number = randint(1, 100)


# Diese Variable wird zählen wie viele Versuche der User bereits benutzt hat.
# Am Anfang ist dieser Wert 0.
tries = 0
# Diese Variable hält fest, ob der User bereits richtig geraten hat. Am Anfang
# ist das natürlich nicht der Fall, also ist diese Variable False.
guessed_correctly = False

# Dieser Block wird ausgeführt bis der User richtig geraten hat.
while not guessed_correctly:
    try:
        user_number = int(input("Rate meine Zahl zwischen 1 und 100!\n"))
    except ValueError:
        print("Bitte gebe eine Zahl ein.")
        # continue springt wieder an der Kopf der Schleife. Damit wird der
        # untere Code nur ausgeführt, wenn der User erfolgreich eine Zahl
        # eingegeben hat.
        continue

    # Die Anzahl der Versuche wird bei einer gültigen Eingabe erhöht.
    tries += 1

    if user_number == secret_number:
        # Der User hat eine korrekte Eingabe gemacht. Die Variable wird
        # aktualisiert, um die Schleife nach diesem Durchlauf anzuhalten.
        guessed_correctly = True
        # Sonderfall für einen Versuch, damit der Plural nicht für einen Versuch
        # verwendet wird.
        if tries == 1:
            print("Richtig, du hast nur ein Versuch gebraucht!")
        else:
            # {} ist ein Platzhalter der mit der .format() Funktion mit der
            # Anzahl der Versuche gefüllt wird.
            print("Richtig, du hast {} Versuche gebraucht.".format(tries))
    elif user_number < secret_number:
        print("Deine Zahl war zu klein.")
    # Else, also wenn user_number > secret_number
    else:
        print("Deine Zahl war zu groß.")
