from collections import defaultdict


c = defaultdict(list)

c.setdefault(3, 4)
print(c)
c.setdefault(3, 89)
print(c)
for key, value in c.items():
    print(key, value)
    print(type(key), type(value))


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


class Test:
    def __init__(self):
        self.a = range(100)
    def __getitem__(self, index):
        return self.a[index]

    def __len__(self):
        return len(self.a)


t = Test()
print(t[39])
print(len(t))
print(t[3:4])


# error:
# print(t.index(8))

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
print(dir(t1))