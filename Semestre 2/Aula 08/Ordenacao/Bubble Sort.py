lista = [12, 68, 95, 41, 25, 71]
print(lista)

def bubbleSort(list):
    for iter in range(len(list)-1, 0, -1):
        print(f'Iteração {iter}')
        for j in range(iter):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        print(list)

bubbleSort(lista)
