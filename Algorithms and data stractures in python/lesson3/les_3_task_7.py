'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''
from random import randint

#Инициализация переменных
nums = [randint(0, 100) for _ in range(0, 10)]
min_1 = 0
min_2 = 0

print(nums)

#Поиск первого минимума
for i in range(len(nums)):
    if nums[i] <= nums[min_1]:
        min_1 = i

#Удаление найденного минимума
#с его записью в переменную
ind = nums.pop(min_1)

#Поиск второго минимума
for i in range(len(nums)):
    if nums[i] <= nums[min_2]:
        min_2 = i

print(f'Два наименьших элемента массива: {ind} и {nums[min_2]}')