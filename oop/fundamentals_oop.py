# struktura - model danych
class Point3D:
    # konstruktor
    def __init__(self, x, y, z):
        # self.x - pole klasowe - dostępne dla wszystkich składowych klasy
        self.x = x
        self.y = y
        self.z = z
    # tekstowa reprezentacja obiektu
    def __str__(self):
        return "[x=%d,y=%d,z=%d]" % (self.x,self.y,self.z)

# obsługa żądań - kontroler
class Point3DController:
    # metoda do dodawania składowych dwóch pkt
    # zwracająca nowy punkt z sumą składowych
    def sumTwoPoints(self, p1, p2):
        # utworzenie obiektu klasy Point3D
        newPoint = Point3D(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)
        return newPoint
    def multiplyByValue(self, point, value):
        return Point3D(point.x * value, point.y * value, point.z * value)
    # metoda sumująca wszystkie składowe punktów znajdujące się w liście
    # metoda przyjmuje listę punktów jako argument
    # metoda zwraca obiekt klasy Poin3D
    def sumAllPoints(self, points):
        sumPoint = Point3D(0,0,0)
        # element listy to obiekt klasy Point3D
        for point in points:
            sumPoint.x += point.x
            sumPoint.y += point.y
            sumPoint.z += point.z
        return sumPoint
    # metoda wyszukująca punkt w liście po jego składowych
    # metoda zwraca wartość typu boolean
    def findPoint(self, points, x, y, z):
        findPoint = Point3D(x,y,z)
        for point in points:
            if(point.x == findPoint.x and point.y == findPoint.y and point.z == findPoint.z):
                return True
        return False
    
# utworzenie obiektu klasy
point1 = Point3D(0,0,0)
point2 = Point3D(5,5,5)
# odwołanie do pól klasowych
print("Point1",point1.x, point1.y, point1.z)
print("Point2",point2.x, point2.y, point2.z)
# modyfikacja pól klasowych
point1.x = 1
point1.y = point2.y - 1
print("Point1",point1.x, point1.y, point1.z)
print("Point2",point2.x, point2.y, point2.z)
# metoda do reprezentacji tekstowej obiektu - toString()
print(point1)
print(point2)
# metoda sumująca składowe obiektów klasy Point3D
pc = Point3DController()
pointSum1 = pc.sumTwoPoints(point1,point2)
print(pointSum1)
# pointSum2 = pc.sumTwoPoints(point2,point2)
# print(pointSum2)
# skalowania składowych punktu
print(pc.multiplyByValue(point1,2))
resultPoint = pc.multiplyByValue(Point3D(9,9,9),0.5)
print(resultPoint)
print(resultPoint.x, resultPoint.y, resultPoint.z)

points = [Point3D(1,1,1), Point3D(2,2,2), Point3D(3,2,1),Point3D(0,5,11)]
print(pc.sumAllPoints(points))