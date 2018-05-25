""" practice for concurrent.futures module
using gcd  example
"""

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers	=	[(1963309,	2265973),	
                (2030677,   3814172),
                (1551645,	2229620),
                (2039045,	2020802)]

from time import time


#plain function  
start = time()
results = list(map(gcd, numbers))
end = time()
print("time1")
print(end - start)

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

#using thread
start = time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()

print("time2")
print(end - start)


#using process
start = time()
pool = ProcessPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()

print("time3")
print(end - start)