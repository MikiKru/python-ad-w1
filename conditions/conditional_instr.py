#P48
# try:
#     print("NIEPARZYSTA" if int(input("Podaj liczbę: ")) % 2 else "PARZYSTA")
# except:
#     print("TO NIE JEST LICZBA")

#P49
login = input("podaj login:")
password = input("podaj password:")

if(login == "admin" and password == "admin"):
    print("PANEL ADMINISTRATORA")
elif (login == "user" and password == "user"):
    print("PANEL UŻYTKOWNIKA")
else:
    print("BŁĄD LOGOWANIA")