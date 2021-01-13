x = (i for i in range(5))
x.__next__()
x.__next__()
for i in x:
    print(i)
