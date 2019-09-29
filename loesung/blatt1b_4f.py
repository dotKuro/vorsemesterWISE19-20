# Hier soll vom User zwei Zahlen abgefragt werden und eine
# Multiplikationstabelle damit erstellt werden.

# Impotiere den 10er Logarithmus aus der Matherweiterung.
from math import log10

correct_width = False

while not correct_width:
    try:
        width = int(input("Wie viele Spalten soll die Tabelle haben?\n"))
    except ValueError:
        print("Das war keine gültige Spaltenzahl.")
        continue

    if width > 0:
        correct_width = True
    else:
        print("Die Spaltenanzahl muss größer als 0 sein.")


correct_height = False

while not correct_height:
    try:
        height = int(input("Wie viele Zeilen soll die Tabelle haben?\n"))
    except ValueError:
        print("Das war keine gültige Zeilenzahl.")
        continue

    if height > 0:
        correct_height = True
    else:
        print("Die Zeilenanzahl muss größer als 0 sein.")

# Für ein gutes Tabellenformat müssen wir wissen wie viele Stellen die Zahlen
# in der Tabelle maximal haben. Multiplizieren wir 2 Zahlen a und b, so hat
# diese Zahl maximal so viele Stellen wie die Stellen von a + b addiert.

# Der 10er Logarithmus hilft uns die Anzahl von Stellen einer Zahl zu bestimmen.
# Achtung! Das funktioniert nicht für die Zahl 0. Da wir jedoch keine 0 zulasen
# ist das in Ordnung.
width_bits_count = int(log10(width)) + 1
height_bits_count = int(log10(height)) + 1

# Die erste Spalte brauch nur so breit sein, dass die ursprünglichen Zahlen
# reinpassen. Alle anderen Spalten müssen auch die Ergebnisse fassen können,
# sind deswegen also breiter.

first_column_width = height_bits_count
column_width = width_bits_count + height_bits_count

# Zuerst muss die Kopfzeile geschrieben werden.

# Erstelle eine leere Zellle oben links.
print(" " * first_column_width, end="||")
# Für jede Zahl in der Breite wird nun eine Zelle erstellt.
# Mit spezellem Pythonformatierung wird wieder dafür gesorgt, dass die Zelle
# die richtige Breite hat. Bei zu kleinen Zahlen wird links mit Leerzeichen
# gefüllt.
for number in range(1, width + 1):
    print(
        "{:>{column_width}}"
        .format(number, column_width=column_width),
        end="|"
    )
print()
print("=" * ((first_column_width + 2) + (column_width+1)*width))

# Nun wird Zeile für Zeile die Tabelle erstellt.
for line_number in range(1, height+1):
    print(
        "{:>{column_width}}"
        .format(line_number, column_width=first_column_width),
        end="||"
    )
    for column_number in range(1, width+1):
        print(
            "{:>{column_width}}"
            .format(line_number*column_number, column_width=column_width),
            end="|"
        )
    print()
