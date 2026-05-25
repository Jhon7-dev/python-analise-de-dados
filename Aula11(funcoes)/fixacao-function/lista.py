lista_compras = []

while True:
     print('----- Lista De Compras -----')
     print('1 - Adicionar Item')
     print('2 - Remover Item')
     print('3 - Ver Lista')
     print('4 - Sair')
     opcao = input('Digite um Opção : ')
     
     if opcao == '1':
          def cadastrar_produto():
               lista = input(' digite o que você deseja adicionar ao carrinho')
               lista.append(lista_compras.str())
               print('Produto {} cadastrado com sucesso! '.format(lista))
               return lista
     cadastrar_produto()