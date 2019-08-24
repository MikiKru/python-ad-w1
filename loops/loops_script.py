# WHILE ELSE
from random import randint, sample, choice

services = ["GitHub", "Google", "Facebook"]
servicesEmpty = []
i = 0
while i < len(servicesEmpty): # fragment kody wykonywany warunkowo
    print(servicesEmpty[i])
    i += 1
else:
    print("...") # fragment kody wykonywany zawsze

# FOR IN - OBLICZ ŚREDNIĄ ARYTMETYCZNĄ 1000 losowych wartości z przedziału od 1-10
suma = 0
for liczba in range(0,10000):
    suma += randint(1,10)
print(suma/10000)

# PRZYPISZ 12 osób do 4 grup - w każdej grupie wylosuj jednego lidera
osoby = set(["AN","TSz", "MP","ZJ","PM","AP","FŚ","MT","AR","IS","MS","MK"])
group_dict = {}
i = 1
while len(osoby) > 0:
    grupa = sample(osoby, 3)
    for osoba in grupa:
        group_dict[osoba] = str(i)
        osoby.discard(osoba)
    group_dict[choice(grupa)] = str(i)+"L"
    i += 1
print(group_dict)










