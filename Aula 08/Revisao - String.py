txt = input('Digite uma palavra bonita: ')

txt = 'hoje-tem-aula-de-python'

print(f'O primeiro caractere é {txt[0]}')
print(f'O último caractere é {txt[-1]}')
print(f'O tamanho da string é {len(txt)}')
print(f'Outra forma de escrever o ultimo caractere {txt[len(txt)-1]}')
print(f'Uma forma de pegar fatias da string é: {txt[2:4]}')
print(f'Uma forma de pegar fatias da string é: {txt[2:]}')
print(f'Uma forma de pegar fatias da string é: {txt[:4]}')
print(f'Uma forma de pegar fatias da string é: {txt[::2]}')
print(f'Uma forma de pegar fatias da string é: {txt[1::2]}')

txt1 = 'hj-e-uad-yhn'
txt2 = 'oetmal-epto'

i = 0
texto = ''

while i < len(txt1):
    #print(txt1[i], end='')
    texto += txt1[i]
    if i < len(txt2):
        #print(txt2[i], end='')
        texto += txt2[i]
    i += 1

print(texto)
