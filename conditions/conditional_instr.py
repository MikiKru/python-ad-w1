#P48
# try:
#     print("NIEPARZYSTA" if int(input("Podaj liczbę: ")) % 2 else "PARZYSTA")
# except:
#     print("TO NIE JEST LICZBA")

#P49
login = input("podaj login:")
password = input("podaj password:")

users = [ ["mk","mk123","ROLE_ADMIN",True],
          ["kk", "kk123", "ROLE_USER", True],
          ["ll", "ll123", "ROLE_USER", True]]


if(login == "admin" and password == "admin"):
    print("PANEL ADMINISTRATORA")
elif (login == "user" and password == "user"):
    print("PANEL UŻYTKOWNIKA")
else:
    print("BŁĄD LOGOWANIA")