#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

amount = int(input('Введите количество вводимых чисел>>>'))
max_s = 0
while amount != 0:
	num = int(input('Введите число>>>'))
	s = 0
	amount -= 1
	n = num
	while num != 0:
		s += num%10
		num = num // 10
	if s > max_s:
		max_s = s
		pr_num = n
	else:
		continue
print(f'Наибольшая сумма чисел: {max_s} у числа {pr_num}')


