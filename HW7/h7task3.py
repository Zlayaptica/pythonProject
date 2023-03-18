# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# (self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
class Worker:

    def __init__(self, name='Ivan', surname='Ivanov', position='dancer', wage=1200, bonus=200):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    @property
    def income(self):
        return self._income


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_income(self):
        return self._income['wage'] + self._income['bonus']


information = Position('Ivan', 'Ivanov', 'dancer', 110, 30)
print(f'New attributes are: {information.name}, {information.surname}, {information.position}, {information.income}')
print(f'Total salary of {information.get_full_name()} is {information.get_full_income()}')
