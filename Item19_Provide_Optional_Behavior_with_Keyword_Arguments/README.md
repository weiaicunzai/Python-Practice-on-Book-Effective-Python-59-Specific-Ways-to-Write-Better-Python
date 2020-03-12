Provide	Optional	Behavior	with	Keyword Arguments

* Function arguments can be specified by position	or by keyword

```
def remainder(number, divisor):
    return number % divisor
```

Yes:
```
remainder(divisor=7, number=20)
```
1. The	first	advantage	is	that	keyword	arguments	make	the	function	call	clearer	to	new readers	of	the	code.

2. The	second	impact	of	keyword	arguments	is	that	they	can	have	default	values	specified	in the	function	definition.

```
flow_per_hour = flow_rate(weight_diff,	time_diff,	period=3600)
```

3. The third reason is that keyword parameters provide a powerful way to extend a function's parameters while remaining backwards comaptible with existing callers.

```
flow_per_hour = flow_rate(weight_diff,	time_diff,	period=3600, units_per_kg=1)
```