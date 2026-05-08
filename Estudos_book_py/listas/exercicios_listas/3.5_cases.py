#  você acabopu de saber que um de seus convidados não poderá comparecer, portanto vai ter que fazer um novo conjunto de convites.
#  comece com o programa anterior  e ao final coloque uma instrução prin, especificando o nome do convidado que não poderá comparecer 

#  modifique sua lista, substituindo o nome do convidado que não poderá comparecer  pelo nome da nova pessoa que você está convidando

#  exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua prensete em sua lista
nomes = ['Tom Hanks', 'Alx Rose', 'Michael Jackson']
message_nome_0 = "Olá, " + nomes[0] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã."
message_nome_1 = "Olá, " + nomes[1] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã."
message_nome_2 = "Olá, " + nomes[2] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã."
print(message_nome_0)
print(message_nome_1)
print(message_nome_2)

print(nomes[0] + " E "+ nomes[2])

# alterando os nomes da lista de convidados
nomes [0] = 'Belo'
nomes [2] = 'Leonardo Di Caprio'
print(nomes)

# segundo conjunto de mensagens para os novos convidados

message_nome_0_novo = "Olá, " + nomes[0] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã "
message_nome_2_novo = "Olá, " + nomes[2] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã "
print(message_nome_0_novo)
print(message_nome_2_novo)