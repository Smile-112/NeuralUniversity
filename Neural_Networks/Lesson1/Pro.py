num = input("Введите целочисленное число от 1 до 9: ")
try:
    num = int(num)
except ValueError:
    print("Вы ввели не целочисленное число")
else:
    if (num > 9) or (num < 1): print("Вы ввели число не от 1 и до 9")
    print(f"{num} х 1 = {num}\n{num} х 2 = {num * 2}\n{num} х 3 = {num * 3}\n"
          f"{num} х 4 = {num * 4}\n{num} х 5 = {num * 5}\n{num} х 6 = {num * 6}\n"
          f"{num} х 7 = {num * 7}\n{num} х 8 = {num * 8}\n{num} х 9 = {num * 9}\n"
          f"{num} х 10 = {num * 10}\n")

print([i for i in range(300, 430) if (i % 11 == 0) and (i % 5 != 0)])

def vis(year: int):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0): print("Високосный")
    else: print("Обычный")


vis(2004)

print({n:n**2 for n in range(1,11)})

print(eval(input("Введите число а, математическую операцию и число b: ")))

lst = [96, 186, 11, 116, 183,  95, 181, 95, 55, 128, 54, 24, 21, 198, 118, 46, 166, 137, 24]

print(list(filter(lambda x: x%2==0,lst)))

# Если продолжить решение из колаба:
import os
os.chdir('/content')
os.mkdir(r"/content/my_folder")
[open(f"/content/my_folder/text_{i}.txt", "w") for i in range(1,11)]

arr = ["дом", "квартира", "поместье"]
print(list(map(lambda x: x[::-1], arr)))