x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

# Let's first combine x and y:

for a,b in zip(x,y):
    print(a,b)


names = ['Jill','Jack','Jeb','Jessica']
grades = [99,56,24,87]

d = dict(zip(names,grades))
print(d)
