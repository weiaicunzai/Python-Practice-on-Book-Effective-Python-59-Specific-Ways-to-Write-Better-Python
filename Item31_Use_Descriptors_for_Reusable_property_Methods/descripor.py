
class HomeWork:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


grade = HomeWork()
grade.value = 100


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


class Grade:
    def __init__(self, name):
        self.name = name
        self._grade = 0

    def __get__(self, obj, type=None):
        print(obj)
        print(self)
        return obj.__dict__.get(self.name) or 0
        #return self._grade

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError()

        print(instance)
        print(instance.__dict__)
        instance.__dict__[self.name] = value
        #print(self.__dict__)



class Exam1:
    #math_grade = Grade('math_grade')
    #writing_grade = Grade('writing_grade')
    #science_grade = Grade('science_grade')
    def __init__(self):
        #pass
        self.math_grade = Grade('math_grade')
        self.writing_grade = Grade('writing_grade')
        self.science_grade = Grade('science_grade')
       # self.math_grade = Grade()
       # self.writing_grade = Grade()
       # self.science_grade = Grade()

exam = Exam1()
print(type(exam.math_grade))
exam.math_grade = 100
print(type(exam.math_grade))
#print(exam.math_grade)



#first_exam = Exam1()
#print(first_exam.writing_grade)
#first_exam.writing_grade = 10
#print(first_exam.__dict__)
#print(type(first_exam.writing_grade))
#first_exam.science_grade = 12
#
##print()
##print(first_exam.writing_grade)
##print(first_exam.science_grade)
##
##second_exam = Exam1()
##second_exam.writing_grade = 81
##second_exam.science_grade = 13
##print()
##print(second_exam.writing_grade)
##print(second_exam.science_grade)
##
##print()
##print(first_exam.writing_grade)
##print(first_exam.science_grade)
##class Foo():
##    attribute1 = Grade()
##
##my_foo_object = Foo()
##x = my_foo_object.attribute1
##
##print(x)
#
#
## lookup.py
#class Vehicle(object):
#    can_fly = False
#    number_of_weels = 0
#
#class Car(Vehicle):
#    number_of_weels = 4
#
#    def __init__(self, color):
#        self.color = color
#
#my_car = Car("red")
#
#print()
#print(my_car.color)
#print(my_car.number_of_weels)
#print(my_car.can_fly)
#

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