# Inherit	from	collections.abc	for	Custom Container	Types

* Inherit	directly	from	Python’s	container	types	(like	list	or	dict)	for	simple	use cases.

```


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1

        return counts

foo = FrequencyList(['f', 'b', 'c', 'd', 'c', 'a'])
print(len(foo))
print(foo.frequency())

```

* Beware	of	the	large	number	of	methods	required	to	implement	custom	container types	correctly.
```
class Test:
    def __init__(self):
        self.a = range(100)
    def __getitem__(self, index):
        return self.a[index]

    def __len__(self):
        return len(self.a)
t = Test
# error
# t.index(3)
# t.count(5)
```
* Have	your	custom	container	types	inherit	from	the	interfaces	defined	in collections.abc	to	ensure	that	your	classes	match	required	interfaces	and behaviors.

```

from collections.abc import Sequence

class Test1(Sequence):
    def __init__(self):
        self.a = range(100)

    def __getitem__(self, index):
        return self.a[index]

    def __len__(self):
        return len(self.a)
t1 = Test1()
print(t1.index(44))
print(t1.count(23))
```