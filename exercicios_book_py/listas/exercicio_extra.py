# peça ao usuário para digitar sseu nome
# peça ao usuário para digitar sua idade
# se nome e idade forem digitados
# EXIBA :
# seu nome é {nome}
#  seu nome invertido é {nome invertido}
#  se o nome contém ou não espaços
#  seu nome tem {n} letras
#  primeira letra do seu nome é 
#  a última letra é {letra}
# se nada for digitado em nome ou idade 
#  exiba "desculpe mas você deixou os campos vazios"

print('olá, usuário! seja bem vindo!')
nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')

if nome_usuario and idade_usuario:
     print('Seu nome é : ' + nome_usuario)
     print('Sua idade é : ' + idade_usuario)
     print('Seu nome invertido é : ' + nome_usuario.sort(reverse=True))
     