"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
dict_words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in dict_words:
    word = word.encode('utf8')
    print(word)
    word = word.decode('utf8')
    print(word)
    print()


