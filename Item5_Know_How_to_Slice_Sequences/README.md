# Know	How	to	Slice	Sequences

* Avoid	being	verbose:	Don’t	supply	0	for	the	start	index	or	the	length	of	the sequence	for	the	end	index.

* Assigning	to	a	list	slice	will	replace	that	range	in	the	original	sequence	with
what’s	referenced	even	if	their	lengths	are	different.

* The list	will	grow	or	shrink	to	accommodate	the	new	values.

* The result of a slice is a whole new slice
