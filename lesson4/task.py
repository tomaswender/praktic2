import cProfile
# // данная реализация алгоритма была взята из интернета и после осмысления добавлена сюда
def rehito():
    n=10000
    #n = int(input("Введите верхнюю границу диапазона: "))
    sieve = set(range(2, n+1))
    while sieve:
        prime = min(sieve)
        #print(prime, end = "\t")    #// все времся уходило только на отображение
        sieve -= set(range(prime, n+1, prime))
    print(sieve)

cProfile.run('rehito()')


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
def rehito2():
    n=10000
    list1 = list(range(2, n+1))
    for i in list1:
        for y in list1:
            if y%i==0 and y!=i:
                list1.remove(y)
    #print(list1)
#rehito()
cProfile.run('rehito2()')


#         190412 function calls in 20.836 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000   20.836   20.836 <string>:1(<module>)
#        1    3.461    3.461   20.836   20.836 task.py:4(rehito)
#        1    0.000    0.000   20.836   20.836 {built-in method builtins.exec}
#   100000    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    90408   17.368    0.000   17.368    0.000 {method 'remove' of 'list' objects}

# /// много времени уходит на перезапись листа

# // разница во времени из-за того что я сохраняю список с простыми числами, а в первом способе список очищается, тем самым цыкл вновь не проходит по тем же значениям