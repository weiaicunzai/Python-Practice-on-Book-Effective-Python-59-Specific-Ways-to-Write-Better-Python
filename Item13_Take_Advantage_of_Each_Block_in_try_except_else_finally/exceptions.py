

try:
    import docutils

except ImportError:
    print('import error')



class Duck:

    def quack(self):
        print('duck quacking...')

    def fly(self):
        print('duck flap...')

class Person:

    def quack(self):
        print('person quacking...')

    def fly(self):
        print('person flapping arms...')


# LBYL coding style  non - pythonic
# leaf before you leap

def quack_and_fly(thing):
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly


# EAFP coding style pythonic
# Easier to ask forgiveness than permission
def quack_and_fly1(thing):

    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)




def f():
    try:

        return 1
    finally:
        return 0

print(f())