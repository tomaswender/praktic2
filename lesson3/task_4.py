import random

#4. Определить, какое число в массиве встречается чаще всего.
# /// условно принято что с максимальным повтором может быть только одно число
list1=[]
b=[0,0]
while len(list1)<30:
    list1.append(random.randint(0, 10))
for i in list1:
    if b[1]<list1.count(i):
        b[0]=list1[i]
        b[1]=list1.count(i)
print(list1)
print(b)