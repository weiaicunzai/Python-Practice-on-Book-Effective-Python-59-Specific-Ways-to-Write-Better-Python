# Consider	Generator	Expressions	for	Large Comprehensions

* List	comprehensions	can	cause	problems	for	large	inputs	by	using	too	much memory, e.g. network sockets


```
it = (len(x)	for	x	in	open(‘/tmp/my_file.txt’))
print(it)>>>
<generator	object	<genexpr>	at	0x101b81480>
```