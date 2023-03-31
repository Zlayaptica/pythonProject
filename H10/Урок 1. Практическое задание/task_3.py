"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
dict_words = ['attribute', 'класс', 'функция', 'type']
dict_words_exit = []
for word in dict_words:
    try:
        dict_words_exit.append(bytes(word, 'ascii'))
    except Exception:
        print(f"Слово '{word}' невозможно записать в байтовом типе с  помощью маркировки b!")
    else:
        print(word, type(word), sep='\n')
    print()