lista = [12, 68, 95, 41, 25, 71]
print(lista)
print('-=-'*10)

def selectionSort(list):
    for i in range(len(list) -1):
        lower = i
        print(f'Execucao {i}')
        for j in range(i + 1, len(list)):
            if list[j] < list[lower]:
                lower = j
        list[i], list[lower] = list[lower], list[i]
        print(list)


    return list

print(selectionSort(lista))
