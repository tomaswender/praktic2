import random


 # 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# //не правильно решено
def sum_pr():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    sum=a+b+c
    pr=a*b*c
    print (f'Сумма равна: {sum}')
    print (f'Произведение чисел: {pr}')

# sum_pr()


#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый 
# сдвиг вправо и влево на два знака. Объяснить полученный результат.
# // не все логические операции

def pobit():
    a=5
    b=6
    print(f'&: {a&b}')
    print(f'|: {a|b}')
    print(f'>>2: {a>>2}')
    print(f'<<2: {a<<2}')
# при смещениии << и >> текущие биты числа смещаются в указанную стороную и добавялются два нуля с обратной стороны 
# pobit()

#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# //ошибка деление на ноль

def line():
    print("Координаты точки A(x1;y1):")
    x1 = float(input("\tx1 = "))
    y1 = float(input("\ty1 = "))
    
    print("Координаты точки B(x2;y2):")
    x2 = float(input("\tx2 = "))
    y2 = float(input("\ty2 = "))
    
    print("Уравнение прямой, проходящей через эти точки:")
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k*x2
    print(" y = %.2f*x + %.2f" % (k, b))

# line()

#4. Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ 
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
# // для символов нужно было использовать chr

def rand():
    alfavit= {1:'a', 2:'b', 3:'c'}
    a = int(input('Введите первое целое число: '))
    b = int(input('Введите второе целое число: '))
    print(f'{random.randint(a, b)}') #- случайное целое число N, A ≤ N ≤ B.v
    a1 = float(input('Введите первое вещественное число: '))
    b1 = float(input('Введите второе вещественное число: '))
    print(f'{random.uniform(a1, b1)}') #- случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A).

# rand()

#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# // https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-ord/



#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def lang():
    a2 = int(input('Введите номер буквы: '))
    a=('abcdefghijklmnopqrstuvwxyz')
    print(a[a2-1])

# lang()

#7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. 
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# // все норм, гугл в помощь

def triangle():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))    
    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник не существует")
    elif a != b and a != c and b != c:
        print("Разносторонний")
    elif a == b == c:
        print("Равносторонний")
    else:
        print("Равнобедренный")

# triangle()

#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# // все норм, гугл в помощь

def year():
    year = int(input('Введите год: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(True)
    else:
        print(False)

# year()


#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def avg():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    c = float(input('Введите третье число: '))
    m=''
    if (a>b and a<c) or (a<b and a>c):
        m=a
    elif (b>a and b<c) or (b<c and b>c):
        m=b
    elif (c>b and c<a) or (c<b and c>a):
        m=c
    print(m)

# avg()