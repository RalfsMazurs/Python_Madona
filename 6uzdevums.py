"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās vērtības starpības dubultu.

"""

skaitlis=int(input("ievadi skaitli: "))

O=skaitlis-17

if skaitlis < 17:
    print(O)
if skaitlis > 17:
    print(O*2)