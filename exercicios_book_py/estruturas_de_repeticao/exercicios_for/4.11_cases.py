# comece seu programa com o exercicio 4.1. faça uma cópia da lista de pizzas e chame-a dee friend_pizzas.Então faça o seguinte
# adicione uma nova pizza à lista original
# adicione uma pizza diferente à lista friend_pizzas
# prove que você tem duas listas diferentes.Exiba as mensagens "minhas pizzas favoritas são", em seguida, use o laço FOR para exibir a primeira lista.
# exiba a mensagem "as pizzas favoritas do meu amigo são:", em seguida,utlize um laço for para exibir a segunda lista

pizzas = ['pepperoni', 'portuguesa', '4 queijos']
friend_pizzas = pizzas[:]

pizzas.append('gorgonzola com mel')
print(pizzas)
friend_pizzas.append('pepperoni com margherita')
print(friend_pizzas)
print('minhas pizzas favoritas são: ')
for pizza in pizzas:
     print(pizza)
print('as pizzas favoritas do meu amigo são: ')
for pizza_friend in friend_pizzas:
     print(pizza_friend)
