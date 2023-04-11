#7. Define a function “sign” which takes a numerical argument and 
#returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

def sign(num):
    if num<0:
       return (-1)
    elif num>0:
        return 1
    else:
        return 0 
# res = sign(4)
# print(res)
print(sign(3))
print(sign(0))
print(sign(-8))    