from dataclasses import dataclass, asdict, astuple
import csv
import os.path

# Классы
@dataclass
class Country:
    id: int
    name: str
    id_city: int

@dataclass
class City:
    id: int
    name: str

@dataclass
class Street:
    id: int
    name: str
    id_city: int

# Массивы для хранения данных
city = []
country = []
street = []

# Чтение из файла
def readFile(names):
    with open(f'{names}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

# Завись в файл
def saveFile(names, object, number):
    if(number == 2 or number == 3):
        with open(f'{names}.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(object)
    else:
        with open(f'{names}.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(object)

# Чтение
def read(object):
    for element in object:
        print(asdict(element))
    print('---------------')

# Создание объекта класса
def create(number, object, obj):
    id = int(input('Id: '))
    name = str(input('Название: '))
    if(number == 2 or number == 3):
        id_city = int(input('Id города: '))
        object.append(obj(id, name, id_city))
    else:
        object.append(obj(id, name))

# Изменение объекта класса
def edit(number, object):
    for g in range(len(object)):
        print(f'{g}. - {asdict(object[g])}')
    selectListObject = int(input(f'Выберете элемент.\n'))
    if selectListObject >= 0 and selectListObject < len(object):
        if(number == 2 or number == 3):
            editValue = int(input(f'Изменить:\n'
            '1 - Id\n'
            '2 - Название\n'
            '3 - Id города\n'))
            if editValue == 1:
                value = int(input('Новое значение id: '))
                object[selectListObject].id = value
            elif editValue == 2:
                value = str(input('Новое значение названия: '))
                object[selectListObject].name = value
            elif editValue == 2:
                value = int(input('Новое значение id города: '))
                object[selectListObject].id_city = value
        else:
            editValue = int(input(f'Изменить:\n'
            '1 - Id\n'
            '2 - Название\n'))
            if editValue == 1:
                value = int(input('Новое значение id: '))
                object[selectListObject].id = value
            elif editValue == 2:
                value = str(input('Новое значение названия: '))
                object[selectListObject].name = value
    else:
        print('Такого элемента нет')

#Удаление объекта класса
def delete(object):
    for g in range(len(object)):
        print(f'{g}. - {asdict(object[g])}')
    selectListObject = int(input(f'Выберете элемент для удаления.\n'))
    if selectListObject >= 0 and selectListObject < len(object):
        object.pop(selectListObject)
    else:
        print('Такого элемента нет')


# Выборка действий
exit = 0
while(not exit):
    start = int(input(f'Возможности:\n'
    '1 - Вывести данные\n'
    '2 - Создать объект\n'
    '3 - Изменить объект\n'
    '4 - Удалить объект\n'
    '5 - Читать из файла\n'
    '6 - Сохранить в файл\n'
    '7 - Название страны  - список городов\n'
    '8 - Сколько в городе улиц\n'
    '9 - Выход\n'))
    if start == 1:
        readObject = int(input(f'Вывести:\n'
        '1 - Города\n'
        '2 - Страны\n'
        '3 - Улицы\n'))
        if readObject == 1:
            read(city)
        elif readObject == 2:
            read(country)
        elif readObject == 3:
            read(street)
    elif start == 2:
        createObject = int(input(f'Создать:\n'
        '1 - Город\n'
        '2 - Страну\n'
        '3 - Улицу\n'))
        if createObject == 1:
            create(createObject, city, City)
        elif createObject == 2:
            create(createObject, country, Country)
        elif createObject == 3:
            create(createObject, street, Street)
    elif start == 3:
        editObject = int(input(f'Изменить:\n'
        '1 - Город\n'
        '2 - Страну\n'
        '3 - Улицу\n'))
        if editObject == 1:
            edit(editObject, city)
        elif editObject == 2:
            edit(editObject, country)
        elif editObject == 3:
            edit(editObject, street)
    elif start == 4:
        deleteObject = int(input(f'Удалить:\n'
        '1 - Город\n'
        '2 - Страну\n'
        '3 - Улицу\n'))
        if deleteObject == 1:
            delete(city)
        elif deleteObject == 2:
            delete(country)
        elif deleteObject == 3:
            delete(street)
    elif start == 5:
        readFileSelect = int(input(f'Читать из файла:\n'
        '1 - Города\n'
        '2 - Страны\n'
        '3 - Улицы\n'))
        if readFileSelect == 1:
            readFile('cities')
        elif readFileSelect == 2:
            readFile('countries')
        elif readFileSelect == 3:
            readFile('streets')
    elif start == 6:
        saveObject = int(input(f'Сохранить:\n'
        '1 - Города\n'
        '2 - Страны\n'
        '3 - Улицы\n'))
        if saveObject == 1:
            saveFile('cities', city, saveObject)
        elif saveObject == 2:
            saveFile('countries', country, saveObject)
        elif saveObject == 3:
            saveFile('streets', street, saveObject)
    elif start == 7:
        for g in range(len(country)):
            print(f'{g}. - {country[g].name}')
            selectListObject = int(input(f'Выберете страну.\n'))
            for element in city:
                if(element.id == country[selectListObject].id_city):
                    print(element.name)
    elif start == 8:
        for g in range(len(city)):
            print(f'{g}. - {city[g].name}')
            selectListObject = int(input(f'Выберете город.\n'))
            for element in street:
                if(element.id_city == city[selectListObject].id):
                    print(f'Количество городов: {len(element.name)}')
    elif start == 9:
        exit = 1