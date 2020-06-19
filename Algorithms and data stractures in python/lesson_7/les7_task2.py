from random import uniform

array = [round(uniform(0, 50), 2) for _ in range(10)]
print(array)

def merge_sort(array):
    #базовый случай - массив с 1 элементом
    if len(array) < 2:
        return array
    #Деление массива на левую и правую части до базового случая
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    #Принт для детального наблюдения за процессом изменения частей
    #print(left, right, sep=';')
    #функция слияния
    def merge(left, right):
        #Результирующий массив
        sorted_array = []
        #Длины массивов и индексы
        r_len = len(right)
        l_len = len(left)
        l = 0
        r = 0
        #Сам процесс сортировки
        #Идём в цикле по изначальному массиву
        for _ in range(l_len + r_len):
            #Проверка на избежание ошибки индекса.
            #Ведь один из массивов может быть больше другого,
            #если изначально на вход был передан массив с нечётным количеством элементов
            if l < l_len and r < r_len:
                if left[l] <= right[r]:
                    #Добавляем меньший элемент в результирующий массив
                    sorted_array.append(left[l])
                    #Переход на следующий индекс, к следующему элементу  в меньшем массиве
                    l += 1
                else:
                    sorted_array.append(right[r])
                    r += 1
            #Если все элементы левого списка уже проверены,
            #то добавляем в результирующий массив все оставшиеся элементы правого массива.
            elif l == l_len:
                sorted_array.append(right[r])
                r += 1
            elif r == r_len:
                sorted_array.append(left[l])
                l += 1
        #Возвращаем отсортированный массив, который сохраняется в одну из переменных left или right,
        #которые будут применены в следующем повторении рекурсии
        return sorted_array
    #Рекурсивный случай
    return merge(left, right)
print(merge_sort(array))
