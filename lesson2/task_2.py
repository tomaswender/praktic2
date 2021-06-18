#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


a = list(input('Введите число: '))
my_list = []
my_list2 = []
for i in a:
    if int(i) % 2 == 0:
        my_list.append(i)
    else:
        my_list2.append(i)
print(f'Четных: {len(my_list)}')
print(f'Не четных: {len(my_list2)}')
