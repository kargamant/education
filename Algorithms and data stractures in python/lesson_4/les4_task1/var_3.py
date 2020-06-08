#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

from cProfile import run
#from functools import lru_cache
from .var_1 import test_sum

#Вариант 3 - с использованием цикла.

#@lru_cache()
def sum_loop(n):
    s = 0
    for i in range(n):
        s += (-0.5)**(i)
    return s

#проверка корректной работы функции print(test_sum(sum_loop))

#Тесты
#Профилизация делать нет смысла, т.к. в данном случае функция будет вызвана ровно 1 раз
'''
"var_3.sum_loop(10)"
1000 loops, best of 5: 2.54 usec per loop
С использованием встроенной мемоизации
1000 loops, best of 5: 117 nsec per loop

"var_3.sum_loop(100)"
1000 loops, best of 5: 23 usec per loop
С использованием встроенной мемоизации
1000 loops, best of 5: 119 nsec per loop

"var_3.sum_loop(500)"
1000 loops, best of 5: 122 usec per loop
С использованием встроенной мемоизации
1000 loops, best of 5: 122 nsec per loop

 "var_3.sum_loop(1000)"
1000 loops, best of 5: 244 usec per loop
С использованием встроенной мемоизации
1000 loops, best of 5: 124 nsec per loop

"var_3.sum_loop(100000)"
1000 loops, best of 5: 34.1 msec per loop
С использованием встроенной мемоизации
1000 loops, best of 5: 144 nsec per loop
'''
'''
Вывод: этот алгоритм справляется с задачей очень быстро, а также может справляться с любым объёмом данных, 
т.к. не имеет лимита стека вызовов рекурсии.
Для данной задачи он наиболее оптимален, 
т.к. ключевыми факторами эффективной работы этой программы являются работа с максимально возможным объёмом данных и скорость выполнения. 
Этот алгоритм не имеет ограничений по объёму обрабатываемых данных и справляется с ними быстро =>
 => является самым эффективным решением данной задачи.  
 '''
#Пометка насчёт встроенной мемоизации
'''
Инструмент lru_cache даёт значительный прирост в скорости, однако он не спасёт от переполнения стека вызова функции,
а также довольно требовательный к ресурсам компьютера. Результаты тестов с его участием зачастую необъективны, поэтому я
решил не рассматривать алгоритм с ним как отдельный вариант решения.
'''