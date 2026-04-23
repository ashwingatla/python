def password(pwd):
    if len(pwd) < 8:
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    if not any(char.islower() for char in pwd):
        return False
    if not any(char.isupper() for char in pwd):
        return False
    if not any(char in '$#!_@%' for char in pwd):
        return False
    else:
        return True

print(password('Abcd@df1fd'))