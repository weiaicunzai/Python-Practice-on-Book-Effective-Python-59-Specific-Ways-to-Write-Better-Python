


class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


class MyOtherObject:
    def __init__(self):
        self.__private_field = 99

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

foo = MyObject()
print(foo.public_field)


print(foo.get_private_field())

#print(foo.__private_field)

bar = MyOtherObject()
print(MyOtherObject.get_private_field_of_instance(bar))



# Document	each	protected	field	and	explain	which	are	internal	APIs
# available	to	subclasses	and	which	should	be	left	alone	entirely.

class MyClass:
    def __init__(self, value):
        # this stores user-defined value for the object
        # It should be coercible to a string. Once assigned
        # for the object it should be treated as immutable
        self._value = value


# only time you should consider private attributs is when you're worried
# about naming conflicts with subclasses

class APIClass:
    def __init__(self, value):
        self.__value = value

# sub conflicts are possible with such common attribute name
class SubClass:
    def __init__(self, value):
        self.__value = value
