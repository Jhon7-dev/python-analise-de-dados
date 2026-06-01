# def make_pizza(*toppings):# o asterisco no parâmetro diz para criar uma tupla vazia chamada toppings e reunir valores recebidos nessa tupla
#      print("\n fazendo uma pizza com os seguintes ingredientes")
#      for topping in toppings:
#           print(toppings)
#           print("- " + topping)
# # make_pizza('pepperoni','')
# # make_pizza('cebola')
# make_pizza('cebola','azeitona','queijo','alho')


# Uma função que aceite vários parâmetros como argumentos, o parâmetro que aceita um número ARBITRÁRIO de argumentos deve ser colocado por último na definição da função.

def make_pizza(size,*toppings):
     print('\n fazendo a pizza ' + str(size) + ' pizza com os seguintes ingredientes')
     for topping in toppings:
          print('- ' + topping)
     print('pizza feita com total de ', len(toppings), 'de ingredientes')
make_pizza(16,'pepperoni')
make_pizza(11,'pepperoni','queijo','manjericão','tomate')