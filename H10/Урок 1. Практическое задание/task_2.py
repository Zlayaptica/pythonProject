"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
dict_words = [b'class', b'function', b'method']

for word in dict_words:
    print('Тип переменной: {}\n'.format(type(word)),
          'Содержание переменной: {}\n'.format(word),
          'Длина переменной: {}\n'.format(len(word)))
