from datetime import date

estado = str(input('Insira a abreviação do seu estado: ')).upper()
anoAcesso = int(input('Quado foi o ultimo ano em que voce acessou o app? '))

ativo = date.today().year -  anoAcesso <= 1
inativo = date.today().year -  anoAcesso > 1
estadoValido = estado == 'SP' or 'MG'

print(f'Estado SP ou MG? {estadoValido}')
print(f'É ativo? {ativo}')

print('É o nosso público alvo? ', inativo and estadoValido)
