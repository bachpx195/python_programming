def simple_gen():
    yield 'Oh'
    yield 'Hello'
    yield 'Three'

for i in simple_gen():
    print(i)
