# Be	Defensive	When	Iterating	Over	Arguments

* iterable vs iterator vs generator

iterator is a stricter concept than iterable

**iterable**: An object capable of returning its members one at a time. e.g.: list, dict, tuple, str, iterator.......

**iterator**: An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its __next__() method just raise StopIteration again. Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. **A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.**



a iterator pass to iter()
```
# iterator
a = (x for x in range(10))
b = a
c = a
print(b is c)
print(id(b))
print(id(c))
print()
```
output:
```
# pass an iterator to iter() function produces the same
# iterator object
True
139951197519808
139951197519808
```
container pass to iter()
```
# pass an container(list) to iter() function produces the a
# fresh new iterator object each time

a = [x for x in range(10)]
print(a)
b = iter(a)
c = iter(a)
print(b is c)
print(id(b))
print(id(c))
```
output:
```
False
140153409939720
140153409939888
```
**generator**: generator is a iterator

* iterate over argument could cause bug

```
No:
def normalize(numbers):

    # iterate through numbers the 1st time
    total = sum(numbers)
    result = []

    # iterate through numbers the 2nd time
    # if numbers is an iterator
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result
```

Yes:
```
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
```

* always use ```is``` to compare object than ```id()```

```
a = [0, 1, 2]

print(iter(a))
print(iter(a))
print(iter(a) is iter(a))
```