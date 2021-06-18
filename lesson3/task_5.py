#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. 
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

n = 10
a = []
for i in range(n):
    a.append(random.randint(-50, 50))

i = 0
index = -1
while i < n:
    if a[i] < 0 and index == -1:
        index = i
    elif a[i] < 0 and a[i] > a[index]:
        index = i
    i += 1
print(index+1,':', a[index])