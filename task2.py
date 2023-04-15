# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5


import random

x = int(input("Введите искомое число: "))
my_list = [random.randint(1, 99) for i in range(1, 10)]
result_list = []
difference = 0
result = x

for i in range(len(my_list)):
    difference = x - my_list[i]
    if difference < 0:
        difference = difference * -1
    result_list.append(difference)
   # print(difference)

min_value = result_list[0]

for j in range(len(result_list)):
    if result_list[j] <= min_value:
        result = my_list[j]
        min_value = result_list[j]

print(my_list)
if result == x:
    print(f"Число {x} присутствует в списке")
else:
    print(f"Максимально близкое число к искомому {result}")
