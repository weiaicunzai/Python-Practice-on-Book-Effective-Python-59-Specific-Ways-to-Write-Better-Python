# Use	Descriptors	for	Reusable	@property	Methods


* Reuse	the	behavior	and	validation	of	@property	methods	by	defining	your	own descriptor	classes.

No:
```
class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value

```

YES:
```
class Grade:
    def __init__(self, name):
        self.name = name
        self._grade = 0

    def __get__(self, instance, type=None):
        return instance.__dict__.get(self.name) or 0

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError()

        instance.__dict__[self.name] = value

class Exam1:
    math_grade = Grade('math_grade')
    writing_grade = Grade('writing_grade')
    science_grade = Grade('science_grade')
    def __init__(self):
        pass

```


* can not attach descriptor to instance attributs


if Exam1 instance doesn't have an writing_grade attribute, python will fall back to class attribute, if found, and class attribute is an object which has implemented descriptor protocal, python will assume you are using descriptor
```
class Exam1:
    def __init__(self):
        self.math_grade = Grade()
        self.writing_grade = Grade()
        self.science_grade = Grade()


exam = Exam1()
print(type(exam.math_grade))
exam.math_grade = 100
print(type(exam.math_grade))


<class '__main__.Grade'>
<class 'int'>
```

* do not store values in the descriptor itself, but to store them in the object that the descriptor is attached to

```
class OneDigitNumericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumericValue("number")

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)
```