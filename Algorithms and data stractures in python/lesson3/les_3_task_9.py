'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
from random import randint

#Создание матрицы и списка с минимальными элементами столбцов
matrix = [[randint(0, 100) for _ in range(5)] for _ in range(5)]
min_coloumns = []
max = 0

#Вывод матрицы на экран
for line in matrix:
	for item in line:
		print(f'{item:>5}', end='')
	print()

#Поиск минимального элемента каждого столбца
for i in range(0, 5):
	min = line[i]
	for line in matrix:
		if line[i] < min:
			min = line[i]
	#Добавление минимального элемента в список
	min_coloumns.append(min)

#Поиск максимума в списке минимальных элементов
for item in min_coloumns:
	if item > max:
		max = item

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max}')