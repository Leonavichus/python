import random

subjects = ['Daniil', 'Ilya', 'Denis', 'Anna']
objcts = ['Fail1', 'Fail2','Fail3', 'Fail4', 'Fail5', 'Fail6']
access = ['read', 'write', 'grant']

class User:
    def __init__(self, subject, objects):
        self.subject = subject
        self.objects = objects

    def __str__(self):
        for i in range(len(objcts)):
            print(f'{objcts[i]} Доступ - {self.objects[objcts[i]]}')

def __main__():
    users = []
    for user in range(len(subjects)):
        objsub = {}
        for i in range(len(objcts)):
            objsub[objcts[i]] = {}
            for j in range(len(access) - 1):
                objsub[objcts[i]][access[j]] = random.randint(0, 1)  
        
        users.append(User(subjects[user], objsub))
    
    rand = random.randint(0, len(subjects) - 1)
    for i in range(len(objcts)):
        for j in range(len(access)):
            users[0].objects[objcts[i]][access[j]] = 1
        
    exit = 0
    while (not exit):
        start = int(input(f'Возможности:\n'
            '1 - Вход\n'
            '2 - Список субъектов\n'
            '3 - Выход\n'))
        if start == 1:
            subWrite = str(input(f'\nВведите имя субъекта\n'))
            if subWrite in subjects:
                for user in users:
                    if user.subject == subWrite:
                        userName = user
                        print(f'Успешный вход субъекта {userName.subject}')
                        quit = 0
                        while (not quit):
                            log = int(input(f'\nCубъект {userName.subject} выберите действие:\n'
                                '1 - Список файлов с доступами\n'
                                '2 - Чтение\n'
                                '3 - Передача прав на объект другому субъекту\n'
                                '4 - Запись/перезапись\n'
                                '5 - Забрать права у другого субъекта\n'
                                '6 - Выход\n'))
                            if log == 1:
                                userName.__str__()
                            elif log == 2:
                                readFile = str(input(f'Выберете файл.\n'))
                                if userName.objects.get(readFile):
                                    if userName.objects[readFile]['read'] == 1:
                                        print(f'Файл {readFile} успешно прочитан.')
                                    else:
                                        print(f'У вас недостаточно прав.')
                                else:
                                    print(f'Файла не существует.')
                            elif log == 3:
                                grandFile = str(
                                    input(f'Выберете файл.\n'))
                                if userName.objects.get(grandFile):
                                    if userName.objects[grandFile]['grant'] == 1:
                                        userAccess = str(input(f'Выберете право.\n'))
                                        for aces in userName.objects.get(grandFile).keys():
                                            if aces == userAccess:
                                                for g in range(len(subjects)):
                                                    print(f'{g}.{subjects[g]}')
                                                userGrant = int(input(f'Выберете субъекта(число).\n'))
                                                if userGrant >= 0 and userGrant < 4:
                                                    users[userGrant].objects[grandFile][userAccess] = 1
                                                    print(f'Право {userAccess} на файл {grandFile} успешно передано субъекту {users[userGrant].subject}')
                                                else:
                                                    print(f'Субъект выбран неверно.')
                                    else:
                                        print(f'У вас недостаточно прав.')
                                else:
                                    print(f'Файла не существует.')
                            elif log == 4:
                                writeFile = str(input(f'Выберете файл.\n'))
                                if userName.objects.get(writeFile):
                                    if userName.objects[writeFile]['write'] == 1:
                                        print(f'Файл {writeFile} успешно записан.')
                                    else:
                                        print(f'У вас недостаточно прав.')
                                else:
                                    print(f'Файла не существует.')
                            elif log == 5:
                                grandNotFile = str(
                                    input(f'Выберете файл.\n'))
                                if userName.objects.get(grandNotFile):
                                    if userName.objects[grandNotFile]['grant'] == 1:
                                        userAccess = str(input(f'Выберете право.\n'))
                                        for aces in userName.objects.get(grandNotFile).keys():
                                            if aces == userAccess:
                                                for g in range(len(subjects)):
                                                    print(f'{g}.{subjects[g]}')
                                                userGrant = int(input(f'Выберете файл субъекта(число).\n'))
                                                if userGrant >= 0 and userGrant < 4:
                                                    users[userGrant].objects[grandNotFile][userAccess] = 0
                                                    print(f'Право {userAccess} на файл {grandNotFile} успешно передано субъекту {users[userGrant].subject}')
                                                else:
                                                    print(f'Субъект выбран неверно.')
                                    else:
                                        print(f'У вас недостаточно прав.')
                                else:
                                    print(f'Файла не существует.')
                            elif log == 6:
                                quit = 1
                                print(f'Выход из систем.\n')
            else:
                print(f'Субъекта {subWrite} не существует.\n')
        elif start == 2:
            for i in range(len(subjects)):
                print(f'- {subjects[i]}')
        elif start == 3:
            exit = 1

if __name__ == '__main__':
    __main__()