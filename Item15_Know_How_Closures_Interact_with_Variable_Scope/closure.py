
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    #return

# want to see whether higher-priority
# items were seen at all
# wrong
def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found

# use nonlocal statement
# (only use nonlocal in simple functions)
def sort_priority3(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found


# if function get complicated, don't
# use nonlocal, warp your state in a
# help class:
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True

            return (0, x)
        return (1, x)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


print()

test = [1, 2, 3, 4, 5]
def hello(values):

    # operate on test
    values.append(1111111111111)

    # bound values to another object([])
    values = []

hello(test)
print(test)