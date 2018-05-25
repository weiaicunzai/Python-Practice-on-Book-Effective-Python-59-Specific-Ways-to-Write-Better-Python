from functools import partial


def hello(name, age, sex):
    print(name, age, sex)


def hello1(name, age, sex='m'):
    print(name, age, sex)


f = partial(hello1, age=10, sex='f')


f('bai')

f = partial(hello, sex = 'f')
f('bai', 33)
