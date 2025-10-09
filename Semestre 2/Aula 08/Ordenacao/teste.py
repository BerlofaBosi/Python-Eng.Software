l = [12, 68, 95, 41, 25, 71]

last = l[0]

if l[1] > l[0]:
    last = l[0]
    l[0] = l[1]
    l[1] = last

for i in range(len(l)):
    if l[i] > last:
        temp = last

print(l)

