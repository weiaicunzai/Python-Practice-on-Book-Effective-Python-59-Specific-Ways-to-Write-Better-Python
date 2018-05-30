
from threading import Thread

class InputData:
    def read(self):
        raise NotImplementedError


#class PathInputData(InputData):
#    def __init__(self, path):
#        super().__init__()
#        self.path = path
#    
#    def read(self):
#        return 'some data\n sdfds \n' + self.path






class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result =None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError
    


#class LineCountWorker(Worker):
#    def map(self):
#        data = self.input_data.read()
#        self.result = data.count('\n')
#    
#    def reduce(self, other):
#        self.result += other.result



def generate_inputs():
    for i in range(10):
        yield PathInputData(str(i))

def create_worker(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

def	execute(workers):
				threads	=	[Thread(target=w.map)	for	w	in	workers]
				for	thread	in	threads:	thread.start()
				for	thread	in	threads:	thread.join()
				first,	rest	=	workers[0],	workers[1:]
				for	worker	in	rest:
								first.reduce(worker)
				return	first.result


class GenericInputData(object):
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class GenericWorker(object):
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError
    
    @classmethod
    def create_worker(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result =None
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
    
    def reduce(self, other):
        self.result += other.result

import os

class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        return 'some data\n sdfds \n' + self.path
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(name)

