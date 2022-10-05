import math
import random
import string

P = pow(10, -5) # вероятность P подбора пароля злоумышленником
V = 10 # паролей в минуту (скорость перебора паролей злоумышленником)
T = 1 # неделя (срок действия)
Vt = V*60*24*7 # паролей в неделю
S1=(Vt*T)/P
power = string.ascii_letters + string.punctuation + string.octdigits
number = int(input('Мощность = '))
strPass = power[:number]
A = len(strPass)
L = 0
Al = pow(A, L)
while(S1>Al):
    L+=1
    Al = pow(A, L)
if(S1<Al):
    print(f'Нижняя граница S* = {int(S1)}')
    print(f'Длина пароля L = {L}')
password = ''
for i in range(L):
    password += random.choice(strPass)
print(f'Пароль = {password}')