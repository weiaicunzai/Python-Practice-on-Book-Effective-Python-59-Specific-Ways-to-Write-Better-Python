# Use	Multiple	Inheritance	Only	for	Mix-in	Utility Classes


Basically, a mixin is a stand-alone base type that provides limited functionality and polymorphic resonance for a child class. If you're thinking in C#, think of an interface that you don't have to actually implement because it's already implemented; you just inherit from it and benefit from its functionality.

If you want to serialize your custom data types to json, you could use mixin class to achieve this, instead of implementing serialization method for each of your custom types.

* Use	pluggable	behaviors	at	the	instance	level	to	provide	per-class	customization when	mix-in	classes	may	require	it.

```

class ToDictMixin:

    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}

        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)

        return output

    def _traverse(self, key, value):

        # if value is a TodictMixin object
        if isinstance(value, ToDictMixin):
            return value.to_dict()

        # if value is also a dictionary
        elif isinstance(value, dict):
            return self._traverse_dict(value)

        # if value is a list
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]

        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(
    10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, right=BinaryTree(11))
)

print(tree.to_dict())

>>>{'left': {'left': None, 'value': 7, 'right': {'left': None, 'value': 9, 'right': None}}, 'value': 10, 'right': {'left': None, 'value': 13, 'right': {'left': None, 'value': 11, 'right': None}}}




class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and
                key == 'parent'):
            return value.value

        else:
            return super()._traverse(key, value)


root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)

print(root.to_dict())

{'tree_with_parents': {'left': {'left': None, 'parent': 10, 'value': 7, 'right': {'left': None, 'parent': 7, 'value': 9, 'right': None}}, 'parent': None, 'value': 10, 'right': None}, 'name': 'test'}
```

* Compose	mix-ins	to	create	complex	functionality	from	simple	behaviors.

```
import json

class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict)

# serialize data
class Data(ToDictMixin, JsonMixin):
    pass
```