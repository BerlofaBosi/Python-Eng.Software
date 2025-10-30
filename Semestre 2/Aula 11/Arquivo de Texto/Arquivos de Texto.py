# Abrindo um arquivo de texto -> variavel = open("arquivo.txt", "modo")

arq = open('aula.txt', 'r')
b = arq.read(3)
print(b)

c = arq.read(4)
print(c)

# Pra resetar o indicador, ou fecha o arquivo e abre de novo ou usa o metodo seek
arq.seek(0,0)

d = arq.read()
print(d)


arq.close()
