#  você acabou de encontrar uma mesa de jantar maior, portanto tem mais espaço disponível. Pense em mais três convidados para o jantar
# comece o programa com exercício anterior e acrescente a instrução print no final do seu programa informando às pessoas que você encontrou uma mesa e jantar maior.
# utilize o insert() para adicionar um novo convidado no inicio de sua lista
# utilize o insert() para adicionar um novo convidado no meio de sua lista
# utilize o append() para adicionar um novo convidado no final de sua lista

nomes = ['Tom Hanks', 'Alx Rose', 'Michael Jackson']
# alterando os nomes da lista de convidados
nomes [0] = 'Belo'
nomes [2] = 'Leonardo Di Caprio'
print(nomes)
# segundo conjunto de mensagens para os novos convidados

message_nome_0_novo = "Olá, " + nomes[0] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã "
message_nome_2_novo = "Olá, " + nomes[2] + "! gostaria de te convidar para um jantar de amigos que vai acontecer amanhã "
print(message_nome_0_novo)
print(message_nome_2_novo)

#  informando às pessoas que a mesa é maior
print("Encontrei uma mesa maior e posso chamar mais convidados para o jantar! ")

# inserindo um convidado no índice 0 da minha lista
nomes.insert(0,'Ringo Stars')
print(nomes)
# inserindo um convidado no meio da lista 
nomes.insert(3,'Slash')
print(nomes)
# usando o append para adiconar um convidado no final da lista
nomes.append('Matt Sorum')
print(nomes)

# mensagem para os novos convidados
message_novoConvidado_0 = "Olá, " + nomes[0] + "! gostaria de te convidar para um jantar de amigos."
print(message_novoConvidado_0)
message_novoConvidado_1 = "Olá, " + nomes[3] + "! gostaria de te convidar para um jantar de amigos."
print(message_novoConvidado_1)
