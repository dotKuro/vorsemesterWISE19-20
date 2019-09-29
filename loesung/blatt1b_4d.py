# Hier sollen alle Zahlen von 1 bis 4 in jeder Kombination mit einander
# multipliziert und sinnvoll ausgegeben werden.


for factor1 in range(1, 5):
    for factor2 in range(1, 5):
        # Die Platzhalter werden von links nach rechts eingesetzt.
        print("{} * {} = {}".format(factor1, factor2, factor1*factor2))
