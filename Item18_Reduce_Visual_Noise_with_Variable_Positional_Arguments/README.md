# Reduce	Visual	Noise	with	Variable	Positional Arguments


```
def log(msg, values):
    if not values:
        print(msg)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(msg, value_str)

log('hello', [1, 3, 5])

# [] looks cumbersome and noisy
log('hello', [])


hello 1, 3, 5
hello
```

* use variable positional arguments

```
def log1(msg, *values):
    if not values:
        print(msg)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(msg, value_str)

log1('hello')


hello
```


two drawbacks:
* if the caller of the function log1 uses the * operator on a iterator, it will be iterated until it's exhausted

```
a_iter = iter(range(10000))

# will exhausted iterator a_iter
# before passing to function
log1('hello', a_iter)

```


* add positional argument to the function log1, the caller will break

```
def log1(seq, msg, *values):
    if not values:
        print(‘%s:	%s’	%	(seq,	msg))
    else:
        values_str	= ‘, ‘.join(str(x) for x in	values)
        print(‘%s:	%s:	%s’	% (sequence, message, values_str))
log(‘Favorite	numbers’,	7,	33)
Favorite	numbers:	7:	33
```

use keyword arguments instead