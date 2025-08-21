def depositar(valor):
    global saldo
    saldo += valor
    movimentos.append(f'+{valor}')

def sacar(valor):
    global saldo
    saldo -= valor
    movimentos.append(f'-{valor}')

def extrato():
    global saldo
    print('---' * 10)
    print(f'O seu saldo é de R${saldo}\n')
    print(f'Houveram os seguintes movimentos na sua conta: {movimentos}')
    for i in movimentos:
        print(i)
    print('---' * 10)

saldo = 0
movimentos = []

depositar(100)
sacar(10)
extrato()
