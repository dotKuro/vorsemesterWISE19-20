# Hier soll nun ein Text durch Verschiebung der Buchstaben mit Hilfe der
# internen Zeichenrepresentation verschlüsselt werden. Und zwar wird eine Zahl,
# der Schlüssel, vom User abgefragt. Anschließend wird ein beliebiger Text
# vom User abgefragt. Nun wird der Text verschlüsselt, indem jeder Buchstabe um
# den Schlüssel verschoben wird. Wird das letzte Zeichen um 1 verschoben, so
# soll das erste Zeichen enstehen.

# Importiere die Anzahl an verschiedenen Charcodes.
from blatt1b_3_hilfe import CHAR_CODE_COUNT

correct_key = False

while not correct_key:
    try:
        key = int(input("Was ist die Verschlüsselungszahl?\n"))
        correct_key = True
    except ValueError:
        print("Das war keine Zahl.")

input_text = input("Welchen Text möchtest du verschlüsseln?\n")

# Am Anfang starten wir mit einem leeren Text und werden nun jedes Zeichen
# verschlüsseln und der verschlüsselten Nachricht hinzufügen.
encrypted_text = ""
for character in input_text:
    character_code = ord(character)
    # Der Modoluoperator (%) ist so viel wie der Rest beim ganzzahiligen Teilen.
    # Er wird für uns den Umbruch vom Ende der Tabelle zum Anfang der Tabelle
    # übernehmen. Warum das funktioniert probierst du am besten selbst auf einem
    # Stück Papier aus.
    encrypted_code = (character_code + key) % CHAR_CODE_COUNT
    encrypted_text += chr(encrypted_code)

print("Verschlüsselter Text:\n")
print(encrypted_text)
