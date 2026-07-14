## Tuples are orders collection of items that are immutable

capitals=['delhi','hyderbad','chennai','mumbai','bangalore','kolkota']
tup=(1,2,3,4,5,6)
tup1=('mango','orange','watermelon','apple','mango')
# print(tup1)

# ## Convert list to a tuple
captls=tuple(capitals)
# print(captls)

# ## Accessing Tuple elements
# print(captls[0])
# print(captls[-1])

# ## Slicing operations
# print(captls[0:4])

## Concatenation
# concat = captls + tup1
# print(concat)

##  Find the number of occurences of an element

# print(tup1.count('mango'))

# ## Find the index of a element

# print(tup1.index('mango'))

# ## Packing tuples

# vehicles = 'car','bus','auto','train'

# print(vehicles)
# ## Unpacking tuples

# a,b,c,d = vehicles
# print(a)
# print(b)
# print(c)

# ## Unpacking based on wild card(*)
# a,*b,c = vehicles
# print(a)
# print(b)
# print(c)

nested_tuple=(captls,tup,tup1)
print(nested_tuple)

## Iterating over nested tuples

for item_list in nested_tuple:
    for item in item_list:
        print(item,end=' ')
    print()