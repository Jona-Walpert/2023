import re
import time
file = open("src.txt", "r") #with open wäre besser
#muster = [0-9]
loesung = 0
for line in file:
    firstnumber = None
    lastnumber= None
    for char in line:
        if char.isnumeric(): #vielleicht auch mit re.findall(\d) machbar?!
            if firstnumber == None: #also das die erste Zahl ist
                firstnumber=char
                lastnumber=char
            else:
                lastnumber=char #überschreiben der letzten zahl mit der richtigen
    print(firstnumber,lastnumber)  #Zeigt alle Zahlenpare an (Zu Testzwecken und kein Teil der Lösung)
    loesung = loesung + int(f'{firstnumber}{lastnumber}') #f string um Zahl n hintereinander zu reihen und nicht mathematisch zu addieren
print(loesung)
    
file.close() 

