#CLI - command line interface
#GUI - graphical user interface
from homework.student_controller import StudentController
# utworzenie obiektu zawierającego metody obsługi dziekanatu
dziekanat = StudentController()

while(True):
    menu = input("APLIKACJA DZIEKANAT\n"
                 "(D)-dodaj nowego studenta\n(U)-usuń studenta\n(Z)-zaktualizuj oceny\n"
                 "(O)-wyczyść listę ocen studenta\n(W)-wypisz listę studentów\n(Q)-wyjdź z programu")
    if(menu.upper()=="D"):
        name = input("podaj imię")
        lastname = input("podaj nazwisko")
        dziekanat.addStudent(name,lastname)
    elif(menu.upper()=="U"):
        pass
    elif(menu.upper()=="Z"):
        pass
    elif(menu.upper()=="O"):
        pass
    elif(menu.upper()=="W"):
        print(dziekanat)
    elif(menu.upper()=="Q"):
        # przerwanie pętli while
        break
    else:
        print("Błędny wybór!")