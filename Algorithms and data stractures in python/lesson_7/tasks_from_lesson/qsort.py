from random import shuffle, choice, randint

size = 10
array = [i for i in range(size)]
shuffle(array)
print(array)

def qsort(array):
    if len(array) <= 1:
        return array
    pivot = choice(array)
    less = []
    eq = []
    greater = []
    for i in array:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
        else:
            eq.append(i)
    return qsort(less) + eq + qsort(greater)

def qsort_no_memory(array, first, last):
    if last <= first:
        return
    pivot = array[randint(first, last)]
    i, j = first, last
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i+1, j-1
    qsort_no_memory(array, first, j)
    qsort_no_memory(array, i, last)
qsort_no_memory(array, 0, len(array)-1)
print(array)
