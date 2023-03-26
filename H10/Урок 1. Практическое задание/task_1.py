"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'сокет', 'декоратор']

for line in words:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))
print('-' * 50)
points = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
          b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
          b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for line in points:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))
print("-" * 50)
for line in words:
    print(f'длина строки - {len(line)}    ')
    print(f'содержание переменной - {line}')
    points_line = ascii(line)
    encod = ''
    for i in range(1, len(points_line) - 1):
        encod = encod + points_line[i]
    print(f'тип переменной - {type(encod)}    ')
    print(f'длина строки - {len(encod)}    ')
    print(f'содержание переменной - {encod}')
    print('-' * 50)

