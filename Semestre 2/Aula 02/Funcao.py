def texto(y, x):
    l = []
    for i in range(x):
        l.append(float(input(f'Digite o valor da {y}{i+1}: ')))
    return l

def dados(sem):
    notas = []
    notas.extend(texto('CP',3))
    if sem == 1:
        notas.extend(texto('SP', 1))
        notas.append(notas[-1])
    elif sem == 2:
        notas.extend(texto('SP', 2))
    else:
        return -1
    notas.extend(texto('GS',1))
    return notas

def media_cp(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
    return (n1 + n2 + n3 - menor) / 2

def media_sem(mcp, sp1, sp2, gs):
    return mcp*0.2 + (sp1 + sp2)/2*0.2 + gs*0.6

def media_final(msem1, msem2):
    return msem1*0.4 + mseam2*0.6

sem1 = dados(1)
sem2 = dados(2)
mcp1 = media_cp(sem1[0], sem1[1], sem1[2])
mcp2 = media_cp(sem2[0], sem2[1], sem2[2])
ms1 = media_sem(mcp1, sem1[3], sem1[4], sem1[5])
ms2 = media_sem(mcp2, sem2[3], sem2[4], sem2[5])
mdf = media_final(ms1, ms2)

if mdf >= 6.0:
    print(f'O aluno foi aprovado com nota {mdf}')
elif mdf >= 4.0:
    print(f'O aluno foi para exame com nota {mdf}')
else:
    print(f'O aluno foi reprovado com nota {mdf}')
