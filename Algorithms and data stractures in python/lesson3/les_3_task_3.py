'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
from random import randint

#Инициализация основного списка и
# переменных со значениями индексов максимального и минимального элементов
nums = [randint(0, 100) for _ in range(0, 10)]
max = 0
min = 0

print(nums)

#Основной цикл
for i in range(len(nums)):
	#Нахождение максимума
	if nums[i] > nums[max]:
		max = i
	#Нахождение минимума
	elif nums[i] < nums[min]:
		min = i

#Независимый обмен значений
nums[max], nums[min] = nums[min], nums[max]

print(f'Максимальный({nums[min]}) и минимальный({nums[max]}) элементы поменялись местами:\n {nums}')