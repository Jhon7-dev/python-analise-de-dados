# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

senha = ''
nome_usuario = ''

while True:
     nome_usuario = input('Nome: ')
     senha = input('senha: ')
     
     if senha == nome_usuario:
          print('Erro! digite novamente')
          continue
     else:
          print('senha e nome cadastrado com sucesso! ')
          break
print('Programa encerrado com sucesso!')