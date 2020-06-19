#from random import shuffle

#size = 10
#array = [i for i in range(size)]
#shuffle(array)
#print(array)

def b_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array)-n):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1
#b_sort(array)
#print(array)

