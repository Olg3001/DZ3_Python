# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые 
# равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random
import os
os.system('cls')

print('Program to find in the list the nearest-neighbor number to the inputed number')

n = int(input('Input the list length: '))

if n <= 0:
    print('Wrong input. Input the positive integer.')
else:    
    x = int(input('Input the number you want to check: '))
    
    if x <= 0:
        print('Wrong input. Input the positive integer.')
    else:
        list = []
    
        for i in range(0, n):
            random_number = round(random.uniform(1, 10))
            list.append(random_number)

        print(f'\nThe list is: {list}')
        list.sort(reverse = True)  
        nearest_number = list[0]    

        for item in list:
            if abs(item - x) <= abs(nearest_number - x):
                nearest_number = item
            
        if nearest_number == x: 
            print(f'The inputed number {nearest_number} is in the list.')
        else:    
            print(f'The nearest-neighbor number is {nearest_number}')