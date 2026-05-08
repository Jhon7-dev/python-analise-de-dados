bicycles = ['trek','caloi','cannondale','redline','specialized']
print(bicycles)

# acessando qualuqer elemento pelo índice
print(bicycles[0].title())
#  acessando o último ou penúltimo elemento pode usar o -1 ou -2
print(bicycles[-1].title())
# usadno valores individuais de uma lista 
message = 'minha primeira bicicleta foi uma da  '  + bicycles[1].title() + ' .'
print(message)

# alterando elementos de uma lista
motos = ['honda', 'suzuki','yamaha','harley davison']
# como eu posso alterar o primeiro elemento de uma lista ?
motos[0] = 'ducati'
print(motos)
# o índice 0 passa a ser ducati

#  concatenando os elementos no final de uma lista
motos.append('royal enfield')
print(motos)

#  o método APPEND() facilita crriar listas dinamicamente. Por exemplo podemos começar com uma lista fazia
volvo = []
volvo.append('xc 40')
volvo.append('xc 60')
volvo.append('xc 90')
print(volvo)

#  para deixar que seus usuários tenham o controle, comece com uma lista vazia que armazenará valores dos usuários.
#  em seguida concatene cada novo valor 

#  inserindo elementos em uma lista
#  pode adicionar um novo elemnto em qualquer posição de sua lista usando o método INSERT(). Fça isso especificando o índice do novo elemento e o valor do novo item

audi = ['q3','q5','q7']
audi.insert(0,'a3')
print(audi)
# ['a3', 'q3', 'q5', 'q7']
#  o elemento é inserido na lista e abre um espaço na posição 0 e armazena o valor 'a3' nesse local.

# REMOVENDO elementos de uma lista

# se a posição do item que você quer remover de uma lista for conhecida, a instrução  DEL poderá ser usada.

audi = ['q3','q5','q7']
print(audi)
del audi [2]
print (audi)
#  o cód usa o del para remover o terceiro  item 'q7', da lista de carros

#  REMOVENDO um item com o método POP()
# remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção.
#  o termo pop deriva de pensar em uma lista como se fosse uma PILHA de itens e remover um item (pop) do topo da pilha.
#  topo da pilha é o final da lista

bmw = ['320i','x1','x2','x3']
print(bmw)
popped_bmw = bmw.pop()
print(bmw)
print(popped_bmw)

#  a variável 'popped_bmw' armazena o valor que foi removido

#  posso usar o método POP() para remover um item de qualquer posição em uma lista se incluir o índice que você deseja remover entre os parênteses

bmw = ['320i','x1','x2','x3']
primeira_bmw = bmw.pop(1)
print("O primeiro modelo de BMW que eu tive foi uma " + primeira_bmw)

#  removendo um item de acordo com o valor => remove()
#  as vezes você só saberá a posição do valor que quer remover de uma lista
# se conhecer apenas o valor do item que deseja remover, o metodo remove() poderá ser usado 

#  quero remover '320i' da lista
bmw = ['320i','x1','x2','x3']
bmw.remove('320i')
print(bmw)

#  também podemos usar o método remove() para trabalhar com um valor que está sendo removido de uma lista. Vamos remover o valor 'x3' e exibir um motivop para removê-lo da lista

bmw = ['320i','x1','x2','x3']
print(bmw)
too_expensive = 'x3'
bmw.remove(too_expensive)
print(bmw)
print("\n A " + too_expensive.title() + " é muito caro para mim." )

#  valor x3 foi removida da lista, mas continua armazenado na variavel too_expensive, permitindo exibir uma frase pelo qual foi removido 'x3'.