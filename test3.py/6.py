#Assume the list given is ['eat', 'ate', 'done', 'tea', 'soup', 'node'] then it should return [['eat','ate','tea], ['done','node'], ['soup']]
l = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
m = {}
for string in l:
    sorted_string = str(sorted(string))
    if sorted_string  in m:
        m[sorted_string].append(string)
    else:
        m[sorted_string] = [string]
print(list(m.values()))            
