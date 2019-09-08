from homework.global_values import last_insert_index

class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # odwołanie do globalnej wartości w skrypcie
        global last_insert_index
        last_insert_index += 1
        self.index_no = last_insert_index
        # pusta lista ocen
        self.grades = []
    def calculateAvg(self):
        sum = 0
        for grade in self.grades:
            sum += grade
        if(len(self.grades) == 0):
            return 0
        return sum/len(self.grades)
    def __str__(self):
        return "| %06d | %15s | %15s | %25s | %5s |" % \
               (self.index_no,self.name,self.lastname,self.grades,
                "B/D" if self.calculateAvg() == 0. else self.calculateAvg())
