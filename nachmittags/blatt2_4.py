
# blatt 2a.4

with open("zahl.txt", "r") as zahl_file:
    try:
        x = int(zahl_file.readline())
        y = int(zahl_file.readline())
    except ValueError:
        print("Ging gerade nicht.")
        exit()


# Schreibt x + y und x * y in die Ausgabe datei
with open("ausgabe.txt", "w") as ausgabe_file:
    ausgabe_file.write(str(x + y))
    ausgabe_file.write("\n")
    ausgabe_file.write(str(x * y))
