# Write	Helper	Functions	Instead	of	Complex


* Python’s	syntax	makes	it	all	too	easy	to	write	single-line	expressions	that	are	overly
complicated	and	difficult	to	read.

* Move	complex	expressions	into	helper	functions,	especially	if	you	need	to	use	the
same	logic	repeatedly.

* The	if/else	expression	provides	a	more	readable	alternative	to	using	Boolean
operators	like	or	and	and	in	expressions.

```
a = condition_a or condition_b

if condition_a:
   a = 10
else:
   a = 100
```