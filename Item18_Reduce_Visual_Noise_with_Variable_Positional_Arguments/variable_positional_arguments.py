
def log(msg, values):
    if not values:
        print(msg)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(msg, value_str)

def log1(msg, *values):
    if not values:
        print(msg)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(msg, value_str)


log('hello', [1, 3, 5])
# looks cumbersome and noisy
log('hello', [])

print()
log1('hello')