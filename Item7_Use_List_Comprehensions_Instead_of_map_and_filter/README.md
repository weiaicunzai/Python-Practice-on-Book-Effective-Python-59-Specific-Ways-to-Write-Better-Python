# Use	List	Comprehensions	Instead	of	map	and filter

* map is lazy evaluation in Python3, so you can't know the size of data in advance, and you can only benifit if you access your data from left to right: x[0], x[1], x[2], .....

```
>>> a = range(10)
>>> map(lambda x: x ** 2, a)
<map object at 0x7f21da6759b0>

# no size
>>> len(map(lambda x: x ** 2, a))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'map' has no len()
```

* there is no evident speed difference between listcomp and map

* listcomp is more readable than map and filter

Yes:
```
>>> a = range(10)
>>> b = [x for x in a if x > 3]
```

No:
```
>>> a = range(10)
>>> b = map(lambda x: x, filter(lambda x: x > 3, a))
```

* set comprehension

```
>>> a = range(10)
>>> b = {x for x in a}
>>> b
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> type(b)
<class 'set'>
```

* dict comprehension

```
>>> a = {'a': 1, 'b': 2, 'c': 3}
>>> b = {k: v for k, v in a.items()}
>>> b
{'c': 3, 'a': 1, 'b': 2}
>>> type(b)
<class 'dict'>
```