# 3. Write a function to find the sum of the cube of elements in a list.
# The list is received as an argument to the function and it should return 
# the sum.

def elements(*nums):
    sum = 0
    for i in nums:
        sum+=i**3
    return sum
print(elements(2,3,4,5))
