# Задание 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
# Подсказка:
# Вариант исполнения:
# - условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
# - условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите операцию (+, -, *, / или 0 для выхода): +
# Введите первое число: 214
# Введите второе число: 234
# Ваш результат 448
# Введите операцию (+, -, *, / или 0 для выхода): -
# Введите первое число: вп
# Вы вместо трехзначного числа ввели строку (((. Исправьтесь
# Введите операцию (+, -, *, / или 0 для выхода).
# while True:
#     operator = input("Введите один из операторов +,-,*,/ или 0 для выхода: ")
#     if operator == '0':
#         break
#     number_one = float(input("Введите первое число: "))
#     number_two = float(input("Введите второе число: "))
#     if operator == '+':
#         result = number_one + number_two
#     elif operator == '-':
#         result = number_one - number_two
#     elif operator == '*':
#         result = number_one * number_two
#     elif operator == '/':
#         if number_two == 0:
#             print("деление на ноль запрещено")
#             continue
#         result = number_one / number_two
#     else:
#         print("операция не поддерживается")
#         continue
#     print(f"{number_one} {operator} {number_two} = {result}")
def calcul():
    a = input('Введите операцию (+, -, *, / или 0 для выхода)')
    if a == '0':
        return print(f'Выход')
    number_one = input('Введите первое число:')
    try:
        number_one = int(number_one)
    except:
        print('Вы вместо числа ввели строку')
        return calcul()
    number_two = input('Введите второе число:')
    try:
        number_two = int(number_two)
    except:
        print('Вы вместо числа ввели строку')
        return calcul()
    if a == '*':
        print(f' {number_one} * {number_two} = {number_one * number_two}')
        return calcul()
    elif a == '+':
        print(f' {number_one} + {number_two} = {number_one + number_two}')
        return calcul()
    elif a == '-':
        print(f' {number_one} - {number_two} = {number_one - number_two}')
        return calcul()
    elif a == '/':
        if number_two == 0:
            print(f'Делитель = 0, На 0 делить нельзя!')
            return calcul()
        else:
            print(f' {number_one} / {number_two} = {number_one / number_two}')
            return calcul()


p = calcul()
