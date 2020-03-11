
# wrong result if numbers is a iterator
def normalize(numbers):

    # iterate numbers 1st time
    total = sum(numbers)
    result = []

    # iterate numbers 2nd time
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result



# pass an iterator to iter() function produces the same
# iterator object
a = (x for x in range(10))
print(a)
b = a
c = a
print(b is c)
print(id(b))
print(id(c))
print()


# pass an container(list) to iter() function produces the a
# fresh new iterator object each time
a = [x for x in range(10)]
print(a)
b = iter(a)
c = iter(a)
print(b is c)
print(id(b))
print(id(c))


print()
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
