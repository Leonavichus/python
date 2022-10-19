import re, uuid
import os, sys

mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
command = "lsblk --nodeps -no serial"
serial = os.popen(command).read().replace("\n","")

if(mac == '5c:3a:45:9d:d1:4f' and serial == '002014400AB5'):
    print(f'MAC-адрес сетевой карты: {mac}')
    print(f'Серийный номер раздела жесткого диска: {serial}')
else:
    print('ТРЕВОГА!!!!\nВЫХОД!!!')
    exit()