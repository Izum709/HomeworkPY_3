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
min_diff = abs(massive[0] - x)
min_index = 0
for i in range(1, len(massive)):
    diff = abs(massive[i] - x)
    if diff < min_diff:
        min_diff = diff
        min_index = i
print('Ближайший элемент:->', massive[min_index]) 