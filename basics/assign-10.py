'''
### Problem 1.10 ⭐⭐⭐ (Medium)
Create a program that calculates the simple interest.
- Principal: 1000
- Rate: 5% per annum
- Time: 2 years

**Formula:** SI = (P × R × T) / 100

Print the result with proper formatting.
'''
principal = 1000
rate = 5
time = 2
simple_interest = (principal * rate * time)/100
print(f"Simple interest for principal:{principal} with rate:{rate}% in the time period: {time} years is {simple_interest}")