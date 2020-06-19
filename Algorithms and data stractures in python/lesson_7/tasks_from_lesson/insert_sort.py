from random import shuffle

size = 10
array = [i for i in range(size)]
shuffle(array)
print(array)

def insert_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j-1] > spam and j != 0:
            array[j] = array[j-1]
            j -= 1
        array[j] = spam
        print(array)
insert_sort(array)
print(array)