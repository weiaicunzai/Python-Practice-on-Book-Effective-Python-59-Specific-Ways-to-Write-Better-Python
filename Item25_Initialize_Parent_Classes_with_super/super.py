
class Base:
    def __init__(self, value):
        print('base')
        self.value = value

class Child:
    def __init__(self, value):
        Base.__init__(self, 5)

class TimesTwo:
    def __init__(self):
        self.value *= 2

class PulsFive:
    def __init__(self):
        self.value += 5

class OneWay(Base, TimesTwo, PulsFive):
    def __init__(self, value):
        Base.__init__(self, value)
        TimesTwo.__init__(self)
        PulsFive.__init__(self)

# plusfive and timestwo in different order
class AnotherWay(Base, PulsFive, TimesTwo):
    def __init__(self, value):
        Base.__init__(self, value)
        TimesTwo.__init__(self)
        PulsFive.__init__(self)

foo = OneWay(5)
print('should be 15:', foo.value)

bar = AnotherWay(5)
print('suppose to be 15:', foo.value)

# Diamond inheritance
class TimesFive(Base):
    def __init__(self, value):
        print('times five')
        #Base.__init__(self, value)
        super().__init__(value)
        self.value *= 5


class PlusTwo(Base):
    def __init__(self, value):
        print('plus two')
        #Base.__init__(self, value)
        super().__init__(value)
        self.value += 2

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        print('this way')
        #TimesFive.__init__(self, value)
        super().__init__(value)
        #PlusTwo.__init__(self, value)

print(';;;;;;;;;;;;;;;')
foo = ThisWay(5)
print('5 * (5 + 2): ', foo.value)
print(';;;;;;;;;;;;;;;')
from pprint import pprint
pprint(ThisWay.mro())

print()

def print_mro(mro):
    mro = [c.__name__ for c in mro]
    mro = '-->'.join(mro)
    print('visited order:', mro)

# case 1

#class A:
#    def process(self):
#        print('A processing')
#
#class B:
#    def process(self):
#        print('B processing')
#
#class C(A, B):
#    pass
#
#c = C()
#c.process()
#print_mro(C.mro())


# case 2
#class A:
#    def process(self):
#        print('process A')
#
#class B:
#    def process(self):
#        print('process B')
#
#class C(B, A):
#    pass
#
#class D(C, B):
#    pass
#
#d = D()
#d.process()
#print_mro(D.mro())
#

## case 3
#class A:
#    def process(self):
#        print('processing A')
#
#class B(A):
#    pass
#
#class C(A):
#    def process(self):
#        print('prcessing C')
#
#class D(B, C):
#    pass
#
#d = D()
#d.process()
#print_mro(D.mro())
#

# case 4
#class A:
#    def process(self):
#        print('processing A')
#
#class B(A):
#    def process(self):
#        print('processing B')
#
#class C(A, B):
#    pass
#
#c = C()
#c.process()
#print_mro(c.mro())