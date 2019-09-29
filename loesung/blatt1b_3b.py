# Hier soll nun ein Programm geschrieben werden, was die verschlüsselten Texte
# der vorherigen Aufgabe entschlüsseln kann. Hier zu wird empfohlen sich den
# vorherigen Code anzuschauen.

# Impotiere die Anzahl an verschiedenen Charcodes.
from blatt1b_3_hilfe import CHAR_CODE_COUNT

correct_key = False

while not correct_key:
    try:
        key = int(input("Was ist die Verschlüsselungszahl?\n"))
        correct_key = True
    except ValueError:
        print("Das war keine Zahl.")

encrypted_text = input("Welchen Text möchtest du entschlüsseln?\n")

# Hier wird das gleiche Verfahren wie davor benutzt, nur wird hier der Schlüssel
# abgezogen statt addiert.
decrypted_text = ""
for character in encrypted_text:
    character_code = ord(character)
    decrypted_code = chr((character_code - key) % CHAR_CODE_COUNT)
    decrypted_text += decrypted_code

print("Entschlüsselter Text:\n")
print(decrypted_text)
