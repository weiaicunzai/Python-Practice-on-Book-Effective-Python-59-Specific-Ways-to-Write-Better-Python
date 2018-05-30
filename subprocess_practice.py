import subprocess



proc = subprocess.Popen(['ls', '-la'])


#subprocess.run('ls, -la', shell=True)

subprocess.run(['ls', '-la'])


#time out
#subprocess.run('ping www.baidu.com', shell=True, timeout=3)
cmd = ['ping', 'www.baidu.com']
subprocess.run(cmd, shell=True, timeout=1)
#subprocess.run(cmd, timeout=5)

import select
import time

def slow_systemcall():
    select.select([], [], [], 0.3)


start = time.time()

for i in range(5):
    slow_systemcall()
end = time.time()

print(end - start)


from threading import Thread

start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    for i in range(5):
        compute_helicopter_location(i)


def hello(age):
    for i in range(100):
        print('age is {}'.format(age))


threads = []
for i in range(4):
    thread = Thread(target=hello, args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()
    thread.join()

    

