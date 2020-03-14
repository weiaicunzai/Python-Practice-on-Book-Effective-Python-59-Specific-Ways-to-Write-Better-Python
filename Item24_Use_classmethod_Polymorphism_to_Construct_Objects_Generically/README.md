# Item	24:	Use	@classmethod	Polymorphism	to	Construct Objects	Generically

* Use	@classmethod	to	define	alternative	constructors	for	your	classes.

```
class GenericWorker(object):
    def __init__(self, input_data):
        self.result = None
        self.input_data = input_data

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_worker(cls, input_class, file_dir):
        workers = []
        for input_data in input_class.generate_inputs(file_dir):
            # the instance of GenericWorker class
            workers.append(cls(input_data))
        return workers
```