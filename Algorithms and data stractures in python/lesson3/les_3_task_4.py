'''
4. Определить, какое число в массиве встречается чаще всего.
'''
from random import randint

#Инициализация переменных: начального списка и списка повторений чисел
nums = [randint(0, 10) for _ in range(0, 20)]
duplicates = []

print(nums)

#Основной цикл
for item in nums:
	s = 0
	for i in range(len(nums)):
		#Поиск повторений
		if item == nums[i]:
			s += 1
	duplicates.append(s)

for i in set(nums):
	print(f'Число {i} встречается {duplicates[nums.index(i)]} раз')
