import sys
import struct
import ctypes

'''Параметры системы: 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] win32'''
def store(*vars):
    sum = 0
    for item in vars:
        print(f'Тип: {item.__class__}\nРазмер: {sys.getsizeof(item)}\nЗначение: {item}\n')
        sum += sys.getsizeof(item)
    return f'Общий объём занимаемой памяти: {sum} байт'
'''
Тестирование функции:
a = 5
b = 125.88
c = 'Hello world!'
d = [1, 2, 3, 4]
e = {'1': 1, '2': 2, '3': 3, '4': 4}
print(store(a, b, c, d, e))
'''



