# Python3 str type

Instances	of	str	contain	Unicode characters

```
# unicode character
text = 'fjskal j!;;'
```

# Python3 bytes type
Instances of bytes contain encoded(utf-8 encoded) unicode raw 8-bit value


OK:
```
b = b'skxj;f'
```

NO:
```
>>> b = b'Ü'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.

>>> text = 'Ü'
>>> b = text.encode()
>>> b
b'\xc3\x9c'
```



str ===(encode(utf-8, utf-16, etc.))====> bytes
bytes ===(decode(utf-8, utf-16, etc.))====> str
