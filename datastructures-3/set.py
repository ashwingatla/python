courses = {"Python", "JAVA", "Python", "DEVOPS"}

## How Set eliminates the duplicates, This is done but storing in the hash value of the element
# print(hash("Python"))
# print(hash("JAVA"))
# print(hash("DEVOPS"))
# print(hash("Python"))

#### Set Operations ####

# add ( ) : It is used Add one element to set
# update ( ) : It is used Add multiple elements to set
# remove ( ) : It is used to remove specified element from set
# discard ( ) : It is used to remove specified element from set
# pop ( ) : It is used to remove random element from set
# clear ( ) : It is used to remove all elements from set
# del : It is used to delete entire set from memory

# add ( ) : It is used Add one element to set
courses.add("GENAI")

# update ( ) : It is used Add multiple elements to set
courses.update({"AWS","GCP"})

# remove ( ) : It is used to remove specified element from set
courses.remove("GCP")

# discard ( ) : It is used to remove specified element from set and ignores if the element is not present in the set
courses.discard("GCP")

# del : It is used to delete entire set from memory
#del courses

## Set Functions
# len()
# min()
# max()
# sorted()

print(len(courses))
print(min(courses))
print(max(courses))
print(sorted(courses))

# Remove Duplicates from list using set() function
skills = ["JAVA", "Python", "DevOps", "JAVA"]
print(set(skills))