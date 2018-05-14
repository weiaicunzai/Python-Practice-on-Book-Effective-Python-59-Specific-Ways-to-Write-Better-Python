
a = 1
print(type(a))
print(type(3))
print(a.__add__(2))
print(dict)


class DoNothing(object):
    pass

print(type(DoNothing))
print(type(DoNothing()))


from a import A

print(type(A))
print(type(A()))

print(type(DoNothing))

print(type(tuple), type(list))


def int_factory(s):
    i = int(s)
    return i

i = int_factory('100')



#metafunction:
def class_factory():
    class Foo:
        def hello(self):
            a = 10
            print("hh", a)
    return Foo

F = class_factory()
print(type(F))

F().hello()
a = F()
print(type(a))



def h():
    print(11)

def h():
    print(22)

h()

class Foo(object):
    i = 4
    def __init__(self, index):
        self.index = index

class Bar(Foo):
    def have1(self, message):
        print(message)
        return 1



hii = type("hii", (), {'x': 111, 'index':10})
print('---------------')
print(hii)
print(hii().x)
print(hii().index)
print(hii.__class__)


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print('called')
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            cls.x = 5
        return cls._instances[cls]

class MyClass(object, metaclass=Singleton):
    pass

m = MyClass()
v = MyClass()
print(m.x)
m.x = 111
print(v.x)
