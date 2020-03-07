# Prefer	enumerate	Over	range

* when you need to iterate over a sequence and know the index of current item in the list

Yes:
```
a = ['a', 'b', 'c', 'd']

for index, item in enumerate(a):
    print(index, item)

```

No:
```
a = ['a', 'b', 'c', 'd']

for index in range(len(a)):
    print(index, a[index])
```

* You	can	supply	a	second	parameter	to	enumerate	to	specify	the	number	from which	to	begin	counting	(zero	is	the	default).

```
>>> a = ['a', 'b', 'c', 'd']
>>> for i, item in enumerate(a, 2):
...     print(i, item)
...
2 a
3 b
4 c
5 d
```