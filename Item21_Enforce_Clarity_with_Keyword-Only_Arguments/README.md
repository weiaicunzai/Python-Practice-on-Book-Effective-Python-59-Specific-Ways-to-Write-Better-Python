# Enforce	Clarity	with	Keyword-Only	Arguments

No:
```
def parse_file(file, parse_text, parse_table)
```

1. easy to confuse the position of the two Boolean arguments that control the parsing behavior
```
parse_file(file, True, False)
parse_file(file, False, True)
```

2. if we add more paramters later:
```
def parse_file(file, parse_text, parse_table, parse_A, parse_B)
```
this would looks extremely crumbersome


we could do this:
```
def parse_file(file, parse_text=True, parse_table=True)
```
but the caller could still use this
```
parse_file(file, False, True)
```


force the caller to know their intention:
```
def parse_file(file, *, parse_text=True, parse_table=True)
```

then:
```
parse_file(file, True, False) # error
parse_file(file, parse_table=False) # ok
```
