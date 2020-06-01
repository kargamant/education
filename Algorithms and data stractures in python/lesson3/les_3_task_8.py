'''
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
'''
#Создание матрицы
matrix = [[int(input('Введите элемент матрицы: ')) for _ in range(0, 4)] for _ in range(0, 4)]
sum_line = 0

#Нахождение суммы элементов строки матрицы
for line in matrix:
	sum_line = 0
	for item in line:
		sum_line += item
	#Добавление суммы в конец строки
	line.append(sum_line)

#Вывод матрицы на экран
for line in matrix:
	for item in line:
		print(f'{item:>5}', end='')
	print()