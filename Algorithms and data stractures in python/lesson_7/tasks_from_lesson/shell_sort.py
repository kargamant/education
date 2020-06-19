from random import shuffle

size = 10
array = [i for i in range(size)]
shuffle(array)
print(array)

def shell_sort(array):
    assert len(array) < 4000, 'Длина массива не должна превышать 4000'
    def incr(array):
        incr = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) < incr[-1]:
            incr.pop()
        while len(incr) > 0:
            yield incr.pop()
    for inc in incr(array):
        print(inc)
        for i in range(inc, len(array)):
            for k in range(i, inc-1, -inc):
                if array[k - inc] <= array[k]:
                    break
                array[k], array[k-inc] = array[k-inc], array[k]
                print(array)
shell_sort(array)
print(array)