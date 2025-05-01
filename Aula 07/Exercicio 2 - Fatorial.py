fat = user = int(input('Insira um número: '))
cont = fat - 1

while cont > 0:
    fat *= cont
    cont -= 1

print(f'O fatorial de {user} é {fat}.')
