# 5. Write a function ‘round_to_two_places’ which takes one argument ‘num’ 
# and returns the given number rounded to two decimal places. For Example,
# round_to_two_places(3.14159) should return 3.14.

def round_to_two_places(n):
    return (round(n,2))
result = round_to_two_places(3.14159)
print(result)