"""speed = int (input ("Ведите скорость автомобиля: "))
time = float(input ("Ведите время поездки  автомобиля: "))

print ("Вы проехали", speed * time)"""



"""num = int (input ("Ведите число: "))
if num > 0:
    print("Это число положительное.")
elif num == 0:
    print("Это число ноль.")
else: 
    print("Это число отрицательное.")"""


"""За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2"""

"""import math
dayDist = int (input ("Ведите расстояние за день: "))
overDist = int (input ("Ведите общее расстояние: "))
print(f"Дней потребуется: {overDist / dayDist}")"""





"""В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32"""


"""
Первый вариант
import math

class_1 = int (input("Введите количество учеников в классе 1: "))
class_2 = int (input("Введите количество учеников в классе 2: "))
class_3 = int (input("Введите количество учеников в классе 3: "))

print (f"Для трех класссов потребуется {math.ceil(class_1 / 2) + math.ceil(class_2 / 2) + math.ceil(class_3 / 2)} парт")"""

"""Второй вариант
class_1 = int (input("Введите количество учеников в классе 1: "))
class_2 = int (input("Введите количество учеников в классе 2: "))
class_3 = int (input("Введите количество учеников в классе 3: "))

print (f"Для трех класссов потребуется {(class_1 // 2 + class_1 % 2) + (class_2 // 2 + class_2 % 2) + (class_3 // 2 + class_3 % 2)} парт")"""

"""Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6"""

"""vagon = int (input("Введите номер вагон от головы поезда: "))
vagonNumb =int (input("Введите номер вагона: "))
if vagon != vagonNumb :
    print("В поезде количество вагонов = ", (vagon+vagonNumb -1 ))
else:
    print("Количество вагонов определить невозможно")"""



"""Задача №7. Решение в группах
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES"""

"""year = int (input("Введите год: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Высокосный")
else:
    print("Не высокоснй год")"""



#  Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# import math
# over = int (input("Введите общее количество журавликов: "))
# n = over / 4

# print(f"({math.ceil(n)}, {math.ceil(n*2)}, {math.ceil(n)})")

# over = int (input("Введите общее количество журавликов: "))
# n = over / 4
# print(f"Петя сделал {n} жеравликов, Сережа сделал {n} журавликов, Катя сделала {n * 2} журавликов")

# n = 24

# # Введите ваше решение ниже
# import math
# b = n / 6
# c = b 
# a = (b + c) * 2


# print(f"({math.ceil(b)}, {math.ceil(a)}, {math.ceil(c)})")


# n1 = n // 6
# n2 = n // 6
# n3 = (n // 6) * 4
# print(n1, n3, n2)


""""""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

# n = 111222

# Введите ваше решение ниже

a = n // 100000
b1 = n //10000
b = b1 % 10
c1 = n // 1000
c = c1 % 10
d1 = n//100
d =d1%10
f1 = n //10
f= f1 %10
g = n %10

if a+b+c == d+f+g:
    print("yes")
else:
    print("no")
"""