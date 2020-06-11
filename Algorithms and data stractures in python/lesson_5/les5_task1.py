from collections import OrderedDict

#Инициализация переменных
N = int(input('Введите количество предприятий:\n'))
sum = 0
d = {}

#Формирование словаря для хранения названий и прибыли
for i in range(1, N+1):
    name = input(f'Введите название {i} предприятия:\n')
    profit = float(input(f'Введите прибыль {i} предприятия:\n'))
    d[name] = profit
    sum += profit

average = sum/N
d['average'] = average
d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

#Обработка значений
val = list(d.values())
names = list(d.keys())
mid = val.index(average)
#Алгоритм, напоминающий бин. поиск
for i in range(0, mid):
    print(f'Прибыль предприятия {names[i]} - меньше среднего {average}')
for i in range(mid+1, len(d)):
    print(f'Прибыль предприятия {names[i]} - больше среднего {average}')

