import random
import time
import scripts.Loader as Loader

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
print("[3]Credits")
print("")
print("[4]Beenden") 

aktion = input("> ") 

if "1" in aktion:
    Loader.Load()

elif "2" in aktion:
    pass

elif "3" in aktion:
    pass

elif "4" in aktion:
    exit
