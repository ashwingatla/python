# '''
# ## Create empty Dictionary
# name = {}
# print(f"{name} empty dictionary")

# ## Create a Dictionary
name = {"kid":1,"adult":"Ash"}
# print(name)

# ## Accessing an element in a Dictionary
# print(name['kid'])

# ## Accessing an element in a Dictionary with get function
#print(name.get('kid'))

# ## Accessing an element in a Dictionary with get function with no key and diplaying a default value
#print(name.get('kid',0))

# ## Adding an element to a Dictionary
name['kidage']=20
name['address']='hyderabad'
#print(name)

# ## Remove an element to a Dictionary
#del name['kid']
#print(name)

# ## Update an element to a Dictionary
name['kid']="Hari"
#print(name)

# ## Dictionary Methods
# keys = name.keys()  ## fetch all the keys
# print(keys)

# values = name.values()  ## Fetch all the values
# print(values)

#items = name.items() ## Create a List of key-value pairs in the form of tuples
#print(items)

# ## Shallow Copy -- All to duplicate a dictionary and make changes to duplicated dictionary without effecting the original dictionary

# name_copy = name.copy()
# name_copy['kid'] = 'Adi'
# print(name_copy)
# print(name)

# ## Iterating over the dictionary
# for key in name.keys():  ## iterating over keys
#     print(key)

# for val in name.values(): ## Iterating over values
#     print(val)

# for key,val in name.items():  ## iterate over the dictionary items
#     print(key,val)

## Nested Dictionaries
# student_list = {"student1" : {"name":"adi","age":9,"grade":"class3"},
#                 "student2" : {"name":"ash","age":10,"grade":"class4"},
#                 "student3" : {"name":"ash","age":11,"grade":"class5"}}
# print(student_list["student1"])
# print(student_list["student2"])
# print(student_list["student3"])

# ## Iterating over nested dictionaries
# print("Iterating over nested dictionaries")
# for student,info in student_list.items():
#     print(student,info)
#     for information,val in info.items():
#         print(information,val)

# ## Dictionary comprehension
# squares = {i:i**2 for i in range(1,6)}
# print(squares)

# ## Conditional Dictionary comprehension
# even_number = {i : i **2 for i in range(1,10) if i % 2==0}
# print(even_number)
# '''
# ## Use a dictionary to count the frequency in list
# numbers=[1,2,2,3,3,3,4,4,4,4]
# frequency={}
# for i in numbers:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)

## merge 2 dictionaries into one
# dict1 = {"a":1,"b":2}
# dict2 = {"c":3,"d":4}
# merged = {**dict1,**dict2}
# # for i,j in dict1.items():
# #     merged[i]=j
# # for k,l in dict2.items():
# #     merged[k]=l
# print(merged)