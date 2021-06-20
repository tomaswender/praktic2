import cProfile
# // данная реализация алгоритма была взята из интернета и после осмысления добавлена сюда
def rehito(n):
    #n = int(input("Введите верхнюю границу диапазона: "))
    sieve = set(range(2, n+1))
    while sieve:
        prime = min(sieve)
        #print(prime, end = "\t")    #// все времся уходило только на отображение
        sieve -= set(range(prime, n+1, prime))
    print(sieve)

#cProfile.run('rehito(10000)')


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


# // это было написано после прочтения устного описания алгоритма, формули из википедии не понял
def rehito2(n):
    list1 = list(range(2, n+1))
    for i in range(2,6):  # ограничел число вызовов что бы не проходить по всему списку
        for y in list1:
            if y%i==0 and y!=i:
                list1.remove(y)
    #print(list1)
#rehito()
cProfile.run('rehito2(10000)')


#         7335 function calls in 0.167 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.167    0.167 <string>:1(<module>)
#        1    0.002    0.002    0.167    0.167 task.py:31(rehito2)
#        1    0.000    0.000    0.167    0.167 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     7331    0.165    0.000    0.165    0.000 {method 'remove' of 'list' objects}

# /// много времени уходит на перезапись листа

# // разница во времени из-за того что я сохраняю список с простыми числами, а в первом способе список очищается, тем самым цыкл вновь не проходит по тем же значениям


# // проверка любого числа

def test(a):
    for i in range(2,6):
        if a%i==0:
            print(f'Число  {a} кратно {i}')
            break
        elif i==5 and a%i!=0:
            print(f'Число является простым')
                   
#test(1517)