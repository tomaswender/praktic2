import cProfile
# // данная реализация алгоритма была взята из интернета и после осмысления добавлена сюда
def rehito(n):
    #n = int(input("Введите верхнюю границу диапазона: "))
    sieve = set(range(2, n+1))
    a=0
    while sieve:
        prime = min(sieve)
        print(prime, end = "\t")    
        sieve -= set(range(prime, n+1, prime))
        a+=1
    print(sieve)

#cProfile.run('rehito(100)')


#        19189 function calls in 5.017 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    5.017    5.017 <string>:1(<module>)
#        1    0.042    0.042    5.016    5.016 task1.py:3(rehito)
#        1    0.000    0.000    5.017    5.017 {built-in method builtins.exec}
#        1    2.491    2.491    2.491    2.491 {built-in method builtins.input}
#     9592    2.341    0.000    2.341    0.000 {built-in method builtins.min}
#     9592    0.141    0.000    0.141    0.000 {built-in method builtins.print}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# // это было написано после прочтения устного описания алгоритма, формулу из википедии не понял
def rehito2(n):
    list1 = list(range(2, n+1))
    for i in list1:
        for y in list1:
            if y%i==0 and y!=i:
                list1.remove(y)   
    print(f'Среди масива {n} чисел: {len(list1)} из них простые')
#rehito2(100000)
cProfile.run('rehito2(100000)')


#Среди масива 100000 чисел: 9592 из них простые
#         90413 function calls in 20.182 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000   20.182   20.182 <string>:1(<module>)
#        1    3.318    3.318   20.182   20.182 task.py:32(rehito2)
#       1    0.000    0.000   20.182   20.182 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    90407   16.863    0.000   16.863    0.000 {method 'remove' of 'list' objects}

# /// много времени уходит на перезапись листа

# // как я понял цыкл и услоавие if y%i==0 and y!=i потбребляет больше времени чем sieve -= set(range(prime, n+1, prime)) 
# в котором из множества удаляются значение с шагом минимального значение(простого числа), в моём варианте приходится много раз вновь проходить по одним значения с начала


# // проверка любого числа

def test(a):
    for i in range(2,a+1):
        if a%i==0 and a!=i:
            print(f'Число  {a} кратно {i}')
            break
        elif a%i==0 and a==i:
            print(f'Число является простым')
                   
#test(132185818684757)

# //// ДАЛЬНЕЙШИЙ КОД НЕ РАБОТАЕТ, ЭКСПЕРЕМЕНТЫ ПО СОВМЕЩЕНИЮ ИЗМЕНЯЕМОГО СПИСКА СОХРАНЕНЯЯ ПОИСК ПО ИНДЕКСАМ И ЦИКЛОВ


#list1 = list(range(2, 30+1))
def t1():
    list1 = list(range(2, 10+1))
    l=len(list1)
    y=0
    while y<l:
        n, y= t3(l,y)
        list1, l = t2(n, list1, l)
    return list1

def t3(l,y):
    for n in range(y, l+1):
        y+=1
        return n, y       

def t2(n, list1, l):
    for i in list1[:n]:
            if list1[n]%i==0 and list1[n]!=i:
                list1.remove(list1[n])
                l-=1
    return list1, l
    

#cProfile.run('t1(list1)')

#print(t1())

