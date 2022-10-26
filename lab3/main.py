from dataclasses import dataclass, asdict, astuple
import csv
import os.path

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

city = []
country = []
street = []

def read(names):
    results = []
    with open(f'{names}.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
        print(results)
    print('---------------')

def create(number, object, obj, names):
    id = int(input('Id: '))
    name = str(input('Название: '))
    if(number == 2 or number == 3):
        file_exists = os.path.isfile(f'{names}.csv')
        id_city = int(input('Id города: '))
        object.append(obj(id, name, id_city))
        with open(f'{names}.csv', 'a+', newline='') as csvfile:
            fieldnames = ['Id', 'Name', 'Id_City']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Id':id, 'Name':name, 'Id_City':id_city})
    else:
        file_exists = os.path.isfile(f'{names}.csv')
        object.append(obj(id, name))
        with open(f'{names}.csv', 'a+', newline='') as csvfile:
            fieldnames = ['Id', 'Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Id':id, 'Name':name})

def edit(number, object, names):
    read(names)
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
def delete(object):
    for g in range(len(object)):
        print(f'{g}. - {asdict(object[g])}')
    selectListObject = int(input(f'Выберете элемент для удаления.\n'))
    if selectListObject >= 0 and selectListObject < len(object):
        object.pop(selectListObject)
    else:
        print('Такого элемента нет')

exit = 0
while(not exit):
    start = int(input(f'Возможности:\n'
    '1 - Вывести данные\n'
    '2 - Создать объект\n'
    '3 - Изменить объект\n'
    '4 - Удалить объект\n'
    '5 - Выход\n'))
    if start == 1:
        readObject = int(input(f'Вывести:\n'
        '1 - Города\n'
        '2 - Страны\n'
        '3 - Улицы\n'))
        if readObject == 1:
            read('cities')
        elif readObject == 2:
            read('countries')
        elif readObject == 3:
            read('streets')
    elif start == 2:
        createObject = int(input(f'Создать:\n'
        '1 - Город\n'
        '2 - Страну\n'
        '3 - Улицу\n'))
        if createObject == 1:
            create(createObject, city, City, 'cities')
        elif createObject == 2:
            create(createObject, country, Country, 'countries')
        elif createObject == 3:
            create(createObject, street, Street, 'streets')
    elif start == 3:
        editObject = int(input(f'Изменить:\n'
        '1 - Город\n'
        '2 - Страну\n'
        '3 - Улицу\n'))
        if editObject == 1:
            edit(editObject, city, 'cities')
        elif editObject == 2:
            edit(editObject, country, 'countries')
        elif editObject == 3:
            edit(editObject, street, 'streets')
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
        exit = 1