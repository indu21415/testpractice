# Write a function half_and_half that takes in a list and change the list such 
# that the elements of the second half are now in the first half. For example,
# if the list is [10,20,30,40,50,60], then it should return [40,50,60,10,20,30]
#  and if the list is [10,20,30,40,50,60,70], then it should return
#  [50,60,70,40,10,20,30].


def half_and_half(l):
    i = []
    b = l[3:]+l[0:3]
    i.extend(b)
    #l.extend(c)
    return i
print(half_and_half([10,20,30,40,50,60]))
#print(half_and_half([10,20,30,40,50,60,70]))

def half(i):
    a = []
    b = i[4:]+i[3:4]+i[0:3]
    a.extend(b)
    return a
print(half([10,20,30,40,50,60,70]))