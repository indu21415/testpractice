# Write a program "num_identifier.py" that will print whether the number is a single digit number or double digit number or big number.
# If given number is one digit number, print "Single digit number"
# If given number is two digit number, print "Double digit number"
# If number is three digit number or bigger, print "Big number"

n = int(input("enter n:"))
if n<10:
    print("Single digit number",n)
elif n<100 and n>=10:
    print("Double digit number",n)
else:
    print("Big number",n)

