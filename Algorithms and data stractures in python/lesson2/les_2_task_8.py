#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

amount = int(input('Введите количество чисел>>>'))
i = int(input('Введите цифру, которую необходимо посчитать>>>'))
s = 0
while amount != 0:
	num = int(input('Введите число>>>'))
	while num != 0:
		if num%10 == i:
			s += 1
		num = num // 10
	amount -= 1
print(f'Цифра {i} встречается {s} раз')