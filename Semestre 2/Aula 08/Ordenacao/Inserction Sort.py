l = [58, 18, 5, 4, 6]
print(l)
for j in range(1, len(l)):
    aux = l[j]
    while j > 0 and aux < l[j-1]:
        l[j] = l[j-1]
        j = j-1
    l[j] = aux
    print(l)
