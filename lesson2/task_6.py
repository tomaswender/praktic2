import random

#6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, вывести правильный ответ.

a = random.randint(0,100)
print('Число загадано!')
for i in range(10):
    b=int(input('Ваш вариант: '))
    if a == b:
        print('Угадал!')
        break
    elif a<b:
        print(f'Введенное число больше загаданного \n у вас усталось {9-i} попыток')
    else:
        print(f'Введенное число меньше загаданного \n у вас усталось {9-i} попыток')