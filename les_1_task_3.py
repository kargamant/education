#3. Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import uniform, randint

print('Введите диапазон случайного целого числа:')
b_int = int(input())
e_int = int(input())
print('Введите диапазон случайного вещественного числа:')
b_f = float(input())
e_f = float(input())
print('Введите диапазон случайного символа:')
b_l = input()
e_l = input()
print(f'Случайное целое число: {randint(b_int, e_int)}\n'
      f'Случайное вещественное число: {uniform(b_f, e_f)}\n'
      f'Случайный символ: {chr(randint(ord(b_l), ord(e_l)))}')