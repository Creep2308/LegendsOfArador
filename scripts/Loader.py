import time
def Load():
	print("***************************\n"); time.sleep(0.25)
	print("Wähle deine Klasse: \n"); time.sleep(0.25)
	print("***************************\n"); time.sleep(0.25)
	
	#Auswahl
	print("[1]Krieger\n"); time.sleep(0.1)
	print("[2]Magier\n"); time.sleep(0.1)
	print("[3]Waldläufer\n"); time.sleep(0.1)
	print("***************************\n"); time.sleep(0.1)
	
<<<<<<< HEAD
	while(1):
		aktion = input("> ")
		if aktion == "1" or aktion == "2" or aktion == "3":
				return(aktion)
				break
		else:
			print("Something went wrong")

	# 3 Spieldateien für jede Klasse 
=======
	if "1" in aktion:
	    return(1)
	elif "2" in aktion:
	    return(2)
	elif "3" in aktion:
		return(3)
	else:
		print("Wrong input")
	
	# 3 Spieldateien für jede Klasse 
>>>>>>> 5511373d94b5d9a4840e55e5c1a813a23ea983ea
