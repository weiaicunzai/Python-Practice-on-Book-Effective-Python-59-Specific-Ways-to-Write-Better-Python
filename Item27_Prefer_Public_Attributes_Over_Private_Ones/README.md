# Prefer	Public	Attributes	Over	Private	Ones

* Use	documentation	of	protected	fields	to	guide	subclasses	instead	of	trying	to	force access	control	with	private	attributes.

```
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
```


* Only	consider	using	private	attributes	to	avoid	naming	conflicts	with	subclasses	that are	out	of	your	control.

```
class APIClass:
    def __init__(self, value):
        self.__value = value

# sub conflicts are possible with such common attribute name
class SubClass:
    def __init__(self, value):
        self.__value = valu
```