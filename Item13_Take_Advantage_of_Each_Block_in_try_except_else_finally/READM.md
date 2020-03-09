
# Take	Advantage	of	Each	Block	in try/except/else/finally

* try exception clause

use try exception clause to prevent programs from crushing

No:
```
>>> import docutils
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'docutils'
```
Yes:
```
try:
    import docutils

except ImportError:
    print('import error')

```
output:
```
import error
```

* when to use try
EAFP coding style, handles racing condition



* duck typing and EAFP coding style

“If it looks like a duck and quacks like a duck, it must be a duck.”
```
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

```

* racing condition

```
d = {}
words = ['a','d','a','c','b','z','d']
#LBYL
for w in words:

    # other thread could deleted w already
    if w not in d:
        d[w] = 0
    d[w] += 1

#EAFP
for w in words:
    try:
        d[w] += 1
    except KeyError:
        d[w] = 1
```

* try finally
Use	try/finally	when	you	want	exceptions	to	propagate	up,	but	you	also	want	to	run cleanup	code	even	when	exceptions	occur.

```
handle = open('tmp/random_data.txt')
try:
    data = handle.read()
finally:
    handle.close()
```

* finally will cover the return result of try

```
def f():
    try:

        return 1
    finally:
        # function 0 will always return 0
        return 0

print(f())

>>>0
```

* Use	try/except/else	to	make	it	clear	which	exceptions	will	be	handled	by	your	code and	which	exceptions	will	propagate	up.


```
def	load_json_key(data,	key):
try:
    result_dict	= json.loads(data)

# May raise ValueError
# you want to handle Value Error exception
except	ValueError	as	e:
    raise	KeyError	from	e

else:
    # May raise	KeyError
    # you want KeyError to propagate up
    return	result_dict[key]
```