# ## Defining a list
# lst=[]
# print(lst)

# ## Element in a list (string, Numbers and boolean)
lst = ["mango","apple", 1,2,3,True]
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

# ## List operations
# append : append() adds an element at the end of the list
# insert : insert() adds and element at specified index
# extends : extend() adds multiple elements to the list.
# remove : remove() removes the specified value
# pop : pop() removes element based on index. If index is not given, pop() removes the last element
# clear : clear() removes all elements from the list.
# del : del can delete an element or entire list.
# sort : Sort the fruits based on the name
# count : Count the occurences of item in a list


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

# ## Reverse of a list
# lst.reverse()
# print(lst)

# ## Clearin the list
# lst.clear()
# print(lst)

## Delete the list
#del(lst)
print(lst)

# ## Extend items in a list by appending another list
fruits=['banana','orange','kiwi','watermelon','apple']
# lst.extend(fruits)
# print(lst)

# ## Count the occurances of item in a list
# lst.append('banana')
# print(lst.count('banana'))

# ## Sort fruits based on the item
# print(lst)
# lst.sort()
# print(lst)

# ## Count the items in the list
# num = lst.count('banana')
# print(num)

#### List functions

#Length,Min, Max, Sort, sum of the list
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sorted(numbers))
# print(sum(numbers))

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
# Enumerate takes an iterable(list,string,tuple) and returns an iterator that produces a pair
## Start from a specific index number
# for num,item in enumerate(fruits,start=1):
#     print(num,item)

## List comprehension

#** List comprehension is a short and clean way to create a new list from an existing sequence like range, list, tuple, or string.

#** It is mainly used to reduce multiple lines of loop code into a single line.

## Print Range from 1 to 6
# normal way
# numbers = []
# for i in range(1,6):
#     numbers.append(i)

# Basic Syntax [expression for item in iterable]
numbers = [x for x in range(1,6)]
#print(numbers)

# square of numbers in normal way
# squares = []
# for i in range(1,6):
#     squares.append(i*i)
# print(squares)

# ## Basic Syntax [expression for item in iterable]
# lst=[x**2 for x in range(10) ]
# print(lst)

# ## Basic Syntax with Logic [expression for item in iterable if condition]
# lst=[x**2 for x in range(10) if x % 2 == 0]
# print(lst)

# Even Numbers
#  normal way
# even_numbers = []
# for i in range(1,11):
#     if i % 2 == 0:
#      even_numbers.append(i)
# print(even_numbers)

# list comprehension
even_numbers = [i for i in range(1,11) if i % 2 == 0]
print(even_numbers)

# ## Basic Syntax with Logic [expression for item in iterable if else condition]
marks = [80, 30, 90, 45, 20]
results = [ "PASS" if x > 35 else "FAIL" for x in marks]
print(results)


# ## Nested list comprehension [expression for item in iterable for item2 in iterable]
# lst=[x * y for x in range(1,5) for y in range(1,10)]
# print(lst)

## List comprehension with function calls

fruits=['banana','orange','kiwi','watermelon','apple','mango', 'guava']
length=[len(item) for item in fruits]
print(length)

## Convert to lower case List.lower(), Similarly for upper list.upper()
courses = ["JAVA", "Python", "DevOps", "GEN AI"]
lowers = [ x.lower() for x in courses ]
print(lowers)