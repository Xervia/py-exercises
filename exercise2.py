#! /usr/bin/env python3

# Geben Sie eine Pyramide durch Ausdruck entsprechend vieler Leerzeichen und Blöcke (`#`) auf dem Bildschirm aus.
# Die Höhe der Pyramide soll durch eine Eingabe vom User bestimmt werden.
# Bedenken Sie auch falsche Eingaben.

# Beispielsausgabe:

# Height: 8

       #
      ###
     #####
    #######
   #########
  ###########
 #############
###############

height = input("Height: ")
output = "#"
for i in reversed(range(0, int(height))):
    spaces = ""
    for _ in range (0, i):
        spaces += " "
    print(spaces + output)
    output += "##"
