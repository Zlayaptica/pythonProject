class DocMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = []

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__()
        return self.__instance


class MyClass(metaclass=DocMeta):
    pass


list_1 = MyClass()
list_2 = MyClass()
print(list_1 is list_2)
