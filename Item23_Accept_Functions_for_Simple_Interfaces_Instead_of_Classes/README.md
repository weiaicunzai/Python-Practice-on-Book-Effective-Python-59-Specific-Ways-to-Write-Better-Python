
# Accept	Functions	for	Simple	Interfaces	Instead	of Classes

* Instead	of	defining	and	instantiating	classes,	functions	are	often	all	you	need	for simple	interfaces	between	components	in	Python

if I want to print 'missing' each time a missing key is accessed

```
def print_missing():
    print('missing')
    return 0

test = {'a': 1, 'b': 2}
d = defaultdict(print_missing, test)
print(d['d'])


>>>missing
>>>0
```


If I want to count the total number of keys that were missing, use stateful closure
```
current = {'green': 12, 'blue':3}
increments = [
    ('red', 15),
    ('blue', 17),
    ('orange', 9)
]

def increment_with_report(current, increments):
    added_count = 0
    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, value in increments:
        result[key] = value

    return result, added_count

increment_with_report(current, increments)
```

but stateful closure is harder to read, we can use a class to encasulates the state you want to track

```
class CountMissing(object):
    def __init__(self):
        self.count = 0

    def missing(self):
        self.count += 1
        print(self.count)
        return self.count

counter = CountMissing()

current = {'green': 12, 'blue':3}
increments = [
    ('red', 15),
    ('blue', 17),
    ('helo', 22)
]
result = defaultdict(counter.missing, current)
```

the problem is, in isolation it's not immediately obvious what the purpose of the CountMissing class is utill you see the usage with defaultdict.

```
# a better approach is to use __call__ method

class BetterCountMissing:
    def __init__(self):
        self.count

    def __call__(self):
        self.count += 1
        return 0

counter = BetterCountMissing()
result = defaultdict(counter, current)

for key, value in increments:
    counter[key] = value
```