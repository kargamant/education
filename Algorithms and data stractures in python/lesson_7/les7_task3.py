from random import randint
from collections import deque

#Генерация массива
m = int(input('Введите m для вычисления длины массива:\n'))
array = [randint(0, 100) for _ in range(2*m+1)]
print(array, len(array), sep='\n')

def sort_by_median(array):
    #Вычисление медианы
    mid = array[len(array)//2 + len(array)%2-1]
    #Очередь в данном случае удобна и экономит большое количество памяти
    result = deque([mid])
    #Удаляем медиану из начального списка, чтобы она не добавлялась повторно в одну из частей
    array.remove(mid)
    #Пробегаемся по массиву ,сортируя, добавляя элементы в очередь(за время O(n)).
    for i in range(len(array)):
        if array[i] <= mid:
            result.appendleft(array[i])
        elif array[i] >= mid:
            result.append(array[i])
    print(mid)
    return result
print(sort_by_median(array))
