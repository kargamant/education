#4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
print('Введите две буквы:')
letter_1 = input()
letter_2 = input()
print(f'Первая буква стоит на {ord(letter_1)-96} месте\n'
      f'Вторая буква стоит на {ord(letter_2)-96} месте\n'
      f'Между ними {ord(letter_2)-ord(letter_1)} букв')