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
    # metoda szukająca i zwracająca studenta
    def findStudentByIndex(self,index_no):
        for student in self.students:
            if(index_no == student.index_no):
                return student
        return None
    # metoda usuwająca studenta z listy
    def deleteStudentByIndex(self,index_no):
        deletedStudent = self.findStudentByIndex(index_no)
        if(deletedStudent != None):
            self.students.remove(deletedStudent)
            print("usunięto studenta " + deletedStudent.__str__())
        else:
            print("Nie ma takiego studenta")
    # dodawanie ocen do studenta
    def addGradesToStudent(self, index_no, new_grades):
        findStudent = self.findStudentByIndex(index_no)
        if(findStudent != None):
            findStudent.grades.extend(new_grades)
            print("zaktualizowano listę ocen studenta")
    def deleteStudentGrades(self, index_no):
        findStudent = self.findStudentByIndex(index_no)
        if (findStudent != None):
            findStudent.grades = []
            print("wyczyszczona lista ocen studenta")







