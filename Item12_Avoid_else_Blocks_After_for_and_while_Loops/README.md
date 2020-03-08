# Avoid	else	Blocks	After	for	and	while	Loops

* Avoid	using	else	blocks	after	loops	because	their	behavior	isn’t	intuitive	and	can be	confusing.

No:
```
a =	4
b =	9
for	i in range(2, min(a, b)	+ 1):
    print(‘Testing’, i)
    if a % i ==	0 and b	% i == 0:
        print(‘Not coprime’)
        break
else:
    print(‘Coprime’)
```