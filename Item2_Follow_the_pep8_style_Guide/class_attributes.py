
class Base:

    def __init__(self):
        self.attr = 1
        self._protected_attr = 2
        self.__private_attr = 3

b = Base()

print(b.attr)
print(b._protected_attr)
# __private_attr becomes _Base__private_attr
print(b._Base__private_attr)


class Derived(Base):

    def __init__(self):
        super().__init__()
        pass


d = Derived()
print(d.attr)
print(d._protected_attr)
print(d._Base__private_attr)