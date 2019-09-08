# Utworzenie pliku z uprawnieniami do zapisu
file = open("file1.txt", "w")
# Szczegóły pliku
print(file.name, file.closed, file.mode)
# Zapis do pliku
file.write("Pierwszy zapis do pliku\n")
file.write("Drugi zapis do pliku\n")
file.writelines(['s1\n','s2\n','s3\n','s4\n'])
file.close()
print(file.name, file.closed, file.mode)

fileAppend = open("file2.txt", "a")
fileAppend.writelines(['1','2','3','4','5','6','7','8\n'])
fileAppend.close()

# odczyt z pliku
fileReader = open("file2.txt", "r")
# print(fileReader.read())
print(fileReader.read(10))
# print(fileReader.readlines())

# sprawdzenie pozycji kursora
print(fileReader.tell())
print(fileReader.read(3))

# iterowanie po obiekcie pliku
for line in fileReader:
    print(line, end="")
fileReader.close()










