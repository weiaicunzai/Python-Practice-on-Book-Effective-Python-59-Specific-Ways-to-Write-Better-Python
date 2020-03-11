# Know	How	Closures	Interact	with	Variable	Scope

* closure

```
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)
```

* want to see whether higher-priority items were seen at all

No:
```
def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found
```

Yes:
```
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
```


* if function get complicated, don't use nonlocal, warp your state in a help class:

```
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True

            return (0, x)
        return (1, x)
```