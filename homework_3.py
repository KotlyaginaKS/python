# # Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# # Найдите количество и выведите его.

# # Пример:


# # list_1 = [1, 2, 3, 4, 5]
# # k = 3
# # # 1

# list_1 = [1, 3, 3, 4, 5]
# k = 3
# print(list_1.count(k)) 


# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5



# 



# eng = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# rus = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
# word = input('Введите слово: ').upper()
# if N == 1:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
# elif N == 0:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
# else:
#     print('Вы мухлюете и играете не по правилам!')

# eng = {1:'AEIOULNSTRАВЕИНОРСТ',
#       	2:'DGДКЛМПУ',
#       	3:'BCMPБГЁЬЯ',
#       	4:'FHVWYЙЫ',
#       	5:'KЖЗХЦЧ',
#       	8:'JZШЭЮ',
#       	10:'QZФЩЪ'}

# word = input('Введите слово: ').upper()

# print(sum([k for i in word for k, v in eng.items() if i in v]))


# eng = {1:'AEIOULNSTRАВЕИНОРСТ',
#       	2:'DGДКЛМПУ',
#       	3:'BCMPБГЁЬЯ',
#       	4:'FHVWYЙЫ',
#       	5:'KЖЗХЦЧ',
#       	8:'JZШЭЮ',
#       	10:'QZФЩЪ'}

# k = 'kjnhjuhuuyhgyuguy'
# m = k.upper()
# print(sum([k for i in m for k, v in eng.items() if i in v]))

eng = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JZШЭЮ',
      	10:'QZФЩЪ'}

k = 'lizard'
m = k.upper()
print(sum([k for i in m for k, v in eng.items() if i in v]))


# import re
# def isCyrillic(text):
	
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# text = 'lizard'
# m = text.upper()
# if isCyrillic(text):
# 	print(sum([k for i in m for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in m for k, v in points_en.items() if i in v]))