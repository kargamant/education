#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
#Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите количество элементов>>>'))
b1 = 1
q = -0.5
s = 0
for i in range(n):
	s += b1 * pow(q, i)
print(f'Сумма {n} элементов: {s}')