from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
hash = "SHA-256"

# генерация
def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()
   return public, private

# шифрование
def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

# расшифровка
def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

# Генерация ключей 
(publicKey, privateKey) = newkeys(1024)
# Ввод строки
message = str(input('Введите строку: '))
# Шифрование строки
encMessage = encrypt(message.encode(), publicKey)
# Вывод 
print("Строка: ", message)
print("Зашифрованная строка: ", encMessage)
# Расшифровка строки
decMessage = decrypt(encMessage, privateKey).decode()
# Вывод 
print("Расшифрованная строка: ", decMessage)