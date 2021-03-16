#! /usr/bin/env python3

# In unserem Kalender sind zum Ausgleich der astronomischen und
# kalendarischen Jahreslänge in regelmäßigen Abständen Schaltjahre eingebaut.
#
# Zur exakten Festlegung der Schaltjahre dienen die folgenden Regeln:
#
# - Ist die Jahreszahl durch 4 teilbar, so ist das Jahr ein Schaltjahr. Diese Regel hat allerdings eine Ausnahme:
# - Ist die Jahreszahl durch 100 teilbar, so ist das Jahr kein Schaltjahr. Diese Ausnahme hat wiederum eine Ausnahme:
# - Ist die Jahreszahl durch 400 teilbar, so ist das Jahr doch ein Schaltjahr.
#
# Erstellen Sie ein Programm, das berechnet, ob eine vom Benutzer eingegebene Jahreszahl ein Schaltjahr bezeichnet oder nicht.

# Beispielsausgabe:

# Jahr: 2020
#
# Das Jahr 2020 ist ein Schaltjahr.

year = input("Jahr: ")

if int(year) % 4 == 0 :
    if int(year) % 100 == 0 and int(year) % 400 != 0:
        print("Das Jahr " + year + " ist kein Schaltjahr.")
    else:
        print("Das Jahr " + year + " ist ein Schaltjahr.")
else:
    print("Das Jahr %s ist kein Schaltjahr." % year)
