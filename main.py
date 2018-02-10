import random
import time
import sys

#Start
print("***************************"); time.sleep(0.5)
print("*                         *"); time.sleep(0.5)
print("*       A R A D O R       *"); time.sleep(0.5)
print("*                         *"); time.sleep(0.5)
print("***************************"); time.sleep(0.5)

print("[1]Start")
print("")
print("[2]Laden")
print("")
print("[3]Creditss")
print("")
print("[4]Beenden") 

aktion = input("> ") 

if "1" in aktion:
    import A.py

elif "2" in aktion:
    import B.py

elif "3" in aktion:
    import C.py

elif "4" in aktion:
    exit