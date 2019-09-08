import pymysql

class DatabaseConnector:
    def __init__(self):
        self.loginToDbServer("localhost","python_user","python123","python_db")
        self.selectFromUsers()
        self.inserIntoUsers(input("imie"),input("nazwisko"),input("data urodzenia"),
                            input("pensja"), input("płeć"))
        decision = input("Potwierdź (T/N): ")
        if(decision.upper() == "T"):
            # przeniesienie danych z bufora pamięci do DB
            self.connect.commit()
        else:
            # wycofanie wprowadzanych danych
            self.connect.rollback()
        self.selectFromUsers()
    def loginToDbServer(self, host, user_login, user_password, db_name):
        try:
            # globalny obiekt połącznia z db
            self.connect = pymysql.connect(host,user_login,user_password,db_name)
            self.coursor = self.connect.cursor()
            print("Ustanowiono połączenie z bazą danych")
        except:
            print("Błąd połączenia z bazą danych")
    def selectFromUsers(self):
        # zapytanie SQL
        sql_query = "SELECT * FROM users"
        # metoda wykonująca zapytanie
        self.coursor.execute(sql_query)
        # zwrócenie tabelki wynikowej
        print("| %3s | %15s | %15s | %15s | %19s | %4s |"
              % ("ID", "IMIĘ", "NAZWISKO", "DATA URODZENIA", "WYNAGRODZENIE NETTO", "PŁEC"))
        for user in self.coursor.fetchall():
            print("| %3d | %15s | %15s | %15s | %17.2fzł | %4s |"
                  % (user[0], user[1], user[2], user[3], user[4], user[5]))
    def inserIntoUsers(self, name, lastname, birthdate, salary, gender):
        self.coursor.execute("INSERT INTO users VALUES (default, %s, %s, %s, %s, %s)",
                             (name, lastname, birthdate, salary, gender))

DatabaseConnector()