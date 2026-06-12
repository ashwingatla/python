# # List - Collection of hetrogenous elements which is mutable
# list1=[10,20,30,40,50]
# print(list1[1],list1[-5])
# print(list1[0:3])
# print(list1[::-1])

#**************************************************************************************************

# Tuple - 
#   Collection of hetrogenous elements which is immutuable
#   Takes less memory compared to list
#   Faster compared to list
#   Represented in Braces

# import sys
# list1=[10,20,30,40,50,60]
# tuple1=(10,20,30,40,50,60)
# print(sys.getsizeof(list1))
# print(sys.getsizeof(tuple1))
# list1 = [10,"hello",True]
# tuple1 = (10,"Gen AI",10.1)
# print(type(list1),end=" | ")
# print(type(tuple1),end=" | ")

#**************************************************************************************************

# Dictionary
#   Key and Value Pairs
#   Represent in {} and dict constructor
#   Values are mutable and Keys are Immutable

# details = {"name" : "Gen AI", "ver" : 2}
# print(details["name"])
# details["name"] = "Agentic AI"
# print(details)
# print(type(details))
# print(details.keys())
# print(details.values())

#**************************************************************************************************
# Set
#   Wont allow duplicates
#   {} is the syntax

# s1 = {10,20,30,10,20,30}
# print(s1)
# print(type(s1))
# s2 = set()
# print(type(s2))
# s3 = set([10,20,30,10,20,30])
# print(s3)
# s4 = set((10,20,30,10,20,30))
# print(s4)

#**************************************************************************************************

# None Data type
# import sys
# x = None
# print(x)
# print(sys.getsizeof(x))
# print(x==x)
# print(x==0)

#**************************************************************************************************
#Division
print(5/2) # Division
print(5//2) # Floor Division
print(10%3) # Percentage
x="10"
y=2
print(int(x) + y)
print(int(x) * y)