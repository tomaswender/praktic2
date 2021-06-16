#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

a=input('Введите числа через пробел: ')
my_list=a.split(' ')
max=0
for i in my_list:
    my_list2=list(i)
    m=[]
    for y in my_list2:
        m.append(int(y))        
    s=sum(m)
    if s>max:
        max=s

print(f"{''.join(my_list2)} | Cумма {max}")