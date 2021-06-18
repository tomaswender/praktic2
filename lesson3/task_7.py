#7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

arr=[]
arr2=[0,0,0]
for i in range(30):
    arr.append(random.randint(0, 10))

for i in range(0, len(arr)):
    if arr[i]>0:
        arr2[0], arr2[1]=arr[i], arr[i]        
for i in range(0, len(arr)-1):
    if arr[i]<arr2[0]:
        arr2[0]=arr[i]
        arr2[2]=i
arr.pop(arr2[2])
arr2.pop(2)
for i in range(0, len(arr)):
    if arr[i]>=arr2[0] and arr[i]<arr2[1]:
        arr2[1]=arr[i]    
print(arr)
print(arr2)


# Второй вариант


m=100
arr=[]
arr2=[m,m]

for i in range(30):
    arr.append(random.randint(0, m))
print(arr)
for i in arr:
    if i<arr2[0]:
        arr2[1], arr2[0] = arr2[0], i                
    elif (i<arr2[1] and i>=arr2[0]):
        arr2[1]=i
print(arr2)


