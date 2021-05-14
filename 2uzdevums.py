"""
    Funkcija akrs akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to kubu starpību un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, ievadot nepieciešamās
    vērtības un parādot skaitli ar pieciem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu kubu starpību
"""
 

pirmais=float(input("ievadi pirmo skaitli: "))
otrais=float(input("ievadi otro skaitli: "))
tresais=float(input("ievadi otro skaitli: "))
O=pirmais**3-otrais**3-tresais**3

answer = str(round(O, 5))

print(answer)