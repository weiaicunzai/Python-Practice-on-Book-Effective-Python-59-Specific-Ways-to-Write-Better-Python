
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


#class A:
#
#    def __init__(self):
#        self.name = 'ffffff'
#
#    def hello(self):
#        return 'fff'

#class B:
#    pass
#
#class C(B):
#    pass
#class D(A, C):
#    pass
#
#d = D()
#print(isinstance(d, B))
#print(isinstance(d, A))
#
#a = A()
#print(hasattr(A, '__dict__'))
#print(a.__dict__)

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

print()

class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parents):
        self.name = name
        self.tree_with_parents = tree_with_parents

my_tree = NamedSubTree('test', root)
print(my_tree.to_dict())


import json

class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict)

class Data(ToDictMixin, JsonMixin):
    pass