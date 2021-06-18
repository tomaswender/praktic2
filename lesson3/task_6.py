#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.
import random

arr=[]
arr2=[0,0,0,0]
s=0
for i in range(10):
    arr.append(random.randint(0, 100))

for i in range(0, len(arr)):
    if arr[i]<=arr2[1]:
        arr2[0]=i
        arr2[1]=arr[i]
    elif arr[i]>arr2[3]:
        arr2[2]=i
        arr2[3]=arr[i]
for i in range(arr2[0]+1, arr2[2]):
    s+=arr[i]
print(arr)
print(arr2)
print(s)