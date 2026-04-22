def password(pwd):
    if len(pwd) < 8:
        return False
    if not any(char.isdigit() for char in pwd):
        return False

print(password('abcdsdfdfd'))