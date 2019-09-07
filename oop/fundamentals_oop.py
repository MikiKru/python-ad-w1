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
    p


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
