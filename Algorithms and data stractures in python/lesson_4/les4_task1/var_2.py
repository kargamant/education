#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

from cProfile import run

#Вариант 2 - рекурсивный способ с использованием мемоизации через словарь

def sum_dict(n):
    sum_d = {1: 1}
    def sum(n):
        if n in sum_d:
            return sum_d[n]
        sum_d[n] = sum(n-1) + (-0.5)**(n-1)
        return sum_d[n]
    return sum(n)
'''
Профилизация
tests = [10, 100, 500]
for i in tests:
    run(f'sum_el({i})')
'''
#Тесты

'''
"var_2.sum_el_dict(10)"
1000 loops, best of 5: 4.93 usec per loop
Профилизация
23 function calls (14 primitive calls) in 0.000 seconds
10 ncalls

"var_2.sum_dict(100)"
1000 loops, best of 5: 51.2 usec per loop
Профилизация
203 function calls (104 primitive calls) in 0.000 seconds
100 ncalls

"var_2.sum_el_dict(500)"
1000 loops, best of 5: 248 usec per loop
Профилизация
1003 function calls (504 primitive calls) in 0.003 seconds
500 ncalls
'''

'''Вывод: этот способ, в сравнении с первым лучше справляется с большим объёмом данных засчёт мемоизации,
однако он всё ещё ограничен лимитом стека вызовов и не может справиться с аргументом более 1000 => не самый эффективный.
'''