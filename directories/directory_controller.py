from os import *

print("Direct path:", getcwd())
print("Zawartość aktualnego katalogu: ", listdir("."))
print("Zawartość aktualnego katalogu: ",
      listdir("D:\\Szkolenia\\Programowanie\\PWN\\DataAnalyst\\AD - Prezentacje\\3. Python"))

# zmiana katalogu
chdir("D:\\Szkolenia\\Programowanie\\PWN\\DataAnalyst\\AD - Prezentacje\\3. Python")
print(listdir("."))
# mkdir("generated from python")
# rmdir("generated from python")
for file in listdir("."):
    print("%50s \t %20.2f MB" % (file, path.getsize(file)/1000000))





