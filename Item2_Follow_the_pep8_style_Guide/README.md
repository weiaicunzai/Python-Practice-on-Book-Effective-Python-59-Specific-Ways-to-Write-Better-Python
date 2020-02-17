# PEP 8

* Functions, variables, and attributes should be in lowercase_underscore
format.
* Protected	instance	attributes	should	be	in	_leading_underscore	format.
* Private	instance	attributes	should	be	in	__double_leading_underscore
format.

```
class Base:

    def __init__(self):
        self.attr = 1
        self._protected_attr = 2
        self.__private_attr = 3

b = Base()

print(b.attr)
print(b._protected_attr)
# __private_attr becomes _Base__private_attr
print(b._Base__private_attr)

>>>
1
2
3
```

```
class Derived(Base):

    def __init__(self):
        super().__init__()
        pass


d = Derived()
print(d.attr)
print(d._protected_attr)
print(d._Base__private_attr)

>>>
1
2
3
```

* When the conditional part of an if-statement is long enough to require that it be written across multiple lines, it's worth noting that the combination of a two character keyword (i.e. if), plus a single space, plus an opening parenthesis creates a natural 4-space indent for the subsequent lines of the multiline conditional. This can produce a visual conflict with the indented suite of code nested inside the if-statement, which would also naturally be indented to 4 spaces. This PEP takes no explicit position on how (or whether) to further visually distinguish such conditional lines from the nested suite inside the if-statement. Acceptable options in this situation include, but are not limited to:

```
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

examples:
```
# Yes:
if (top_inter + bot_inter == 1 and
        left_inter + right_inter == 1 and
        current_inters[tuple(cur)] == 255):

    img_cols[cur[0]: bot[0], cur[1]] = 25

# No:
if top_inter + bot_inter == 1 and \
   left_inter + right_inter == 1 and \
   current_inters[tuple(cur)] == 255:

    img_cols[cur[0]: bot[0], cur[1]] = 25
```

* Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.

```
# Yes:
a = 1 + \
    1
a

>>>
2

# No:
a = 1 + \ # add one space here
    1

>>>
  File "<stdin>", line 1
    a = 1 + 1\
              ^
SyntaxError: unexpected character after line continuation character
```

* If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.

Yes:
```
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

No:
```
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

* Don’t	check	for	empty	values	(like	[]	or	'')	by	checking	the	length	(if
len(somelist)	==	0).	Use	if	not	somelist	and	assume	empty	values
implicitly	evaluate	to	False.

* The	same	thing	goes	for	non-empty	values	(like	[1]	or	'hi').	The	statement	if
somelist	is	implicitly	True	for	non-empty	values.

* Comparisons to singletons like None should always be done with is or is not, never the equality operators.

Also, beware of writing if x when you really mean if x is not None -- e.g. when testing whether a variable or argument that defaults to None was set to some other value. The other value might have a type (such as a container) that could be false in a boolean context!


None is singleton

```

a = None
b = None
>>> id(a)
10735616
>>> id(b)
10735616

```

The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behaviour of Python in this case is undefined. :-)

```

# a and b has the same memory address
>>> a = -5
>>> b = -5
>>> id(a)
10853440
>>> id(b)
10853440

>>> a = -6
>>> b = -6
>>> id(a)
140661196486640
>>> id(b)
140661196486608
```