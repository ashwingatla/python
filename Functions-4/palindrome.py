## Check if the string is a palindrome
string='noon'

def palindrome(stri):
    return stri == stri[::-1]
print(palindrome(string))