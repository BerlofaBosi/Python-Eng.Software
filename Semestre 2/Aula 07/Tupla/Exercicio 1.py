# Crie uma maneira para adicionar elementos em uma tupla

adicionaTupla = lambda tupla, elemento: tupla + tuple([elemento])


a = ()
print(a)
print(adicionaTupla(a, 'Davi'))
