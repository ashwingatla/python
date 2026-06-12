## Defining a list
lst=[]
print(lst)

## Element in a list (string, Numbers and boolean)
lst = ["ash","win", 1,2,3,True]
print(lst)

## Access elements in a list using indexes
print(lst[0])


## Access elements in a list using negative indexes(picks element from the right)
print(lst[-1])

## Access range of elements in a list 
print(lst[0:2])

## Modifying elements in a list
lst[1] = "gatla"
print(lst)

## List methods
# Append
lst.append("win")
print(lst)

#insert
lst.insert(2,10)
print(lst)

# Remove an item from the list(Removes 1st occurence)
lst.remove('ash')
print(lst)

# Remove an item from the list(Removes 1st occurence) and returns the item
dlt_item = lst.pop(0)
print(dlt_item)

## Get the index of an item in the list
index = lst.index('win')
print(index)
print(lst)
## Count the items in a list
lst.insert(1,"win")
print(lst)
print(lst.count(2))

## Reverse of a list
lst.reverse()
print(lst)

## Clearin the list
lst.clear()
print(lst)