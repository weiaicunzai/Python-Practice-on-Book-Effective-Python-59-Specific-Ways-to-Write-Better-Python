# Avoid	Using	start,	end,	and	stride	in	a	Single Slice

somelist[start:end:stride]

* stride often cause unexpected behavior, breaks when dealing with utf-8 encoded UNICODE character

OK:
```
>>> x = b'ksjf'
>>> x[::-1]
b'fjsk'
>>>
```

ERROR:
```
>>> x = '翻译'
>>> x = x.encode()
>>> x = x[::-1]
>>> x.decode()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x91 in position 0: invalid start byte
```


* use start, end, stride together is confusing

NO:
```
a = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’]
a[2::2]			#[‘c’,	‘e’,	‘g’]
a[-2::-2]		#[‘g’,	‘e’,	‘c’,	‘a’]
a[-2:2:-2]		#[‘g’,	‘e’]
a[2:2:-2]		#[]
```
Yes:
```
a[::2]		#	[‘a’,	‘c’,	‘e’,	‘g’]
a[::-2]		#	[‘h’,	‘f’,	‘d’,	‘b’]
```


* if you have to use start, end, and stride

Yes:
```
b	=	a[::2]		#	[‘a’,	‘c’,	‘e’,	‘g’]
c	=	b[1:-1]		#	[‘c’,	‘e’]
```

Or use itertool's islice method, but islice do not accept negative start, end or stride value