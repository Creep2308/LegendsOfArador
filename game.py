my_file = open('data/.dat', 'w')
savegame_daten = ['']

for line in savegame_daten:
    my_file.write(line + '\n') # \n = neue Zeile

my_file.close()
