import random
from math import gcd

message = str(input('Введите строку: '))

prime = lambda x : [i for i in range(1,x) if [i%j for j in range(2,i//2)].count(0)==0]
MAX_PRIME = 1000
p = random.choice(prime(MAX_PRIME)[10:])
q = p
while (q == p):
    q = random.choice(prime(MAX_PRIME)[10:])
n = p*q
f = (q-1)*(p-1)
while True:
    i = random.randint(2, f-1)
    if gcd(i, f) == 1:
        e = i
        break

while (f*i+1)%e != 0:
    i+=1
d = (f*i+1)//e

print('Открытый ключ '+str(e)+', '+str(n))
print('Закрытый ключ '+str(d)+', '+str(n))


def encrypt(message, n, e):
    ciphertext = []
    for char in message:
        ciphertext.append((ord(char)**e) % n)
    return ciphertext

ciphertext = encrypt(message, n, e)
print(ciphertext)

def decrypt(ciphertext, d, n):
    message = []
    for char in ciphertext:
        message.append(chr((char**d)%n))
    return message

print(''.join(decrypt(ciphertext, d, n)))