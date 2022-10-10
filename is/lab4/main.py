import rsa
import pybase64

# Генерация ключей 
(publicKey, privateKey) = rsa.newkeys(1024)
# Ввод строки
message = str(input('Введите строку: '))
# Шифрование строки
encMessage = rsa.encrypt(message.encode(), publicKey)
# Вывод 
print("Строка: ", message)
print("Зашифрованная строка: ", encMessage)
# Расшифровка строки
decMessage = rsa.decrypt(encMessage, privateKey).decode()
# Вывод 
print("Расшифрованная строка: ", decMessage)

# Генерация ключей и сохранение
pub = publicKey.save_pkcs1()
with open('public.pem', 'wb') as pubfile:
    pubfile.write(pub)
    pubfile.close()

pri = privateKey.save_pkcs1()
with open('private.pem', 'wb') as prifile:
    prifile.write(pri)
    prifile.close()

# Загрузка ключей
with open('public.pem') as publickfile:
    p = publickfile.read()
    publicKey = rsa.PublicKey.load_pkcs1(p)

with open('private.pem') as privatefile:
    p = privatefile.read()
    privateKey = rsa.PrivateKey.load_pkcs1(p)
