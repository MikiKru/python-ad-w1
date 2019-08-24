#P48
# try:
#     print("NIEPARZYSTA" if int(input("Podaj liczbę: ")) % 2 else "PARZYSTA")
# except:
#     print("TO NIE JEST LICZBA")

#P49
# login = input("podaj login:")
# password = input("podaj password:")

# login, hasło, uprawnienia, aktywacja
# users = [ ["mk","mk123","ROLE_ADMIN",True],
#           ["kk", "kk123", "ROLE_USER", True],
#           ["ll", "ll123", "ROLE_USER", True]]

# LOGOWANIE NA PODSTAWIE LISTY UŻTRKOWNIKÓW
# isLogged = False
# for user in users:
#     if(login == user[0] and password == user[1]):
#         isLogged = True
#         if(user[2] == "ROLE_ADMIN"):
#             print("PANEL ADMINISTRATORA")
#             break
#         else:
#             print("PANEL UŻYTKOWNIKA")
#             break
# print("" if isLogged else "BŁĄD LOGOWANIA")

# login, hasło, uprawnienia, aktywacja
users = [ ["mk","mk123","ROLE_ADMIN",True],
          ["kk", "kk123", "ROLE_USER", True],
          ["ll", "ll123", "ROLE_USER", True]]

login = input("podaj login:")

isLogged = False
for user in users:
    # spr. czy jest taki użytkownik
    if(login == user[0] and user[3] == True):
        password = input("podaj password:")
        # spr. czy ma poprawne hasło
        if(password == user[1]):
            isLogged = True
            # sprawdzam uprawnienia
            if (user[2] == "ROLE_ADMIN"):
                print("PANEL ADMINISTRATORA")
                break
            else:
                print("PANEL UŻYTKOWNIKA")
                break
        else:
            print("BŁĘDNE HASŁO")
    elif(login == user[0] and user[3] == False):
        print("KONTO ZABLOKOWANE!")

print("" if isLogged else "BŁĄD LOGOWANIA")




