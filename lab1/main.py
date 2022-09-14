# Класс
class Math:
    # Конструктор
    # self — это ссылка на создаваемый в памяти компьютера объект
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # Возвращает строковое представление объекта
    def __str__(self):
        return f"Число a = {self.a}, число b = {self.b}, число c = {self.c}, число d = {self.d}"

    # Деструктор
    def __del__(self):
        del self.a
        del self.b
        del self.c
        del self.d
        print('Объект уничтожен')

    # Функция для вычисления среднего арифмитического числа
    def get_arithmetic_mean(self):
        arithmetic_mean = (self.a+self.b+self.c+self.d) / 4
        return f"\nСреднее арифмитическое = {arithmetic_mean}"

    # Функция для поиска максимального числа
    def get_maximum(self):
        maximum = max(self.a,self.b,self.c,self.d)
        return f"\nМаксимальное число = {maximum}"

# Ввод переменных
a = float(input("Введите число a: ") or 0)
b = float(input("Введите число b: ") or 0)
c = float(input("Введите число c: ") or 0)
d = float(input("Введите число d: ") or 0)

# Создание объекта
math = Math(a,b,c,d)

# Вывод данных
print(math,math.get_arithmetic_mean(),math.get_maximum())

# Уничтожение объекта
del math