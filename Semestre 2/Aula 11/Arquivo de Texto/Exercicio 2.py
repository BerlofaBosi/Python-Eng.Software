arquivo = open('aula.txt', 'r+')

txt = ''

while True:
    char = arquivo.read(1)

    if char == '':
        break

    elif char == 'a':
        print('A')
        txt += 'A'
    else:
        print(char)
        txt += char

arquivo.seek(0,0)
arquivo.write(txt)
arquivo.close()
