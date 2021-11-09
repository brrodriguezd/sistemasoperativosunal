import os
import hashlib

os.chdir ('C:/Users/camil/Documents/Parcial1/Parcial1')

a = list()
names = list()
for entry in os.scandir():
    if (entry.name.endswith('.py') or entry.name.endswith('.txt')) and not entry.name.startswith('hash '):
        names.append(entry.name)
        with open(entry.name, 'r') as fp:
            a.append(fp.read())

for i in range (len(a)):
    m = hashlib.sha1()
    m.update(bytes(a[i], 'utf-8'))
    name = 'hash sha1 '+ str(names[i].split('.')[0]) + '.txt'
    with open(name, 'w') as fp:
        fp.write(str(m.hexdigest()))

os.chdir ('C:/Users/camil/Documents/Parcial1/Parcial1/Punto4')

a = list()
names = list()
for entry in os.scandir():
    if (entry.name.endswith('.py') or entry.name.endswith('.txt')) and not entry.name.startswith('hash '):
        names.append(entry.name)
        with open(entry.name, 'r') as fp:
            a.append(fp.read())

for i in range (len(a)):
    m = hashlib.sha1()
    m.update(bytes(a[i], 'utf-8'))
    name = 'hash sha1 '+ str(names[i].split('.')[0]) + '.txt'
    with open(name, 'w') as fp:
        fp.write(str(m.hexdigest()))

os.chdir ('C:/Users/camil/Documents/Parcial1/Parcial1/Buda')

a = list()
names = list()
for entry in os.scandir():
    if (entry.name.endswith('.py') or entry.name.endswith('.txt')) and not entry.name.startswith('hash '):
        names.append(entry.name)
        with open(entry.name, 'r') as fp:
            a.append(fp.read())

for i in range (len(a)):
    m = hashlib.sha1()
    m.update(bytes(a[i], 'utf-8'))
    name = 'hash sha1 '+ str(names[i].split('.')[0]) + '.txt'
    with open(name, 'w') as fp:
        fp.write(str(m.hexdigest()))