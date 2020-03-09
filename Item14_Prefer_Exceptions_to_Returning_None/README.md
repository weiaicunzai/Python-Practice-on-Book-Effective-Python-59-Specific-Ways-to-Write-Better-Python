# Prefer	Exceptions	to	Returning	None


* Functions	that	return	None	to	indicate	special	meaning	are	error	prone	because None	and	other	values	(e.g.,	zero,	the	empty	string)	all	evaluate	to	False	in conditional	expressions.

No:
```
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return None
```

* Raise	exceptions	to	indicate	special	situations	instead	of	returning	None.	Expect	the calling	code	to	handle	exceptions	properly	when	they’re	documented.

Yes:
```
def	divide(a,	b):
    try:
        return	a	/	b
    except	ZeroDivisionError	as	e:
        raise	ValueError(‘Invalid	inputs’)	from	e
```

* raise from

```
try:
    raise ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError from e
```
output:
```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ValueError
```


```
try:
    raise ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError
```

output:
```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ValueError
```

difference:
use from clause:
```
During handling of the above exception, another exception occurred:
```

do not use from clause:
```
During handling of the above exception, another exception occurred:
```

Different message, intended to flag a possible bug in the error handling

when you want to raise exception in an exception handler, you could use
from clause

example:

```
code in django:
# if you want to raise an Error and custom the output message:
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
```