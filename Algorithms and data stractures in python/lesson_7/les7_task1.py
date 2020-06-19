from random import randint

#генерация массива
array = [randint(-100, 100) for _ in range(10)]
print(array)

#Рекурсивная сортировка пузырьком
def bsort_rec(array):
    n = 1
    #Вложенная функция
    def _bubble_sort(array, n):
        #Базовый случай
        if n == len(array):
            return array
        #Сама сортировка
        for i in range(len(array)-n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        #Рекурсивный случай
        return _bubble_sort(array, n+1)
    return _bubble_sort(array, n)

#Сортировка пузырьком с использованием мемоизации через временную переменную
def bsort(array):
    #Счётчик
    count = 0
    #Сортировка
    for n in range(1, len(array)):
        #Сохранение значения массива во временную переменную
        spam = array.copy()
        for i in range(len(array)-n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            count += 1
        #Проверка
        #Если значение временной переменной совпало со значением массива после очередного вложенного цикла,
        #то массив отсортирован, и нету смысла проходить последующие циклы пока n не станет равной длине списка.
        #Таким образом среднее количество итераций снижается с константного 45 до 35-42(в худшем случае 44).
        if spam == array:
            print(count)
            return
#print(bsort_rec(array))
bsort(array)
print(array)
