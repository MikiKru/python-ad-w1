from homework.student import Student


class StudentController:
    def __init__(self):
        self.students = []
    def __str__(self):
        output = ""
        for student in self.students:
            output += (student.__str__() + "\n")
        return output
    # metoda dodająca studenta do listy
    def addStudent(self, name, lastname):
        student = Student(name, lastname)
        self.students.append(student)

dziekanat = StudentController()
dziekanat.addStudent("test", "test")
dziekanat.addStudent("test", "test")
dziekanat.addStudent("test", "test")
print(dziekanat)
