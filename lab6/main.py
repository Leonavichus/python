# Сортировка выбором
import math
import copy
from random import randint

# Сортировка векторов
def selection_sort(myListOfVectors, number):
    list = []
    # Расчет длинны вектора
    # if number == 2:
    #     for i in range(len(myListOfVectors)):
    #         for j in range(len(myListOfVectors[i]) - 1):
    #             list.append(math.sqrt(myListOfVectors[i][j] * myListOfVectors[i][j] + myListOfVectors[i][j+1] * myListOfVectors[i][j+1]))
    # elif number == 3:
    #     for i in range(len(myListOfVectors)):
    #         for j in range(len(myListOfVectors[i]) - 2):
    #             list.append(math.sqrt(myListOfVectors[i][j] * myListOfVectors[i][j] + myListOfVectors[i][j+1] * myListOfVectors[i][j+1] + myListOfVectors[i][j+2] * myListOfVectors[i][j+2]))

    # Сортировка выбором
    for i in range(0, len(myListOfVectors) - 1):
        smallest = i
        for j in range(i + 1, len(myListOfVectors)):
            if myListOfVectors[j] < myListOfVectors[smallest]:
                smallest = j
        myListOfVectors[i], myListOfVectors[smallest] = myListOfVectors[smallest], myListOfVectors[i]

# Ввод данных
n = int(input('Количество элементов = '))
category = int(input('Тип вектора = '))
myListOfVectors = []

# Создание списка векторов
for i in range(1, n + 1):
    if category == 2:
        x = randint(-10, 10)
        y = randint(-10, 10)
        myListOfVectors.append((x,y))
    elif category == 3:
        x = randint(-10, 10)
        y = randint(-10, 10)
        z = randint(-10, 10)
        myListOfVectors.append((x,y,z))

# Сортировка и вывод отсортированного списка векторов
myListOfVectors2 = copy.copy(myListOfVectors)
print(myListOfVectors)
selection_sort(myListOfVectors, category)
b = sorted(myListOfVectors2)
print(f'Ручная сортировка = {myListOfVectors}')
print(f'Сортировка библиотеки = {b}')
if(b == myListOfVectors):
    print('Совпадают!')