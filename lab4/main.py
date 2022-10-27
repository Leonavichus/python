from dataclasses import dataclass, asdict, astuple
import pickle
from collections import Counter

# Классы
@dataclass
class Post:
    id: int
    name: str

@dataclass
class Teacher:
    id: int
    fcs: str
    age: int
    id_department: int
    id_post: int

@dataclass
class Department:
    id: int
    name: str
    institute: str

# Массивы для заполнения
post = []
teacher = []
department = []
id_dep = []
depMas = []
depCount = []
ageMas = []
ageCount = []

# Заполенние массива
def add(file, object):
    with open(f"{file}.pickle", "rb") as f:
        while True:
            try:
                o = pickle.load(f)
            except EOFError:
                break
            else:
                object.append(o)

# Чтение из файла
def load_object(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                o = pickle.load(f)
            except EOFError:
                break
            else:
                print (o)

# Создание объекта класса
def create(number, obj, names):
    with open(f"{names}.pickle", "ab") as f:
        id = int(input('Id: '))
        name = str(input('Название: '))
        if(number == 2):
            age = int(input('Возвраст: '))
            id_department = int(input('Id кафедры: '))
            id_post = int(input('Id должности: '))
            # Запись объекта в файл
            pickle.dump(obj(id, name, age, id_department,id_post), f, protocol=pickle.HIGHEST_PROTOCOL)
        elif(number == 3):
            institute = str(input('Институт: '))
            # Запись объекта в файл
            pickle.dump(obj(id, name, institute), f, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            # Запись объекта в файл
            pickle.dump(obj(id, name), f, protocol=pickle.HIGHEST_PROTOCOL)

# Заполенние массивов
add('teacher', teacher)
add('department', department)
add('post', post)

exit = 0
while(not exit):
    start = int(input(f'Возможности:\n'
    '1 - Вывести данные\n'
    '2 - Создать объект\n'
    '3 - Кафедра, на которой работает больше всего сотрудников\n'
    '4 - Список кафедр в порядке убывания количества сотрудников\n'
    '5 - Самая молодая кафедра\n'
    '6 - Выход\n'))
    if start == 1:
        readObject = int(input(f'Вывести:\n'
        '1 - Должности\n'
        '2 - Преподаватели\n'
        '3 - Кафедры\n'))
        if readObject == 1:
            load_object("post.pickle")
        elif readObject == 2:
            load_object("teacher.pickle")
        elif readObject == 3:
            load_object("department.pickle")
    elif start == 2:
        createObject = int(input(f'Создать:\n'
        '1 - Должности\n'
        '2 - Преподаватели\n'
        '3 - Кафедры\n'))
        if createObject == 1:
            create(createObject, Post, 'post')
        elif createObject == 2:
            create(createObject, Teacher, 'teacher')
        elif createObject == 3:
            create(createObject, Department, 'department')
    elif start == 3:
        # Заполнение массива
        for g in range(len(teacher)):
            id_dep.append(teacher[g].id_department)
        # Поиск числа, которое повторяется больше всего
        maxId = max(a for a in id_dep if id_dep.count(a) == max(map(id_dep.count, id_dep)))
        for element in department:
            if(element.id == maxId):
                print(f'Кафедра с наибольшим количчеством сотрудников: {element.name}')
    elif start == 4:
        # Заполенние массива
        for g in range(len(teacher)):
            depCount.append(teacher[g].id_department)
        # Подсчет количества одинаковых элементов
        a = dict(Counter(depCount))
        # Заполенние массива
        for g in range(len(department)):
            depMas.append((department[g].id, department[g].name))
        # Преобразование в словарь
        myDict = {depMas[i][0]: depMas[i][1] for i in range(0, len(depMas), 1)}
        dictNew = []
        # Создание кортежа для сортировки (добавляем количество сотрудников и навзание кафедры)
        for i in range(1, len(myDict)+1):
            dictNew.append((myDict[i], a[i]))
        # Сортировка
        dictNew = sorted(dictNew, key=lambda tup: tup[1], reverse=True)
        print(dictNew)
    elif start == 5:
        # Заполенние массивов
        for g in range(len(teacher)):
            ageMas.append((teacher[g].id_department, teacher[g].age))
            ageCount.append(teacher[g].id_department)
        # Подсчет одинаковых элементов
        a = Counter(ageCount)
        c = Counter()
        # Создание словаря из списка складывая значения в одинаковых ключах
        [c.update({k: int(v)}) for k,v in ageMas]
        # Деление значений двух словарей
        b = dict((k, float(c[k])/a[k]) for k in c)
        # Получение минимального возраста
        minId = min(b, key=b.get)
        for element in department:
            if(element.id == minId):
                print(f'Самая молодая кафедра: {element.name}')
    elif start == 6:
        exit = 1