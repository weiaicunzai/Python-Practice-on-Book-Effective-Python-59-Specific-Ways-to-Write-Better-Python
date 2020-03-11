# Consider	Generators	Instead	of	Returning	Lists

* The	simplest	choice	for	functions	that	produce	a	sequence	of	results	is	to	return	a	list	of items.

No:
```
def	index_words(text):
    result	=	[]
    if	text:
        result.append(0)
    for	index,	letter	in	enumerate(text):
        if	letter	==	‘	‘:
            result.append(index	+	1)
    return	result
```

* reaturn iterator instead of list

Yes:
```
    def index_words_iter(text):
        if text:
            yield 0
        for index, letter in enumerate(text):
            if letter == ' ':
                yield index + 1
```