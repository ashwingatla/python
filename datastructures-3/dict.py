# Create a dictionary
student = {
    "name": "Ravi",
    "age": 25,
    "course": "Python",
    "marks": 85
}

# print(student['name']) ## Returns the key-value
# print(student.get('name')) ## Returns the value, if it doesnt exit it returns none
# print(student.get('name1','ash')) ## If no key exists, return default value

# ## Add Element to a dictionary
# student['grade'] = 'A'
# print(student)

# # Dictionary Operations
# print(student.keys())
# print(student.values())
# print(student.items())

# ## Modifying multiple values at once or add a new dictionary to existing

# student.update({"name" : "Ashok", "marks" : 70})
# print(student)

# ## Pop function removes and return the value
# value = student.pop("grade")
# print(student)
# print(value)

# ## Popitem function remove and return the key value
# key,value = student.popitem()
# print(key,value)

## Clear the dictionary
#print(student.clear())

## Delete the dictionary
#del(student)

# Working with Nested Dictionary
students= {
    "student1" : {
    "name": "Ramesh",
    "age": 27,
    "course": "Java",
    "marks": 60
    },
    "student2" : {
    "name": "santosh",
    "age": 23,
    "course": "genai",
    "marks": 90
    }}

# ## Fetch the nested dictionary from students
# print(students["student1"])

# ## Fetch the key "name" from student1 in Students
# print(students['student1']['name'])

# ## Fetch the key "name" from student1 in Students using get function
# print(students['student1'].get('name'))

# ## Looping through a dictionary
# for key1,val1 in student.items():
#     print(key1,val1)

## Looping through a nested dictionary
for key1 in students:
    print(key1)
    for key2 in students[key1]:
        print(students[key1][key2])