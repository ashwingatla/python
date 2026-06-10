# Conditional Statements (If, Ifelse, Else)
print("*****************************If Statements*************************************")
## If Statement
age = 18
if age >= 18:
    print("You can drive a car")
## *********************************************************************************
print("******************************Else Statements**********************************")
## else
## The else statement executes a block of code if the condition in the if statement is False.

age = 17
if age >= 18:
    print("You can drive a car")
else:
    print("You cannot drive the car")
## ***************************************************************************************
print("*******************************Elif Statements**************************************")
## elif
## The elif statement allows you to check multiple conditions. It stands for "else if"

age = 12
if age < 13:
    print("You are a child")
elif 13 <= age <=19:
    print("You are a teen")
else:
    print("You are an adult")
## ***************************************************************************************
print("*************************Nested Conditional Statements******************************")
## Nested Condiitonal Statements

# You can place one or more if, elif, or else statements inside another if, elif, or else statement
#  to create nested conditional statements.

## number even ,odd,negative

#num = int(input("Enter a number : "))
num = 1
if num >=0:
    print("Its a positive number")
    if num % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
else:
    print("Its negative number")

## **************************************************************************************
## Practical Example - 1
print("*****************************Practice-1-LeapYear************************************")
## Determine if a year is a leap year using nested condition statement
#year = int(input("Enter a year : "))
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its is a leap year")
        else:
            print("Its not a leap year")
    print("Its is a leap year")
else:
    print("Its not a leap year")

## ***********************************************************************************
## Practical Example - 2
print("*****************************Practice-2-Calculator***********************************")
## Simple Calculator program
# Take user input
#varA = int(input("Enter number A : "))
#varB = int(input("Enter number B : "))
varA = 10
varB = 8
print("Performing simple arithematic operations")
#operation = input("Enter Operation required (+,-,*,/) : ")
operation = '-'
if operation == '+':
    print ("Addition", varA + varB)
elif operation == '-':
    print("Substraction",varA - varB)
elif operation == '*':
    print("Multiplication",varA * varB)
elif operation == '/':
    if varB !=0:
        print("Division",varA / varB)
    else:
        print("zero division error")
else:
    print("Invalid Operation")

## ***********************************************************************************
## Practical Example - 3
# ### Determine the ticket price based on age and whether the person is a student.
# Ticket pricing based on age and student status
print("*****************************Practice-3-Ticket Pricing***********************************")

#age= int(input("Enter your age : "))
#is_student= input("Are you a student(Yes/No) : ").lower()
age = 10
is_student = 'yes'
if age <= 5:
    print("Entry fee of $5")
elif age <= 12:
    print("Entry fee of $10")
elif age <= 17:
    if is_student == 'yes':
        print("Entry fee of $12")
    else:
        print("Entry fee of $15")
elif age <= 65:
    if is_student == 'yes':
        print("Entry fee of $18")
    else:
        print("Entry fee of $25")
else:
    print("Entry fee of $20")

## ***********************************************************************************
## Practical Example - 4
#Complex Example: Employee Bonus Calculation
#Calculate an employee's bonus based on their performance rating and years of service.
print("*****************************Practice-4-Employee Bonus***********************************")

#performance_rating = int(input("Enter the rating(1-5) : "))
#service_years = int(input("Enter the years of service : "))
performance_rating = 4
service_years = 10
if performance_rating >= 4:
    if service_years >= 10:
        bonus = 20
    elif service_years >= 5:
        bonus = 15
    else:
        bonus = 10
elif performance_rating >= 3:
    if service_years >= 10:
        bonus = 15
    elif service_years >= 5:
        bonus = 10
    else:
        bonus = 5
elif performance_rating >= 2:
    if service_years >= 10:
        bonus = 10
    elif service_years >= 5:
        bonus = 5
    else:
        bonus = 3
else:
    print("Please quit your job")
    bonus = 0
## Bonus Calculation
#salary = int(input("Enter your salary : "))
salary = 500000
bonus_cal = (salary * bonus)//100
print("You have received %s thousand" % bonus_cal)

## ***********************************************************************************
## Practical Example - 5
#Complex Example : User Login System
#A simple user login system that checks the username and password.

print("*****************************Practice-5-User Login System***********************************")
username = input("Enter your username: ")
password = input("Enter your password : ")
if username == 'admin123' and password == 'password123':
    print("Login successful")
else:
    print("Login Unsuccessful")