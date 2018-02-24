import os
import scripts.EscapeSeq as EscapeSeq
from time import sleep
from pathlib import Path

def load():
    EscapeSeq.Escape()
    #Remove the Placeholder if it exists
    if Path("data/characters/GitPlaceholder").is_file():
        os.remove("data/characters/GitPlaceholder")
    
    print("***************************\n"); sleep(0.25)
    print("Choose your Character: \n"); sleep(0.25)
    print("***************************"); sleep(0.25)

    dir = os.listdir("data/characters/")

    #Print the content of the directory
    for i in range(len(dir)):
        print("["+str(i+1)+"]"+str(dir[i]))
    while 1:
        aktion = input("> ")
        try:
            print(ReadCharData(dir[int(aktion)]) if aktion == "0" else ReadCharData(dir[int(aktion)-1]))
        except Exception as e:
            print("Something went wrong: "+str(e))
            print("Reloading!")
            sleep(0.75)
            load()


def ReadCharData(para_name):
    with open("data/characters/"+para_name, "r") as r:
        x = r.read()
    x.split("\n")
    return x