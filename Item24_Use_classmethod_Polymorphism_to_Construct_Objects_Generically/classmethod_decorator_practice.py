
import os
import time
from glob import iglob
from threading import Thread

#class InputData:
#    def read(self):
#        raise NotImplementedError
#
#class PathInputData(InputData):
#    def __init__(self, path):
#        super().__init__()
#        self.path = path
#
#    def read(self):
#        try:
#            with open(self.path, 'rt') as f:
#                return f.read()
#        except (UnicodeDecodeError, IsADirectoryError):
#            return ''
#
#class Worker(object):
#    def __init__(self, input_data):
#        self.input_data = input_data
#        self.result = None
#
#    def map(self):
#        raise NotImplementedError
#
#    def reduce(self, other):
#        raise NotImplementedError
#
#class LineCountWorker(Worker):
#    def map(self):
#        data = self.input_data.read()
#        self.result = data.count('\n')
#
#    def reduce(self, other):
#        self.result += other.result
#
#def generate_inputs(data_dir):
#    for name in iglob(os.getcwd()+'/**/*', recursive=True):
#        yield PathInputData(os.path.join(data_dir, name))
#
#def create_worker(input_list):
#    workers = []
#    for input_data in input_list:
#        workers.append(LineCountWorker(input_data))
#    return workers
#
#def	execute(workers):
#    threads	= [Thread(target=w.map)	for	w in workers]
#    for	thread	in	threads:
#        thread.start()
#    for	thread	in	threads:	thread.join()
#    #for w in workers:
#    #    w.map()
#
#    first,	rest	= workers[0],	workers[1:]
#    for	worker	in	rest:
#    	first.reduce(worker)
#    return	first.result
#
#def map_reduce(data_dir):
#    inputs = generate_inputs(data_dir)
#    workers = create_worker(inputs)
#
#    return execute(workers)
#
#start = time.perf_counter()
#print(map_reduce(os.getcwd()))
#
#finish = time.perf_counter()
#
#print(round(finish - start, 5))



class GenericInputData(object):

    def __init__(self, path):
        self.path = path

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, file_dir):
        raise NotImplementedError

class PathInputData(GenericInputData):
    #def __init__(self, path):
    #    super().__init__()
    #    self.path = path

    def read(self):
        try:
            with open(self.path) as f:
                return f.read()

        except (UnicodeDecodeError, IsADirectoryError):
            return ''

    @classmethod
    def generate_inputs(cls, file_dir):
        path = os.path.join(os.getcwd(), '**', '*')
        for file_path in iglob(path, recursive=True):
            yield cls(file_path)


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
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

def	execute(workers):
    threads	= [Thread(target=w.map)	for	w in workers]
    for	thread	in	threads:
        thread.start()
    for	thread	in	threads:	thread.join()
    #for w in workers:
    #    w.map()

    first,	rest	= workers[0],	workers[1:]
    for	worker	in	rest:
    	first.reduce(worker)
    return	first.result

def map_reduce(work_class, input_class, file_dir):
    workers = work_class.create_worker(input_class, file_dir)
    return execute(workers)

print(map_reduce(LineCountWorker, PathInputData, os.getcwd()))
#import os
#
#####class PathInputData(GenericInputData):
#####    def __init__(self, path):
#####        super().__init__()
#####        self.path = path
#####
#####    def read(self):
#####        return 'some data\n sdfds \n' + self.path
#####
#####    @classmethod
#####    def generate_inputs(cls, config):
#####        data_dir = config['data_dir']
#####        for name in os.listdir(data_dir):
#####            yield cls(name)
#

#print()
#import time
#
#st = time.perf_counter()
#def print_message():
#    print('start.....')
#    time.sleep(0.5)
#    print('stop.....')
#
#t1 = Thread(target=print_message)
#t2 = Thread(target=print_message)
#
#t1.start()
#t2.start()
#t2.join()
#
#finish = time.perf_counter()
#print('time:', round(finish - st, 3))
#
#
#print()
#
#p = os.path.join(os.getcwd(), '**', '*')
#for i in iglob(p, recursive=True):
#    print(i)
#
#with open('images') as f:
#    print('kk')