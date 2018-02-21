import time
import os

def create():
	print("***************************\n"); time.sleep(0.25)
	print("Wähle deine Klasse: \n"); time.sleep(0.25)
	print("***************************\n"); time.sleep(0.25)
	
	#Auswahl
	print("[1]Krieger\n"); time.sleep(0.1)
	print("[2]Magier\n"); time.sleep(0.1)
	print("[3]Waldläufer\n"); time.sleep(0.1)
	print("***************************\n"); time.sleep(0.1)
	
	races = ["Warrior", "Mage", "Ranger"]

	while(1):
		aktion = input("> ")
		if aktion == "1" or aktion == "2" or aktion == "3":
				createCharFile(races[int(aktion)-1])
		else:
			print("Something went wrong")
	# 3 Spieldateien für jede Klasse 

def createCharFile(race):
	name = input("Enter a name ")
	if checkName(name):
		with open("data/characters/"+name, "w") as f:
			f.write("Name: "+name+"\n")
			f.write("Race: "+race+"\n")
	else:
		print("Already taken")
		createCharFile(race)
	

def checkName(para_name):
	dir = os.listdir("data/characters/")
	for i in range(len(dir)):
		if para_name == dir[i]:
			return(False)
	return(True)