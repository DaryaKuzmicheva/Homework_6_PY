#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)



import random
n = int(input("Введите длину массива: "))
array = []
for x in range(n):
    array.append(random.randint(1, 20))
print(array)
size = len(array)
max = array[0]
min = array[0]
index = 0
minindex = 0
maxindex = 0
while index < size:
  if array[index] > max:
    max = array[index]
    maxindex = index
  if array[index] < min:
    min = array[index]
    minindex = index
  index = index + 1
print(f"Максимальный элемент массива = {max}")
print(f"Индекс максимального массива: {maxindex}")
print(f"Минимальный элемент массива = {min}")
print(f"Индекс минимального массива: {minindex}")
for i in range(len(array)):
  if min <= array[i] <= max:
     print(f"Индекс элемента min < max: {i}")