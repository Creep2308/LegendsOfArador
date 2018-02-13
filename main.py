print("***************************\n")
print("Wähle deine Klasse: \n")
print("***************************\n")

#Auswahl
print("[1]Krieger\n")
print("[2]Magier\n")
print("[3]Waldläufer\n")
print("***************************\n")

aktion = input("> ")

if "1" in aktion:
    from A1 import *

elif "2" in aktion:
    from A2 import *

elif "3" in aktion:
    from A3 import *

# 3 Spieldateien für jede Klasse 