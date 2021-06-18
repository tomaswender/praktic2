import random

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

list1=[]
maxi= [0,0]
mini=[0,0]
b=0
while len(list1)<10:
    list1.append(random.randint(0, 100))
for i in range(0, len(list1)):
    if list1[i]>b:
        b=list1[i]
        maxi[0]=i 
        maxi[1]=list1[i]
for i in range(0, len(list1)):
    if list1[i]<b:
        b=list1[i]
        mini[0]=i 
        mini[1]=list1[i]   
print(list1)
print(maxi)
print(mini)
list1[maxi[0]]=mini[1]
list1[mini[0]]=maxi[1]
print(list1)