class Math:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"Число a = {self.a}, число b = {self.b}, число c = {self.c}, число d = {self.d}"

    def __del__(self):
        del self.a
        del self.b
        del self.c
        del self.d
        print('Объект уничтожен')

    def get_arithmetic_mean(self):
        arithmetic_mean = (self.a+self.b+self.c+self.d) / 4
        return f"\nСреднее арифмитическое = {arithmetic_mean}"

    def get_maximum(self):
        maximum = max(self.a,self.b,self.c,self.d)
        return f"\nМаксимальное число = {maximum}"

a  = float(input("Введите число a: "))
b  = float(input("Введите число b: "))
c  = float(input("Введите число c: "))
d  = float(input("Введите число d: "))

math = Math(a,b,c,d)

print(math,math.get_arithmetic_mean(),math.get_maximum())

del math