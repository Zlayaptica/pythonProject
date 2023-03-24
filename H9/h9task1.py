class Allowing(object):
    global result

    def __delattr__(self, name):
        result = self.__dict__.get(name)
        for method in ('__get__', '__set__', '__delete__'):
            if hasattr(result, method):
                result = result.__delete__(name)
            break
        else:
            result = object.__delattr__(self, name)
        return result

    def __getattribute__(self, *args):
        result = object.__getattribute__(self, *args)
        for method in ('__get__', '__set__', '__delete__'):
            if hasattr(result, method):
                result = result.__get__(self, self.__class__)
        return result

    def __setattr__(self, name, val):
        result = self.__dict__.get(name)
        for method in ('__get__', '__set__', '__delete__'):
            if hasattr(result, method):
                result = result.__set__(self, val)
            break
        else:
            result = object.__setattr__(self, name, val)
        return result

    @property
    def world(self):
        return 'hello!'
