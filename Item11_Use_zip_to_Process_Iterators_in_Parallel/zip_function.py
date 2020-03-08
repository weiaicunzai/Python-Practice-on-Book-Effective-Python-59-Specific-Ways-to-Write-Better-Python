from itertools import zip_longest

names = ['xiaoming', 'xiaohong', 'xiaozhang']
ages = [12, 13, 14]

# No

for idx in range(len(names)):
    print(names[idx], ages[idx])


# Yes

for name, age in zip(names, ages):
    print(name, age)
print()



names.append('xiaobai')
for name, age in zip(names, ages):
    print(name, age)
print()

for name, age in zip_longest(names, ages):
    print(name, age)