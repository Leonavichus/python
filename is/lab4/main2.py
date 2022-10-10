from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os

def encrypt(dataFile, publicKeyFile):
    # считывание данных из файла
    with open(dataFile, 'rb') as f:
        data = f.read()
    
    # преобразование данных в байты
    data = bytes(data)

    # считывание открытого ключа из файла
    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()
    
    # создание объекта открытого ключа
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # шифрование сеансового ключа с помощью открытого ключа
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # шифрование данных с помощью сеансового ключа
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    []

    # сохранение зашифрованных данных в файл
    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
    print('Зашифрованный файл, сохраненный в ' + encryptedFile)
    

def decrypt(dataFile, privateKeyFile):
    # считывание закрытого ключа из файла
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # создать объект закрытого ключа
        key = RSA.import_key(privateKey)

    # считывание данных из файла
    with open(dataFile, 'rb') as f:
        # чтение сеансового ключа
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    # шифрование сеансового ключа
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # шифрование данных с помощью сеансового ключа
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # сохранение расшифрованных данных в файл
    [ fileName, fileExtension ] = dataFile.split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)

    print('Расшифрованный файл, сохраненный в ' + decryptedFile)

data = 'data.txt'
publicKeyFile = 'public.pem'
encrypt( data, publicKeyFile )
print('\n')

decryptFile = 'data_encrypted.txt'
privateKeyFile = 'private.pem'

decrypt(decryptFile, privateKeyFile)