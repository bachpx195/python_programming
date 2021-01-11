# generator expression

# xyz = (i for i in range(500000))
# print(list(xyz)[:5])

input_list = [5,6,2,1,6,7,10,12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))

# list comprehension

# xyz = [i for i in range(500000)]
# print(xyz[:5])

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)

# These look and appear to act very similarly, but they are quite different under the hood. First, with a generator, the values are generated from an original input, but the values are not copied and instead are generated on-the-fly. This means we will use far less memory, since the entire list is not processed all at once, but also means the process is a bit slower, since things are indeed generated as we go.

# The list comprehension puts the entire list into memory, so it is faster, but the penalty is memory use.
