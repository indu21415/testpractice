#Write a function named type_check that takes two parameters and it should
#return True if both parameters are of the same data type, and False otherwise.

def func(a,b):
    if type(a)==type(b):
        return True
    else:
        return False
print(func(2,3))
print(func(1,'a'))