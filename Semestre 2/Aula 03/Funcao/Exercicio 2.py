carrinho = []

def adicionarProduto(produto):
    carrinho.append(produto)

def removerProduto(produto):
    for i in range(len(carrinho)):
        if carrinho[i] == produto:
            carrinho.pop(i)
            return
    #carrinho.remove(produto)
    print('Produto não Encontrado')

def verCarrinho():
    global carrinho
    print('Seu carrinho: ', carrinho)


adicionarProduto('MacBook Air M1')
adicionarProduto('Monitor Portatil')
adicionarProduto('Adaptador USB C - HDMI')
verCarrinho()
removerProduto('Adaptador USB C - HDMI')
verCarrinho()
