


class Old:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

old = Old(10)
old.get_value()
old.set_value(13)

# use plain attributes
class New:
    def __init__(self, value):

        self.value = value
        self.name = ''

new = New(10)
new.value


# if you decide you need special behavior when an attribute is set, you can
# migrate to the @property decorator and it's corresponding setter attributs

class Counter:
    def __init__(self, count):
        self._count = count


    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value > 0:
            self.value = value
        else:
            raise ValueError('value should be greater than 0')

class Test(Counter):
    def __init__(self, value):
        #self.value = value
        #self.count = value
        pass

    #def count(self, value):
    #    print('hello')

t = Test(10)
t.count = -100
print(t.count)
