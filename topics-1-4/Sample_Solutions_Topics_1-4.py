"""
TOPICS 1-4: SAMPLE SOLUTIONS (SELECTED PROBLEMS)
Shows solving approach and best practices for different difficulty levels
"""

import math

print("=" * 80)
print("TOPIC 1: PYTHON BASICS & ENVIRONMENT SETUP - SAMPLE SOLUTIONS")
print("=" * 80)

# ===== PROBLEM 1.1 =====
print("\n📌 Problem 1.1: Print Name, Age, Hobby")
print("-" * 80)

name = "John"
age = 25
hobby = "Reading"

print(name)
print(age)
print(hobby)

print("\n✅ Explanation:")
print("- Create three variables")
print("- Print each on a separate line")
print("- Simple and straightforward!")

# ===== PROBLEM 1.5 =====
print("\n📌 Problem 1.5: Student Information Summary")
print("-" * 80)

student_name = "Alice"
roll_number = 101
grade = "A"
school = "Green Valley High School"

print("=" * 40)
print("STUDENT INFORMATION")
print("=" * 40)
print(f"Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Grade: {grade}")
print(f"School: {school}")
print("=" * 40)

print("\n✅ Explanation:")
print("- Use f-strings for better formatting")
print("- Add visual separators for readability")
print("- Make the output look professional")

# ===== PROBLEM 1.9 =====
print("\n📌 Problem 1.9: Celsius to Fahrenheit Conversion")
print("-" * 80)

celsius = 0
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is {fahrenheit}°F")

print("\n✅ Explanation:")
print("- Apply the formula: F = (C × 9/5) + 32")
print("- Use meaningful variable names")
print("- Format with degree symbols for clarity")

# ===== PROBLEM 1.10 =====
print("\n📌 Problem 1.10: Simple Interest Calculator")
print("-" * 80)

principal = 1000
rate = 5  # per annum
time = 2  # years

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Principal: ${principal}")
print(f"Rate: {rate}% per annum")
print(f"Time: {time} years")
print(f"Simple Interest: ${simple_interest}")
print(f"Total Amount: ${total_amount}")

print("\n✅ Explanation:")
print("- Formula: SI = (P × R × T) / 100")
print("- Calculate both SI and total amount")
print("- Format as currency for clarity")

print("\n" + "=" * 80)
print("TOPIC 2: VARIABLES, DATA TYPES & OPERATORS - SAMPLE SOLUTIONS")
print("=" * 80)

# ===== PROBLEM 2.1 =====
print("\n📌 Problem 2.1: Check Data Types")
print("-" * 80)

values = [42, 3.14, "Hello", True]

for value in values:
    print(f"Value: {value}, Type: {type(value)}")

print("\n✅ Explanation:")
print("- type() function identifies data type")
print("- Loop through list to check multiple values")
print("- Format output for readability")

# ===== PROBLEM 2.4 =====
print("\n📌 Problem 2.4: All Arithmetic Operations")
print("-" * 80)

num1 = 10
num2 = 3

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")  # Floor division
print(f"{num1} % {num2} = {num1 % num2}")    # Modulo
print(f"{num1} ** {num2} = {num1 ** num2}")  # Exponentiation

print("\n✅ Explanation:")
print("- / gives decimal division")
print("- // gives floor division (rounds down)")
print("- % gives remainder (modulo)")
print("- ** means power/exponentiation")

# ===== PROBLEM 2.11 =====
print("\n📌 Problem 2.11: Extract Digits from Number")
print("-" * 80)

num = 1234

thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10

print(f"Number: {num}")
print(f"Thousands: {thousands}")
print(f"Hundreds: {hundreds}")
print(f"Tens: {tens}")
print(f"Ones: {ones}")

print("\n✅ Explanation:")
print("- thousands = 1234 // 1000 = 1")
print("- hundreds = (1234 % 1000) // 100 = 234 // 100 = 2")
print("- tens = (1234 % 100) // 10 = 34 // 10 = 3")
print("- ones = 1234 % 10 = 4")

# ===== PROBLEM 2.13 =====
print("\n📌 Problem 2.13: Distance Between Two Points")
print("-" * 80)

x1, y1 = 0, 0
x2, y2 = 3, 4

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Distance: {distance}")

print("\n✅ Explanation:")
print("- Formula: distance = √[(x2-x1)² + (y2-y1)²]")
print("- (3-0)² + (4-0)² = 9 + 16 = 25")
print("- √25 = 5")

# ===== PROBLEM 2.14 =====
print("\n📌 Problem 2.14: Volume of a Sphere")
print("-" * 80)

radius = 5
volume = (4/3) * math.pi * radius**3

print(f"Radius: {radius}")
print(f"Volume: {volume:.2f} cubic units")

print("\n✅ Explanation:")
print("- Formula: V = (4/3) × π × r³")
print(f"- V = (4/3) × π × 5³")
print(f"- V = (4/3) × π × 125")
print(f"- V ≈ {volume:.2f}")

# ===== PROBLEM 2.15 =====
print("\n📌 Problem 2.15: Decimal to Binary and Hexadecimal")
print("-" * 80)

num = 255

binary = bin(num)[2:]      # bin() gives '0b...' so we slice from [2:]
hexadecimal = hex(num)[2:] # hex() gives '0x...' so we slice from [2:]

print(f"{num} in binary: {binary}")
print(f"{num} in hexadecimal: {hexadecimal}")

print("\n✅ Explanation:")
print("- bin(255) returns '0b11111111'")
print("- hex(255) returns '0xff'")
print("- We slice [2:] to remove '0b' or '0x' prefix")

print("\n" + "=" * 80)
print("TOPIC 3: CONTROL FLOW - SAMPLE SOLUTIONS")
print("=" * 80)

# ===== PROBLEM 3.2 =====
print("\n📌 Problem 3.2: Grade Assignment Based on Marks")
print("-" * 80)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

print("\n✅ Explanation:")
print("- Use if-elif-else for multiple conditions")
print("- Conditions are checked in order")
print("- First matching condition determines the grade")

# ===== PROBLEM 3.6 =====
print("\n📌 Problem 3.6: Sum of Numbers from 1 to 10")
print("-" * 80)

total = 0
for i in range(1, 11):
    total += i

print(f"The sum is {total}")

print("\n✅ Explanation:")
print("- Start with total = 0")
print("- Add each number from 1 to 10")
print("- Final sum: 1+2+3+...+10 = 55")

# ===== PROBLEM 3.8 =====
print("\n📌 Problem 3.8: Factorial of a Number")
print("-" * 80)

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")

print("\n✅ Explanation:")
print("- Factorial: 5! = 5 × 4 × 3 × 2 × 1 = 120")
print("- Start with factorial = 1")
print("- Multiply by each number from 1 to n")

# ===== PROBLEM 3.9 =====
print("\n📌 Problem 3.9: Check if Number is Prime")
print("-" * 80)

def check_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

# Test
test_numbers = [17, 4, 2, 15]
for num in test_numbers:
    result = check_prime(num)
    print(f"{num} is {'prime' if result else 'not prime'}")

print("\n✅ Explanation:")
print("- Prime numbers: only divisible by 1 and themselves")
print("- Check divisibility from 2 to √n")
print("- If any divisor found, not prime")

# ===== PROBLEM 3.10 =====
print("\n📌 Problem 3.10: Fibonacci Series (10 terms)")
print("-" * 80)

a, b = 0, 1
fibonacci_series = []

for i in range(10):
    fibonacci_series.append(a)
    a, b = b, a + b

print("Fibonacci series:", " ".join(map(str, fibonacci_series)))

print("\n✅ Explanation:")
print("- Start: a=0, b=1")
print("- Each term = sum of previous two")
print("- Series: 0 1 1 2 3 5 8 13 21 34")

# ===== PROBLEM 3.14 =====
print("\n📌 Problem 3.14: Check if Number is Palindrome")
print("-" * 80)

def is_palindrome(num):
    """Check if a number is palindrome"""
    str_num = str(num)
    return str_num == str_num[::-1]

test_nums = [121, 123, 1331]
for num in test_nums:
    result = is_palindrome(num)
    print(f"{num} is {'palindrome' if result else 'not palindrome'}")

print("\n✅ Explanation:")
print("- Convert number to string")
print("- Compare with reversed string [::-1]")
print("- '121' == '121' → palindrome")

print("\n" + "=" * 80)
print("TOPIC 4: FUNCTIONS & SCOPE - SAMPLE SOLUTIONS")
print("=" * 80)

# ===== PROBLEM 4.1 =====
print("\n📌 Problem 4.1: Add Two Numbers")
print("-" * 80)

def add(a, b):
    """Add two numbers and return the sum"""
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")

print("\n✅ Explanation:")
print("- def keyword defines function")
print("- a, b are parameters (inputs)")
print("- return sends result back")

# ===== PROBLEM 4.3 =====
print("\n📌 Problem 4.3: Check if Even or Odd")
print("-" * 80)

def is_even(num):
    """Check if number is even"""
    return num % 2 == 0

print(f"is_even(4) = {is_even(4)}")   # True
print(f"is_even(7) = {is_even(7)}")   # False

print("\n✅ Explanation:")
print("- num % 2 gives remainder")
print("- If remainder is 0, it's even")
print("- Return True/False directly")

# ===== PROBLEM 4.8 =====
print("\n📌 Problem 4.8: Calculate Factorial")
print("-" * 80)

def factorial(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(0) = {factorial(0)}")

print("\n✅ Explanation:")
print("- Base case: 0! = 1, 1! = 1")
print("- For n > 1: multiply 2 to n")
print("- 5! = 2 × 3 × 4 × 5 = 120")

# ===== PROBLEM 4.9 =====
print("\n📌 Problem 4.9: Return Multiple Values")
print("-" * 80)

def calculate(a, b):
    """Calculate sum, product, and difference"""
    sum_val = a + b
    product_val = a * b
    difference_val = a - b
    
    return sum_val, product_val, difference_val

sum_result, prod_result, diff_result = calculate(10, 3)
print(f"Sum: {sum_result}, Product: {prod_result}, Difference: {diff_result}")

print("\n✅ Explanation:")
print("- Return multiple values as tuple")
print("- Unpack them when calling: sum, prod, diff = calculate(10, 3)")

# ===== PROBLEM 4.10 =====
print("\n📌 Problem 4.10: Check if Prime")
print("-" * 80)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

print(f"is_prime(17) = {is_prime(17)}")   # True
print(f"is_prime(4) = {is_prime(4)}")     # False
print(f"is_prime(2) = {is_prime(2)}")     # True

print("\n✅ Explanation:")
print("- Check if divisible by any number from 2 to √n")
print("- If divisible, return False")
print("- If no divisors found, return True")

# ===== PROBLEM 4.13 =====
print("\n📌 Problem 4.13: Generate Fibonacci Sequence")
print("-" * 80)

def fibonacci(n):
    """Generate first n terms of Fibonacci sequence"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence

result = fibonacci(5)
print(f"fibonacci(5) = {result}")

print("\n✅ Explanation:")
print("- Handle edge cases (n <= 0)")
print("- Start with [0, 1]")
print("- Each term = sum of previous two")

# ===== PROBLEM 4.15 =====
print("\n📌 Problem 4.15: Compound Interest with Defaults")
print("-" * 80)

def compound_interest(principal, rate=5, time=2):
    """Calculate compound interest with default parameters"""
    amount = principal * (1 + rate/100) ** time
    interest = amount - principal
    
    return interest

# Using all defaults
interest1 = compound_interest(1000)
print(f"compound_interest(1000) = ${interest1:.2f}")

# Custom values
interest2 = compound_interest(1000, 7, 3)
print(f"compound_interest(1000, 7, 3) = ${interest2:.2f}")

print("\n✅ Explanation:")
print("- Default parameters: rate=5, time=2")
print("- Formula: A = P(1 + r/100)^t")
print("- Can override defaults when calling")

print("\n" + "=" * 80)
print("🎉 SAMPLE SOLUTIONS COMPLETE!")
print("=" * 80)
print("\n📌 TIPS FOR SOLVING PROBLEMS:")
print("1. Understand the problem completely")
print("2. Break it into smaller steps")
print("3. Write pseudocode first")
print("4. Implement and test")
print("5. Optimize if needed")
print("6. Add comments for clarity")
