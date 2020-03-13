
def log_missing():
    print('missing key--------------------------------')
    return 0

current = {'green': 12, 'blue':3}
increments = [
    ('red', 15),
    ('blue', 17),
    ('orange', 9)
]

from collections import defaultdict

import numpy as np
c = defaultdict(list)

# c['hhhh'] will get
print(c['hhhh'])

d = defaultdict(log_missing)

d['hh'] += 10
print(d)
d['cc']
print(d)

current.setdefault('jj', 1111111)
current.setdefault('ff', 13333)
print(current)


#count the total number of keys that were missing
current = {'green': 12, 'blue':3}
increments = [
    ('red', 15),
    ('blue', 17),
    ('orange', 9)
]

def count_missing_keys(current, increments):
    add_counts = 0

    def missing():
        nonlocal add_counts
        add_counts += 1
        print('missing counts are {}'.format(add_counts))
        return add_counts

    result = defaultdict(missing, current)
    for key, value in increments:
        #result[key] = value doesnt call missing function
        #result[key] or result[key] += value does
        result[key] += value
    result[1] = 10
    print(result)
count_missing_keys(current, increments)

current = {'green': 12, 'blue':3}
increments = [
    ('red', 15),
    ('blue', 17),
    ('orange', 9)
]


def increment_with_report(current,	increments):
    added_count = 0
    def missing():
        nonlocal   added_count  # Stateful	closur
        added_count +=   1
        print(1111)
        return 0
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key]
    return result, added_count

increment_with_report(current, increments)

print("=" * 30)

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

for key, value in increments:
    result[key] += value



print(callable(CountMissing))
print(callable(list))

class Test:
    def __call__(self):
        print('hello')

print(callable(Test()))
print(callable(object))


a = defaultdict(Test(), current)
print(a)


class BetterCountMissing:

    def __init__(self):
        self.added = 0

    def __call__(self):
        print('here')
        self.added += 1
        return 0


b = BetterCountMissing()
b()

def print_missing():
    print('missing')
    return 0

print()
test = {'a': 1, 'b': 2}
d = defaultdict(print_missing, test)
print(d['d'])