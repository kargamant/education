#2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
print('Введите координаты первой точки:')
x1 = int(input())
y1 = int(input())
print('Введите координаты второй точки:')
x2 = int(input())
y2 = int(input())
if x1==x2:
    print('Такой прямой не существует')
else:
    k = (y1 - y2) / (x1 - x2)
    if k==0:
        print(f'Уравнение прямой: y={y2}')
    b = y2-k*x2
    print(f'Уравнение прямой: y = {k}x+{b}')
