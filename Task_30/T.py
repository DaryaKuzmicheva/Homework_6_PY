#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

n = int(input("Введите длину массива: "))
x = int(input("Введите значение первого элемента массива: "))
d = int(input("Введите разность арифметической прогрессии (d): "))
array = []
for i in range(n):
    a = x + i * d
    array.append(a)
print(array)

