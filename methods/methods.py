import datetime
from time import localtime, time, ctime

returnedValue = localtime()
print(returnedValue)



productNames = ["A","B","C"]
productPrice = [1.99,2.33,5.00]

# metoda przyjmująca agrumnty i nie zwracająca wartości
def printSequence(sequence):
    for element in sequence:
        print(element, end=" ")
    print()

printSequence(productNames)
printSequence(productPrice)
printSequence([1,3,4,5,6,7,8,9,5,3])

"""
1. Szukanie min i max [1,23] | 
2. a = |0-1|/|1-23| = a = |0 - 1| / |min - max|
3. b = 1 - 1/22 * 23 = b = 1 - (a * max)
4. y = a*x + b -> 1/22*x - 1/22 | min - max
"""
# def findMinimum(data):
#     return min(data)
#
# def findMaximum(data):
#     return max(data)

def findExtrema(data):
    return min(data), max(data)

def normalizeDataset(data, lowBorder=0, topBorder=1):
    normalizedData = []
    a = abs(lowBorder - topBorder) / abs(findExtrema(data)[0] - findExtrema(data)[1])
    b = topBorder - (a * findExtrema(data)[1])
    for element in data:
        # normalizacja liniowa aX + b
        normalizedData.append(a * element + b)
    return normalizedData
def printDataset(data):
    for element in data:
        print("%6.3f" % element, end= " ")
    print()
data = [1 ,23 ,4 ,2 , 4, 5, 4, 11] # do znormalizowania od 0 -> 1

printDataset(data)
printDataset(normalizeDataset(data))
printDataset(normalizeDataset(data, lowBorder = -1, topBorder = 1))

# Dowolna liczba argumentów
def gradesAvg(*grades):
    sum = 0
    for grade in grades:
        sum += grade
    return sum/len(grades)

print("Uczeń 1: " + str(gradesAvg(2,3,1,4,5,6)),
      "Uczeń 2: " + str(gradesAvg(4,5)),
      "Uczeń 3: " + str(gradesAvg(4,4,4,4)))


#P57
def factorial(n):
    result = 1
    if(n < 0):
        return "Error"
    if(n == 0):
        return 1
    for i in range(2,n+1):
        result *= i
    return result

print(factorial(4))
print(factorial(0))
print(factorial(-19))

# REKURENCYJNIE
def factorialRec(n):
    if(n == 1):
        return 1
    return n * factorialRec(n - 1)

def date_diff_in_microseconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.microseconds

t_start = datetime.datetime.now()
print(factorial(1000))
t_stop = datetime.datetime.now()
print("Factorial: " + str(date_diff_in_microseconds(t_stop, t_start)))

t_start = datetime.datetime.now()
print(factorialRec(800))
t_stop = datetime.datetime.now()
print("Factorial Rec: " + str(date_diff_in_microseconds(t_stop, t_start)))

# P58
# 1,1,2,3,5,8,....
def fibonacciSeries(n):
    fib = []
    sum = 0
    for index, value in enumerate(range(0,n+1)):
        if(index == 0):
            fib.append(0)
        elif(index == 1):
            fib.append(1)
        else:
            fib.append(fib[index - 1] + fib[index - 2])
        sum += fib[index]

    return fib, fib[n], sum

print(fibonacciSeries(15))

names = ["Ala","Ola","Ela"]
for i, name in enumerate(names):
    print(i, name)
# == # 
i = 0
for name in names:
    print(i, name)
    i += 1

