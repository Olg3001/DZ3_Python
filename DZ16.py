# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N / 2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random

print('Program to check how many times the inputed number is in the list')

n = int(input('Input the list length: '))

if n <= 0:
    print('Wrong input! Input positive integer. ')
else:    
    x = int(input('Input the number you want to find: '))

    list = []
    count = 0

    for i in range(0, n):
        random_number = round(random.uniform(1, n / 2))
        list.append(random_number)
        if list[i] == x: 
            count += 1

    print(f'\nThe list is: {list}')
    if count == 0: 
        print('The inputed number is not in the list.')
    else: 
        print(f'The inputed number is {count} times in the list.')