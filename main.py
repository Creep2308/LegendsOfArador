import random
import time
import scripts.Loader as Loader
import scripts.Credits as Creds

#Start
print("***************************"); time.sleep(0.25)
print("*                         *"); time.sleep(0.25)
print("*       A R A D O R       *"); time.sleep(0.25)
print("*                         *"); time.sleep(0.25)
print("***************************"); time.sleep(0.25)

print("[1]Start\n"); time.sleep(0.1)
print("[2]Laden\n"); time.sleep(0.1)
print("[3]Credits\n"); time.sleep(0.1)
print("[4]Beenden\n"); time.sleep(0.1)

aktion = input("> ") 

if "1" in aktion:
    print(Loader.Load())

elif "2" in aktion:
    pass

elif "3" in aktion:
    Creds.printCreds()

elif "4" in aktion:
    exit
