import datetime
import locale
import numpy as np
from datetime import datetime as dt

def recursion(arr: list, prev: int):
    if len(arr) == 1:
        return [arr]
    vals = []
    arr.remove(prev)
    for i in arr[len(arr) // 2:][::-1]:
        for j in recursion(arr[::-1], i):
            if prev ^ j[0] in [1, 2, 4]:
                vals.append([prev] + j)
    return vals

def cycle(cube: list, start: int):
    start = cube.index(start)
    idx = [0, 3, 5, 6, 7, 4, 2, 1]
    if start in idx[len(idx) // 2:]:
        idx = idx[::-1]
    rec = recursion(idx, start)
    for i in rec:
        if i[0] ^ i[-1] not in [1, 2, 4]:
            rec.remove(i)
    cycle = []
    for i in rec:
        cycle.append([cube[j] for j in i])
    cycle.sort()
    print('Гамильтоновы циклы для вершины графа - "1"')
    for i in cycle:
        print(cycle.index(i) +1, end=' ')
        print("-",i)
    return cycle

def get_ru(t: dt) -> str:
    loc = locale.getlocale()
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
    val = t.strftime("%B")
    locale.setlocale(locale.LC_ALL, loc)
    return val

def pprint64(value):
    printArray = np.unpackbits(np.frombuffer(value, dtype=np.uint8)).reshape((8, 8))
    print(*printArray, sep='\n')

def pprint128(value):
    printArray = np.unpackbits(np.frombuffer(value, dtype=np.uint8)).reshape((16, 8))
    print(*printArray, sep='\n')

print('ШАГ 1')
cube = np.array([[[7, 8], [5, 6]], [[1, 2], [3, 4]]])
graph = {
    '1' : [ '2','3','7' ],
    '2' : [ '1','4','8' ],
    '3' : [ '1','4','5' ],
    '4' : [ '2','3','6' ],
    '5' : [ '3','6','7' ],
    '6' : [ '4','5','8' ],
    '7' : [ '1','5','8' ],
    '8' : [ '2','6','7' ],
}
n = 8
matrix = [[0] * n for _ in range(n)]
for vertex_y, value in graph.items():
    for vertex_x in value:
        matrix[int(vertex_y) - 1][int(vertex_x) - 1] = 1

print('Матрица')
for row in matrix:
    print(row)

print('\n----------------\n')

hamiltonian_cycles = np.array(cycle(list(cube.flatten()), 1))

print(f'Количество Гамильтоновых циклов: {len(hamiltonian_cycles)}')
print('\n----------------\n')

day = dt.now().day
print(f"День месяца = {day}")

if day <= 11:
    print(f'{day}<=11, поэтому выбираем {day} и {day}+1')
    print(f'Выбраны {day} и {day + 1} элементы цикла')
    k1 = hamiltonian_cycles[day - 1]
    k2 = hamiltonian_cycles[day]
elif day == 12:
    print(f'{day}=12, поэтому выбираем {day} и {day}-11')
    print(f'Выбраны {day} и {day - 11} элементы цикла')
    k1 = hamiltonian_cycles[day - 1]
    k2 = hamiltonian_cycles[day - 12]
elif day >= 13:
    print(f'{day}>=13, поэтому выбираем {day}%12 и {day}%12+1')
    print(f'Выбраны {day % 12} и {day % 12 + 1} элементы цикла')
    k1 = hamiltonian_cycles[day % 12 - 1]
    k2 = hamiltonian_cycles[day % 12]

print(f'K1 = {k1}')
print(f'K2 = {k2}')
print('\n----------------\n')

print('ШАГ 2')
date_key = f'{dt.now().day:02d}{get_ru(dt.now())[:3]}{dt.now():0%y}'
date_key_bytes = date_key.encode("cp1251")
date_key_bits = np.unpackbits(np.frombuffer(date_key_bytes, dtype=np.uint8)).reshape((8, 8))
print(f'Дата = {date_key}')
for i in range(len(date_key_bytes)):
    print(f'{date_key[i]} = {date_key_bits[i]}')
print('\n----------------\n')

print('ШАГ 3')
date_key_bits[:] = date_key_bits[k1 - 1]
print(f'Перестановка по строкам с ключом K1 = {k1}')
print(*date_key_bits, sep='\n')

date_key_bits.T[:] = date_key_bits.T[k2 - 1]
print(f'Перестановка по столбцам с ключом K2 = {k2}')
print(*date_key_bits, sep='\n')

for i in range(len(date_key_bits) // 2):
    date_key_bits[i * 2] = np.roll(date_key_bits[i * 2], -3)
    date_key_bits[i * 2 + 1] = np.roll(date_key_bits[i * 2 + 1], 3)
print('Циклический сдвиг влево на 3 символа для нечётных номеров матрицы и сдвиг вправо на 3 символа для чётных')
print(*date_key_bits, sep='\n')
print('\n----------------\n')

print('ШАГ 4')
k1r = np.packbits(date_key_bits.reshape(8 * 8))
print(f'Ключ первого раунда K1r')
pprint64(k1r)
print()

borislav = 'Борислав'
borislav_key_bytes = borislav.encode("cp1251")
borislav_bits = np.unpackbits(np.frombuffer(borislav_key_bytes, dtype=np.uint8)).reshape((8, 8))
print(f'Первое имя = {borislav}')
for i in range(len(borislav_key_bytes)):
    print(f'{borislav[i]} = {borislav_bits[i]}')
print()
borislav_key_bits = np.frombuffer(borislav_key_bytes, dtype=np.uint8)
k2r = k1r ^ borislav_key_bits
print(f'Ключ второго раунда K2r = K1r XOR Борислав')
pprint64(k2r)
print()

antonina = 'Антонина'
antonina_key_bytes = antonina.encode("cp1251")
antonina_bits = np.unpackbits(np.frombuffer(antonina_key_bytes, dtype=np.uint8)).reshape((8, 8))
print(f'Второе имя = {antonina}')
for i in range(len(antonina_key_bytes)):
    print(f'{antonina[i]} = {antonina_bits[i]}')
print()
antonina_key_bits  = np.frombuffer(antonina_key_bytes, dtype=np.uint8)
k3r = k2r ^ antonina_key_bits
print(f'Ключ третьего раунда K3r = K2r XOR Антонина')
pprint64(k3r)

print('\n----------------\n')

print('ШАГ 5')
def feistel(left: np.ndarray, right: np.ndarray, key: np.ndarray, caesar: int = 5):
    swap = np.array([7, 4, 3, 6, 2, 1, 5, 8])
    subkey = right.copy()
    # Перестановка комбинированным шифром правой части
    subkey += caesar
    subkey[:] = subkey[swap - 1]
    # Сложение по модулю 2 ключа с результатом операций выше
    subkey[:] = subkey ^ key
    # Двойная перестановка комбинированным шифром правой части
    subkey += caesar
    subkey[:] = subkey[swap - 1]
    subkey += caesar
    subkey[:] = subkey[swap - 1]
    # Сложение по модулю 2 Левой части и subkey (результата функции шифрования)
    left[:] = subkey ^ left


variant = 'Информационность'
variant_key_bits = np.frombuffer(variant.encode("cp1251"), dtype=np.uint8)
print(f'Исходный текст для шифрования = {variant}')
print(f'len={len(variant_key_bits) * 8} bits')
print()
pprint128(variant_key_bits)
print()

print('ШИФРОВАНИЕ')
ciphertext = variant_key_bits.copy()
left = ciphertext[:8]
right = ciphertext[8:]

print(f'Левая часть: {bytes(left).decode("cp1251")}')
print(f'Правая часть: {bytes(right).decode("cp1251")}')
print()

feistel(left, right, k1r)
print(f'Ключ первого раунда K1r')
pprint64(k1r)
print(f'Результат первого раунда шифрования')
pprint128(ciphertext)
print()

feistel(right, left, k2r)
print(f'Ключ второго раунда K2r')
pprint64(k2r)
print(f'Результат второго раунда шифрования')
pprint128(ciphertext)
print()

feistel(left, right, k3r)
print(f'Ключ третьего раунда K3r')
pprint64(k3r)
print(f'Результат третьего раунда шифрования')
pprint128(ciphertext)
print()
print(f'Зашифрованный текст: {bytes(ciphertext).decode("cp1251")}')
print()

print('ДЕШИФРОВАНИЕ')
print()

feistel(left, right, k3r)
print(f'Ключ третьего раунда K3r')
pprint64(k3r)
print(f'Результат дешифрования с ключом третьего раунда')
pprint128(ciphertext)
print()

feistel(right, left, k2r)
print(f'Ключ второго раунда K2r')
pprint64(k2r)
print(f'Результат дешифрования с ключом второго раунда')
pprint128(ciphertext)
print()

feistel(left, right, k1r)
print(f'Ключ первого раунда K1r')
pprint64(k1r)
print(f'Результат дешифрования с ключом первого раунда')
pprint128(ciphertext)
print()

print(f'Дешифрованный текст: {bytes(ciphertext).decode("cp1251")}')