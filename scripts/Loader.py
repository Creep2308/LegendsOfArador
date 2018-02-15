def Load():
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
	    return(1)
	elif "2" in aktion:
	    return(2)
	elif "3" in aktion:
	    return(3)
	else:
		print("Wrong input")
	
	# 3 Spieldateien für jede Klasse 
