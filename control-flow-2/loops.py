# Loops
# Introduction to Loops

# for Loop

# Iterating over a range
# Iterating over a string
# while Loop

# Loop Control Statements

# break
# continue
# pass
# Nested Loops

### *********************************************************************
## for loop
print("**************************for loop****************************************")

for i in range(5):
    print(i)

### *********************************************************************
## while loop
## The while loop continues to execute as long as the condition is True.
print("**************************while loop****************************************")
i = 0
while i < 5:
    print(i)
    i += 1

### *********************************************************************
## Loop Control Statements
## break
## The break statement exits the loop permaturely

## break statement
print("**************************break loop****************************************")
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break

### *********************************************************************
## Loop Control Statements
## continue
## The continue statement skips the current iteration

## continue statement
print("**************************continue loop****************************************")
for i in range(5):
    if i == 2:
        continue
    print(i)
### *********************************************************************
## Nested Loop Control Statements

## Nested loop statement
print("**************************nested loop****************************************")
for i in range(1,5):
    print("Table : ",i)
    for j in range(1,11):
        print("%d * %s =" % (i,j),i*j)

## Examples- Calculate the sum of first N natural numbers using a while and for loop
print("******************Calculate the sum of first N natural numbers using a while************************")
n = 10
total = 0
j = 1
while j < n:
    total = total + j
    j += 1
print(total)

print("******************Calculate the sum of first N natural numbers using a for loop************************")
n = 10
total = 0
for i in range(1,n):
    total += i
print(total)

## Example- Prime numbers between 1 and 100
print("**************Prime Numbers***********")
for i in range(1,20):
    if i > 1:
        for num in range(2,i):
            if i % num == 0:
                break
        else:
            print(i)