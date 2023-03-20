l = [2, 3, 4, 2, 7, 3, 4, 8, 9, 1, 2, 3]
m = []
for i in l:
    if i not in m:
        m.append(i)
m.sort()
print(m)