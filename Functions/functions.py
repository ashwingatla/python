## Defining a function

# def func_name(parameters):
#     <function body>
#     return value

#Sample function
# def even_odd_number(num):
#     if num % 2 == 0:
#         print("This is an even number")
#     else:
#         print("This is an odd number")

# even_odd_number(3)

## Multiple parameters
def add_sub(a,b):
    add = a + b
    sub = a - b
    return add, sub
add_num,sub_num = add_sub(1,2)
print(add_num,sub_num)

#### Default parameters
def add_sub(a=1,b=3):
    add = a + b
    sub = a - b
    return add, sub
add_num,sub_num = add_sub()
print(add_num,sub_num)

### Positional Arguments
def postional_arg(*args):
    for i in args:
        print(i)

postional_arg(1,23,4,5,3,"ash")

### Keyword Arguments
def keyword_arg(**kwargs):
    for i_key,j_val in kwargs.items():
        print(f"key:{i_key},value:{j_val}")

keyword_arg(name="ash",age=20)