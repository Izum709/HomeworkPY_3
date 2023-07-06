# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

massive = []
n = int(input('Введите длину массива -> '))
for i in range(n):
    i = int(input('Введите элемент массива -> '))
    massive.append(i)
print(massive)
x = int(input('Введите число X -> '))
for i in range(len(massive)):
    if x == massive[i]:
        print('Искомый элемент совпал с элементом массива -> ', massive[i])
        print('Ближайшие элементы ->', massive[i - 1], ' < ', x, ' < ', massive[i + 1] )
        break
    elif massive[n - 1 ] < x:
        print('Ближайший элемент массива ->', massive[n - 1])
        break
    elif massive[0] > x:
        print('Ближайший элемент массива ->', massive[0])
        break
    elif massive[i] < x < massive[i + 1]:
        print('Ближайшие элементы ->', massive[i], ' < ', x, ' < ', massive[i + 1] )
        break
    elif x == massive[n - 1]:
        print('Ближайшие элементы ->', massive[i - 2], ' < ', x,)
        break
    else:
        print('=(')
        break