# globalna wartość poza klasą
last_insert_index = 0

class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # inkrementacja globalnej wartości w skrypcie
        global last_insert_index
        last_insert_index += 1
        self.index_no = last_insert_index
        # pusta lista ocen
        self.grades = []

    def __str__(self):
        return "| %06d | %15s | %15s | %25s |" % \
               (self.index_no,self.name,self.lastname,self.grades)
print(Student("Test","Test"))