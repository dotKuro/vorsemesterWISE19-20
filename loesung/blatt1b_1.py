# In dieser Aufgabe soll der User nach der aktuellen Temperatur und
# Windgeschwindigkeit gefragt werden. Dann soll die gefühlt Temperatur nach der
# alten und der neuen Rechnungsweise berechnet werden. Auch hier wieder der
# Hinweis: Konzepte der vorherigen Aufgaben werden hier eventuell nicht mehr
# erklärt. Wenn du etwas nicht verstehst überfliegt die vorherigen Aufgaben.
# Die Formeln zur Berechnung sind auf dem Aufgabenblatt zu finden.
# (vorkurs.cs.uni-frankfurt.de)
#
# Anders in der Aufgabenstellung gefordert, möchte ich dem User die Möglichkeit
# geben Kommazahlen einzugeben.

# Importiere die Wurzel Funktion aus der Matheerweiterung
from math import sqrt

correct_temperatur = False
# Solange keine korrekte Temperatur vorliegt, frage dannach.
while not correct_temperatur:
    try:
        # float ist der Datentyp für Kommazahlen.
        # Es wird probiert aus der Usereingabe ein Kommazahl zu machen.
        # Python erwartet hierbei eine Zahl im englischen Format.
        # (Mit . als ,)
        # Wenn wir die Kommas die der User eingibt durch Punkte ersetzen so
        # können wir sowohl das deutsche als auch das englische Format
        # unterstützen.
        # Beim Programmieren ist es wichtig auf die Sprachgewohnheiten der
        # User zu achten.
        user_tempratur = float(
            input("Gib die aktuelle Temperatur in Grad Celcius an.\n")
            .replace(",", ".")
        )
        # Dieser Code wird nur erreicht, wenn die Temperatureingabe valide war.
        correct_temperatur = True
    except ValueError:
        print("Das war keine gültige Temperatur.")

correct_wind_velocity = False
# Solange keine korrekte Temperatur vorliegt, frage dannach.
while not correct_wind_velocity:
    try:
        user_wind_velocity = float(
            input("Gib die aktuelle Windgeschwindigkiet in km/h ein.\n")
            .replace(",", ".")
        )
    except ValueError:
        print("Das war keine gültige Windgeschwindigkeit.")
        continue

    if user_wind_velocity < 0:
        print("Windgeschwindigkeiten können nur positiv sein.")
    else:
        correct_wind_velocity = True


# Wenn eine Rechnung zu lange für eine Zeile ist so kann man sie einmal komplett
# klammern, damit man sie in mehrere Zeilen aufteilen kann.
windchill_temprature_old = (
    33 +
    (
        0.478 +
        (0.237 * sqrt(user_wind_velocity)) -
        (0.0124 * user_wind_velocity)
    ) * (user_tempratur - 33)
)
windchill_temprature_new = (
    13.12 +
    (0.6215 * user_tempratur) -
    (11.37 * user_wind_velocity**0.16) +
    (0.3965 * user_tempratur * user_wind_velocity**0.16)
)


# In den Platzhaltern können wir auch Informationen einbauen, wie Zahlen
# formatiert werden sollen. Diese Formatierungen werden immer mit einem
# Doppelpunkt eingeleitet. .3f bedeutet, dass immer genau 3 Nachkomma stellen
# angezeigt werden sollen.
# https://docs.python.org/3/library/string.html#format-specification-mini-language
print(
    "Die gefühlte Temperatur nach dem alten Verfahren ist {:.3f} Grad Celcius"
    .format(windchill_temprature_old)
)
print(
    "Die gefühlte Temperatur nach dem neuen Verfahren ist {:.3f} Grad Celcius"
    .format(windchill_temprature_new)
)
