# Use	zip	to	Process	Iterators	in	Parallel

* The	zip	built-in	function	can	be	used	to	iterate	over	multiple	iterators	in	parallel.

names = ['xiaoming', 'xiaohong', 'xiaozhang']
ages = [12, 13, 14]

No:

```
for idx in range(len(names)):
    print(names[idx], ages[idx])
```

# Yes

```
for name, age in zip(names, ages):
    print(name, age)
```

* zip will stop when one of the wrapped iterator is exhausted

```
names.append('xiaobai')
for name, age in zip(names, ages):
    print(name, age)
```
output:
```
xiaoming 12
xiaohong 13
xiaozhang 14
```

* itertools.zip_longest allow you to iterate over multiple iterators regardless of their lengths

```
from itertools import zip_longest

for name, age in zip_longest(names, ages):
    print(name, age)
```

output:
```
xiaoming 12
xiaohong 13
xiaozhang 14
xiaobai None
```