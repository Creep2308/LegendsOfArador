import time
import os
import scripts.EscapeSeq as EscapeSeq

def create():
	EscapeSeq.Escape()
	print("***************************\n"); time.sleep(0.25)
	print("Choose your Class: \n"); time.sleep(0.25)
	print("***************************\n"); time.sleep(0.25)
	
	#Auswahl
	print("[1]Warrior\n"); time.sleep(0.1)
	print("[2]Mage\n"); time.sleep(0.1)
	print("[3]Ranger\n"); time.sleep(0.1)
	print("***************************\n"); time.sleep(0.1)
	
	classes = ["Warrior", "Mage", "Ranger"]

	while(1):
		aktion = input("> ")
		if aktion == "1" or aktion == "2" or aktion == "3":
				CharClass = classes[int(aktion)-1]
				break
		else:
			print("Something went wrong")
	# 3 Spieldateien für jede Klasse 

	EscapeSeq.Escape() 
	print("***************************\n"); time.sleep(0.25)
	print("Choose your Race: \n"); time.sleep(0.25)
	print("***************************\n"); time.sleep(0.25)

	#Auswahl
	print("[1]Human\n"); time.sleep(0.1)
	print("[2]Dwarf\n"); time.sleep(0.1)
	print("[3]Floran\n"); time.sleep(0.1)
	print("[4]Goblin\n"); time.sleep(0.1)
	print("***************************\n"); time.sleep(0.1)
	
	race = ["Human", "Dwarf", "Floran", "Goblin"]

	while(1):
		aktion = input("> ")
		if aktion == "1" or aktion == "2" or aktion == "3" or aktion == "4":
				CharRace = race[int(aktion)-1]
				break
		else:
			print("Something went wrong")

	EscapeSeq.Escape() 
	print("***************************\n"); time.sleep(0.25)
	print("Choose your Gender: \n"); time.sleep(0.25)
	print("***************************\n"); time.sleep(0.25)

	#Auswahl
	print("[1]Male\n"); time.sleep(0.1)
	print("[2]Female\n"); time.sleep(0.1)
	print("***************************\n"); time.sleep(0.1)
	
	genders = ["Male", "Female"]

	while(1):
		aktion = input("> ")
		if aktion == "1" or aktion == "2":
				CharGender = genders[int(aktion)-1]
				break
		else:
			print("Something went wrong")

	createCharFile(CharClass, CharRace, CharGender)


def createCharFile(para_class, para_race, para_gender):
	name = input("Enter a name ")
	if checkName(name):
		with open("data/characters/"+name, "w") as f:
			f.write("Name: "+name+"\n")
			f.write("Class: "+para_class+"\n")
			f.write("Race: "+para_race+"\n")
			f.write("Gender: "+para_gender+"\n")
		print("\nCharacter creation successful.\nPress any key to continue")
		input()
	else:
		print("Already taken")
		createCharFile(para_class, para_race, para_gender)
	

def checkName(para_name):
	dir = os.listdir("data/characters/")
	for i in range(len(dir)):
		if para_name == dir[i]:
			return(False)
	return(True)