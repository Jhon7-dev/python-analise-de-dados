#  você acabou de descobrir que sua nova mesa de jantar não irá chegar a atempo e tem espaço só para dois convidados
#  comece o programa com o programa anterior e adicione uma mensagem que só vai poder convidar apenas dois convidados
# utilize o método pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.
# utilize o del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final do seu programa
nomes = ['Tom Hanks', 'Alx Rose', 'Michael Jackson']
# alterando os nomes da lista de convidados
nomes [0] = 'Belo'
nomes [2] = 'Leonardo Di Caprio'
print(nomes)


# inserindo um convidado no índice 0 da minha lista
nomes.insert(0,'Ringo Stars')
print(nomes)
# inserindo um convidado no meio da lista 
nomes.insert(3,'Slash')
print(nomes)
# usando o append para adiconar um convidado no final da lista
nomes.append('Matt Sorum')
print(nomes)

#  mensagem informativa
print("Desculpe, meus amnigos apenas 2 pessoas poderão jantar comigo. ")

#  método pop()
popped_nome_0 = nomes.pop(0)
print("Infelizmente, " + popped_nome_0 + " você não poderá comparecer ao jantar, pela falta de lugar na mesa.")

popped_nome_3 = nomes.pop(3)
print("Infelizmente, " + popped_nome_3 + " você não poderá comparecer ao jantar, pela falta de lugar na mesa.")
print(nomes)
popped_nome_3_new = nomes.pop(3)
print("Infelizmente, " + popped_nome_3_new + " você não poderá comparecer ao jantar, pela falta de lugar na mesa.")
print(nomes)
popped_nome_2_new = nomes.pop(2)
print("Infelizmente, " + popped_nome_2_new + " você não poderá comparecer ao jantar, pela falta de lugar na mesa.")
print(nomes)

# del
del nomes [0]
print(nomes)
del nomes[0]
print(nomes)


