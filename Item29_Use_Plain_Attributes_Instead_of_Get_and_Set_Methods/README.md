# Use	Plain	Attributes	Instead	of	Get	and	Set Methods


* Use	@property	to	define	special	behavior	when	attributes	are	accessed	on	your objects,	if	necessary.

```
class Counter:
    def __init__(self, count):
        self._count = count


    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value > 0:
            self.value = value
        else:
            raise ValueError('value should be greater than 0'
```