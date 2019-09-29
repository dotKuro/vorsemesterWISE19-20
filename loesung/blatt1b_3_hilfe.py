# Wir beginnen unsere Suche mit Char_code 0
char_code = 0

# Am Anfang ist unser Code natürlich noch in der Range
in_range = True

# Versuche ein Zeichen aus dem Char_Code zu generien. Bei einem Value Error
# sind wir außerhalb der Range. Das ist der gesuchte kleinste Charcode, der
# außerhalb der Range liegt.
# (Das wir nach einem ValueError suchen konnte man mit chr(-1) rausfinden.)
while in_range:
    try:
        chr(char_code)
        char_code += 1
    except ValueError:
        in_range = False

# Speichere denn Wert in eine konstante den wir in unserem Programm benutzten
# können.
CHAR_CODE_COUNT = char_code
