#P48
# try:
#     print("NIEPARZYSTA" if int(input("Podaj liczbę: ")) % 2 else "PARZYSTA")
# except:
#     print("TO NIE JEST LICZBA")

#P49
login = input("podaj login:")
password = input("podaj password:")

# login, hasło, uprawnienia, aktywacja
users = [ ["mk","mk123","ROLE_ADMIN",True],
          ["kk", "kk123", "ROLE_USER", True],
          ["ll", "ll123", "ROLE_USER", True]]

# LOGOWANIE NA PODSTAWIE LISTY UŻTRKOWNIKÓW
for user in users:
    if(login == user[0] and password == user[1]):
        if(user[2] == "ROLE_ADMIN"):
            print("PANEL ADMINISTRATORA")
            break
        else:
            print("PANEL UŻYTKOWNIKA")
            break
