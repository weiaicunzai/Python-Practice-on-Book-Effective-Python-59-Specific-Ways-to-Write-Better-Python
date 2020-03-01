from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',
                          keep_blank_values=True)
print(repr(my_values))


# get values from dictionary my_values

print('Red:      ', my_values.get('red'))
print('Green:    ', my_values.get('green'))
print('Opacity:  ', my_values.get('opacity'))


# result:
# Red:       ['5']
# Green:     ['']
# Opacity:   None


# if we need to set a default value when value is None or empty
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print()
print('Red:     %r'	%	red)
print('Green:   %r'	%	green)
print('Opacity: %r'	%	opacity)

# if we need to reaturn an int value
red	= int(my_values.get('red',	[''])[0]	or	0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)

print()
print('Red:     %r'	%	red)
print('Green:   %r'	%	green)
print('Opacity: %r'	%	opacity)


# the code above is extremely hard to read
# warp all this into a helper function


def get_first_int(values, key, default=0):

    #res = values.get(key, [''])[0]

    #if res:
    #    return res
    #else:
    #    return default

    found = values.get(key, [''])

    if found[0]:
        found = int(found[0])
    else:
        found = default

    return found