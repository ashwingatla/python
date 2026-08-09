#Immutability: Convert the capitals list into a tuple and demonstrate (in code) that tuples are immutable — show an attempted mutation and handle the resulting situation cleanly.
capitals=['delhi','hyderbad','chennai','mumbai','bangalore','kolkota']
capital_tuple = tuple(capitals)
try:
    capital_tuple[1] = "hydrbad"
except TypeError:
    print("Tuple cannot be modified")


#Indexing & Slicing: Using the capitals tuple, produce a new tuple containing every second city in reverse order.
capitals_reverse = capitals[::-2]
print(capitals_reverse)

#Tuple stats: Given numbers = (10, 20, 80, 40, 50, 60), write a function that returns a dict with length, min, max, sum, and a sorted_list (sorted ascending as a list).
numbers = (10, 20, 80, 40, 50, 60)
num = {}
num["length"] = len(numbers)
num["min"] = min(numbers)
num["max"] = max(numbers)
num["sum"] = sum(numbers)
num["sorted_list"] = sorted(numbers)
print(num)

#Occurrences & indices: For tup1 = ('mango','orange','watermelon','apple','mango'), write code that returns the count of 'mango' and a list of all indices where 'mango' appears.

fruits = ('mango','orange','watermelon','apple','mango')
print(f"count : {fruits.count('mango')}")
occurence = [idx for idx, fruit in enumerate(fruits) if fruit == "mango"]
print(occurence)

#Packing / Unpacking: Given vehicles = 'car','bus','auto','train', unpack so you get first_vehicle, middle_vehicles (as a list), and last_vehicle.

vehicles = 'car','bus','auto','train'
first_vehicle, *middle_vehicles, last_vehicle = vehicles
print(first_vehicle)
print(middle_vehicles)
print(last_vehicle)

#Nested tuples flattening: Given a nested tuple like (captls, tup, tup1) (use examples from tuples.py), write a function that flattens it into a single list of items and iterates to print each item on its own line.

nested_tuple=(capitals,fruits,vehicles)
def flattend_list(nested):
    flattened_list = [item for tup in nested for item in tup]
    for item in flattened_list:
        print(item)

flattend_list(nested_tuple)