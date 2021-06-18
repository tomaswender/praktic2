#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list1 = []
list2 = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(2, 100):
    list1.append(i)
for n in list1:
    for i,y in list2.items():
        if n%i==0:
            list2[i]=list2[i]+1
print(list2)