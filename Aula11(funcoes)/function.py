
def cadastrar_produto():
     produto = input('digite o nome do produto que deseja cadastrar: ')
     produto = produto.casefold()
     print('produto {} cadastrado com sucesso'.format(produto))
     return produto