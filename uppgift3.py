__author__ = 'Jonathan'
"""
Pseudokod
==========
Fråga efter resistans
Fråga efter spänning
Beräkna effekten
Presentera resultatet

"""

#Get input values
resistance = input("Ange resistansen i ohm! :")
voltage = input("Ange spänning i volt! :")

#Check (for debug)
print("Resistansen = {0}, spänningen = {1}".format(resistance, voltage))

#Calc power
try:
    power = (float(voltage) ** 2 / float(resistance))
except:
    print("Det gick inte att utföra beräkningen")
    exit(-1)

    #Present result
    print("Effekten = {0} W".format(power))