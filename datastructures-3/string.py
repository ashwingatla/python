## String Operations

name = "python"
#print(len(name))

## Index based operations

#print(name[0])
#print(name[-1])

## Slicing operations

#print(name[0:2])
#print(name[::-1])

##  String concatenation

# learner = "Ashwin"
# print(name + " " + learner)

## String Multiplication
#print(name * 3)

## Check character or word exists (True/False)
#print("i" in msg)

## String with forloop
# for i in msg:
#     print(i)

### String methods
msg = "i like gen ai Development"

# upper() : convert all characters to upper case
#print(msg.upper())
# lower() : convert all characters to lower case
#print(msg.lower())
# title() : First character of every word converts into upper case
#print(msg.title())
# capitalize() : converts first letter of string into uppercase.
#print(msg.capitalize())
# strip() : removes spaces from beginning and ending of string.
#print(msg.strip())
# lsstrip() : lstrip() removes spaces from left side.
#print(msg.lstrip())
# rsstrip() : rstrip() removes spaces from right side.
#print(msg.rstrip())
# replace() : Replace old value with new value and creates new string
#print(msg.replace('like','love'))
# split() : splits string into list of elements
#print(msg.split())
# join() : joins list values into string (we can give delim)
courses = ["Python", "Java", "DevOps"]
#print('#'.join(courses))
# find() : returns index position of given value.
#print(msg.find('like'))
# count() : returns how many times value is repeated
#print(msg.count('like'))
# startsWith() : checks whether string starts with given value.
#print(msg.startswith('I'))
# endsWith() : checks whether string ends with given value.
#print(msg.endswith('Development'))
# isdigit() : checks whether all characters are digits.
#print(msg.isdigit())
# isalpha() : checks whether all characters are alphabets.
#print(msg.isalpha())
# isalnum() : checks whether all characters are alphabets or numbers.
#print(msg.isalnum())
# format() : Construct a string with dynamic values
