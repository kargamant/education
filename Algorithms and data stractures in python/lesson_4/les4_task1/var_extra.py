#Способ для тех, кто помнит школьную программу по математике:D
#1, -0.5, 0.25, -0.125... является геометрической прогрессией
#сумму n элементов можно вычислить по формуле b1(q**n - 1)/q-1
#q = -0.5
#b1 = 1

def sum_math(n):
    return 1*(((-0.5)**n) - 1)/(-0.5-1)

#Тесты
'''
"var_extra.sum_math(10)"
1000 loops, best of 5: 566 nsec per loop

 "var_extra.sum_math(100)"
1000 loops, best of 5: 413 nsec per loop

"var_extra.sum_math(500)"
1000 loops, best of 5: 407 nsec per loop
'''
'''
Вывод:
Данный алгоритм работает быстрее всех, а также лучше всех справляется с большим объёмом данных.
Сложность O(n) в данном случае не зависит от лишних переменных, циклов, т.к. вся функция это одно математическое выражение.
Ограничений ввиде лимита стека вызовов функции здесь нет.
Это самый эффективный способ решения задачи, однако я всё же за автоматизацию того, что может сделать человек) 
'''