'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
from random import randint

#Инициализация переменных
nums = [randint(0, 100) for _ in range(0, 10)]
max = 0
min = 0
sum = 0

print(nums)

#Основной цикл
for i in range(len(nums)-1):
    #Поиск максимума и минимума совершается по индексам
    if nums[i] > nums[max]:
        max = i
    elif nums[i] < nums[min]:
        min = i

#Проверка для корректной работы функции range
if min > max:
    #Нахождение суммы
    for i in range(max+1, min):
        sum += nums[i]
elif max > min:
    for i in range(min+1, max):
        sum += nums[i]
else:
    sum = 0

print(f'Сумма элементов между максимальным {nums[max]} и минимальным {nums[min]} : {sum}')