#6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
print('Введите длины трёх отрезков')
a = int(input())
b = int(input())
c = int(input())
if a+b>c and b+c>a and a+c>b:
    if a==b and a==c:
        print('Треугольник равносторонний')
    elif a==b or b==c or a==c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника не существует')