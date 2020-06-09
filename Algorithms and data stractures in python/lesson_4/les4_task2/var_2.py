#С использованием решета эратосфена через рекурссию
from cProfile import run

def sieve(el):
    # n - граница массива.
    # она определяется введённым номером i-ого элемента
    # и позже после вызова функции увеличивается на его удвоенное значение.
    # Это помогает увеличить скорость алгоритма так,
    # чтобы не сильно нагрузить генератор решета и при этом сэкономить на количестве вызовов рекурссии.
    #Это поможет избежать переполнения стека вызовов функции при работе с большим объёмом данных
    n = el
    def _sieve(n, el):
        sieve = [i  for i in range(n)]
        sieve[1] = 0
        for i in range(2, n):
            if i != 0:
                k = i*2
                while k < n:
                    sieve[k] = 0
                    k += i
        result = [i for i in sieve if i != 0]
        # Проверка на существование значения i-ого элемента в массиве result
        if len(result)-1 < el-1:
            n += el * 2
            return _sieve(n, el)
        return result[el-1]
    return _sieve(n, el)
'''
tests = [10, 100, 500]
for item in tests:
    run(f'sieve({item})')
'''
#Тесты
'''
"var_2.sieve(10)"
1000 loops, best of 5: 15.7 usec per loop
Профилизация
12 function calls (11 primitive calls) in 0.000 seconds
ncalls -  2/1    0.000    0.000    0.000    0.000 var_2.py:6(_sieve)

"var_2.sieve(100)"
1000 loops, best of 5: 1.07 msec per loop
Профилизация
20 function calls (17 primitive calls) in 0.001 seconds
ncalls - 4/1    0.001    0.000    0.001    0.001 var_2.py:6(_sieve)

"var_2.sieve(500)"
1000 loops, best of 5: 12.5 msec per loop
Профилизация
24 function calls (20 primitive calls) in 0.012 seconds
 ncalls - 5/1    0.011    0.002    0.012    0.012 var_2.py:6(_sieve)
'''

'''
Вывод: быстрее всего работают способы, использующие решето Эратосфена. Само решето Эратосфена имеет сложность O(nlog(logn)),
что позволяет справляться с поиском простых чисел максимально быстро. В целом алгоритм по поиску i-ого простого числа выполняется достаточно быстро,
т.к. за границу решета я взял i-ый элемент и позже в цикле удваивал его. Это помогает увеличить скорость алгоритма так,
чтобы не сильно нагрузить генератор решета и при этом сэкономить на количестве итераций цикла.
'''