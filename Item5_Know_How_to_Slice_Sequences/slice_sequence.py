
a = list(range(10))

print(a)

print('First	four:',	a[:4])
print('Last	four:',	a[-4:])
print('Middle	four:',	a[3:-3])


# All of these forms of slicing would be clear to a new reader of your code.
# I	encourage you to use these	variations.

print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])
print()


# when start and end are beyound boundary
print('when start and end are beyound boundary...')
print(a[:100])
print(a[-100:])
print(a[100:])
print()

# the result of a slice is a whole new slice

b = a[3:]

print('before')
print(a)
print(b)


#############################
# modify the value in b won't change the
# result in a

b[0] = 1000

print('after')
print(a)
print(b)
print()

#############################
# when used in assignment, slice will replace
# the original list
print('before assignment: ')
print('a: ', a)
print('b: ', b)

a[:3] = [100, 200, 300]
print('after assignment: ')
print('a: ', a)
print('b: ', b)
print()


#############################
# The list will grow or shrink to accommodate
# the new values

a = list(range(10))
print('a: ', a)

# a will shrink
a[:5] = [33, 44]
print('shrinked a: ', a)
print('length: ', len(a))

a = list(range(10))

# a will growth
a[:5] = [33, 44, 55, 66, 77, 88, 99, 9999]
print('growth: ', a)
print('length: ', len(a))
print()


#############################
# get a copy of original list
b = a[:]