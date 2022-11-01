# Сортировка выбором
import math

# Сортировка векторов
def selection_sort(myListOfVectors, number):
    list = []
    # Расчет длинны вектора
    if number == 2:
        for i in range(len(myListOfVectors)):
            for j in range(len(myListOfVectors[i]) - 1):
                list.append(math.sqrt(myListOfVectors[i][j] * myListOfVectors[i][j] + myListOfVectors[i][j+1] * myListOfVectors[i][j+1]))
    elif number == 3:
        for i in range(len(myListOfVectors)):
            for j in range(len(myListOfVectors[i]) - 2):
                list.append(math.sqrt(myListOfVectors[i][j] * myListOfVectors[i][j] + myListOfVectors[i][j+1] * myListOfVectors[i][j+1] + myListOfVectors[i][j+2] * myListOfVectors[i][j+2]))

    # Сортировка выбором
    for i in range(0, len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]
        myListOfVectors[i], myListOfVectors[smallest] = myListOfVectors[smallest], myListOfVectors[i]

# Ввод данных
n = int(input('Количество элементов = '))
category = int(input('Тип вектора = '))
myListOfVectors = []

# Создание списка векторов
for i in range(1, n + 1):
    if category == 2:
        x = int(input(f'Введите x{i} = '))
        y = int(input(f'Введите y{i} = '))
        myListOfVectors.append((x,y))
    elif category == 3:
        x = int(input(f'Введите x{i} = '))
        y = int(input(f'Введите y{i} = '))
        z = int(input(f'Введите z{i} = '))
        myListOfVectors.append((x,y,z))

# Сортировка и вывод отсортированного списка векторов
selection_sort(myListOfVectors, category)
print(myListOfVectors)