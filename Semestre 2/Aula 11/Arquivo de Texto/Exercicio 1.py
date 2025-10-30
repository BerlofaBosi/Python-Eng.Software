arquivo = open('aula.txt', 'r')

char = arquivo.read(1)

while char != '':
    print(char)
    char = arquivo.read(1)


