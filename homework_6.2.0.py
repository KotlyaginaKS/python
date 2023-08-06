'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_2 = []
# max = 10
# min = 6

# 1 вариант
# for i in range(len(lst_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)

# # 2 вариант

# for i in range(len(list_1)):
#     if min <= list_1[i] <= max:
#         print(i, end=' ')

# # 3 вариант

def find_ind(arr, min_value, max_value):
    index = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            index.append(i)
    return index

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = int(input('Введите минимальное значение: '))
max_value = int(input('Введите максимальное значение: '))

result = find_ind(arr, min_value, max_value)
print(result)