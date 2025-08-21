def contVogais(frase):
    """Conta as vogais do input e retorna o total."""
    vogais = 0
    for i in range(len(frase)):
        if frase[i].lower() in 'aeiou':
            vogais += 1

    return vogais

def invertStr(frase):
    """Inverte a string inputada."""
    return frase[::-1]

def contPlvrs(frase):
    """Retorna quantas palavras tem na string inputada."""
    return len(frase.split())
