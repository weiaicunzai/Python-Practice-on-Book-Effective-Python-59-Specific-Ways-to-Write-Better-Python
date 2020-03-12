

* Default	argument	values are only evaluated once per module loaded

No:
```
def log(msg, when=datetime.now()):
    print('%s, %s' % (msg, when))

log(‘Hi	there!’)
sleep(0.1)
log(‘Hi	again!’)

2014-11-15	21:10:10.371432:	Hi	there!
2014-11-15	21:10:10.371432:	Hi	again!
```

**datetime.now() will only be evaluated once when module loading**

Yes:
```
def	log(message,	when=None):
    “““Log	a	message	with	a	timestamp.
    Args:
        message:	Message	to	print.
        when:	datetime	of	when	the	message	occurred.
                Defaults	to	the	present	time.
    ”””
    when	=	datetime.now()	if	when	is	None	else	when
	print(‘%s:	%s’	%	(when,	message))
```

* default	argument values	are	only	evaluated	once	(at	module	load	time), so default will always point to ```{}```, and since ```{}``` is mutable, this will cause extremely confusing results

No:
```
def	decode(data, default={}):
    try:
        return	json.loads(data)
    except	ValueError:
        return	default

# foo, bar and {} are the same dictionary
foo	=	decode(‘bad	data’)
foo[‘stuff’]	=	5
bar	=	decode(‘also	bad’)
bar[‘meep’]	=	1
print(‘Foo:’,	foo)
print(‘Bar:’,	bar)
>>>
Foo: {‘stuff’:	5,	‘meep’:	1}
Bar: {‘stuff’:	5,	‘meep’:	1}
```

Yes:
```
def	decode(data,	default=None):
    “““Load	JSON	data	from	a	string.
    Args:
    	data:	JSON	data	to	decode.
    	default:	Value	to	return	if	decoding	fails.
    					Defaults	to	an	empty	dictionary.
    ”””
    if	default	is	None:
    	default	=	{}
    try:
    	return	json.loads(data)
    except	ValueError:
    	return	default
```