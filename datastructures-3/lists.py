# ## Defining a list
# lst=[]
# print(lst)

# ## Element in a list (string, Numbers and boolean)
# lst = ["mango","apple", 1,2,3,True]
# print(lst)

# ## Access elements in a list using indexes
# print(lst[0])

# ## Access elements in a list using negative indexes(picks element from the right)
# print(lst[-1])

# ## Access range of elements in a list 
# print(lst[0:2])

# ## Modifying elements in a list
# lst[1] = "banana"
# print(lst)

# ## List methods
# # Append
# lst.append("orange")
# print(lst)

# #insert
# lst.insert(2,10)
# print(lst)

# # Remove an item from the list(Removes 1st occurence)
# lst.remove('banana')
# print(lst)

# # Remove an item from the list(Removes 1st occurence) and returns the item
# dlt_item = lst.pop(0)
# print(dlt_item)

# ## Get the index of an item in the list
# index = lst.index('orange')
# print(index)
# print(lst)
# ## Count the items in a list
# lst.insert(1,"win")
# print(lst)
# print(lst.count(2))

# ## Reverse of a list
# lst.reverse()
# print(lst)

# ## Clearin the list
# lst.clear()
# print(lst)

# ## Extend items in a list by appending another list
# fruits=['banana','orange','kiwi','watermelon','apple']
# lst.extend(fruits)
# print(lst)

# ## Count the occurances of item in a list
# lst.append('banana')
# print(lst.count('banana'))

# ## Sort fruits based on the item
# print(lst)
# lst.sort()
# print(lst)

# ## Cound the items in the list
# num = lst.count('banana')
# print(num)

# ## Reverse a list
# lst.reverse()
# print(lst)

## Clear the list
# fruits.clear()

# # Slicing Lists
# print(fruits[1:3])

# # Skipping list elements by 1
# print(fruits[::2])

# # Reverse the elements
# print(fruits[::-1])

# # Iterating over a list
# for item in fruits:
#     print(item)

# # Iterating over using index with enumerate
# for num,item in enumerate(fruits):
#     print(num,item)

## List comprehension
# ## Basic Syntax [expression for item in iterable]
# lst=[x**2 for x in range(10) ]
# print(lst)

# ## Basic Syntax with Logic [expression for item in iterable if condition]
# lst=[x**2 for x in range(10) if x % 2 == 0]
# print(lst)

# ## Nested list comprehension [expression for item in iterable for item2 in iterable]
# lst=[x * y for x in range(1,5) for y in range(1,10)]
# print(lst)

## List comprehension with function calls

fruits=['banana','orange','kiwi','watermelon','apple','mango', 'guava']
length=[len(item) for item in fruits]
print(length)