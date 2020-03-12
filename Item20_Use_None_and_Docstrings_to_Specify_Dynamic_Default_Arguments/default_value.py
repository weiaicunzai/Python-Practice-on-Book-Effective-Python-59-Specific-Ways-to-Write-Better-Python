import json

def decode(data, default=[1, 2, 3]):

    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('hello')
foo.append(1)
print(foo)


bar = decode('he')
bar.append(2)
print(bar)
#foo = decode('bad data')
#foo['stuff'] = 5
#bar = decode('also bad')
#bar['meep'] = 1
#print(foo)
#print(bar)

a = [1, 2, 3]
print(id(a))
a.append(1)
print(id(a))


a = (1, 3)
print(id(a))
print(id(a))