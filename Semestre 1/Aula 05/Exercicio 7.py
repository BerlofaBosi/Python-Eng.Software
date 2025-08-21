# https://www.campuscode.com.br/conteudos/o-calculo-do-digito-verificador-do-cpf-e-do-cnpj
# cpf teste: 145.382.206-20

cpf = input('Qual é o seu cpf (somente números): ')
intCpf = []

for c in range(0, 11):
    intCpf.append(int(cpf[c]))

# Verificador 1 ==================================
i = 10
soma = 0
for c in range(0, 9):
    soma += intCpf[c] * i
    i -= 1

verificador1 = 11 - (soma % 11)

if verificador1 >= 10:
    verificador1 = 0

# Verificador 2 ==================================
i = 11
soma = 0
for c in range(0, 10):
    soma += intCpf[c] * i
    i -= 1

verificador2 = 11 - (soma % 11)

if verificador2 >= 10:
    verificador2 = 0

# Validação CPF ==================================
if (intCpf[9] == verificador1) and (intCpf[10] == verificador2):
    print('O cpf inserido é um cpf válido.')
else:
    print('O cpf inserido é inválido.')
