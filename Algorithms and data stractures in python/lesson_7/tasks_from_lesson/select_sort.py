from random import shuffle

size = 10
array = [i for i in range(size)]
shuffle(array)
print(array)

def select_sort(array):
    for i in range(len(array)):
        min = i
        for k in range(i+1, len(array)):
            if array[k] < array[min]:
                min = k
        array[i], array[min] = array[min], array[i]
select_sort(array)
print(array)