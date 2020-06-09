#без использования решета эратосфена

def prime(el):
    n = el
    while True:
        p = 1
        for i in range(2, n):
            for k in range(2, i):
                if i%k == 0:
                    break
                if k == i-1 and i%k != 0:
                    p += 1
            if p == el:
                return i
        n += el * 2
#Тесты
'''
"var_3.prime(10)"
1000 loops, best of 5: 33.1 usec per loop

"var_3.prime(100)"
1000 loops, best of 5: 9.21 msec per loop

'''

'''
Вывод: быстрее всего работают способы, использующие решето Эратосфена. Само решето Эратосфена имеет сложность O(nlog(logn)),
что позволяет справляться с поиском простых чисел максимально быстро. В целом алгоритм по поиску i-ого простого числа выполняется достаточно быстро,
т.к. за границу решета я взял i-ый элемент и позже в цикле удваивал его. Это помогает увеличить скорость алгоритма так,
чтобы не сильно нагрузить генератор решета и при этом сэкономить на количестве итераций цикла. Способ без решета работает крайне медленно.
Cложность одного поиска простых чисел в нём составляет O(n**2). Он крайне не эффективен.
'''