# escreva um laço while que permita aos usuários fornecer o nome de um artista e o título de um álbum. Depois que tiver essas informações, chame o make_album() cooms as entradas do usuário e apresente o dicionário criado. incluir valor de saída do while

def make_album(nome_cantor,nome_album):
     full_dicionary = nome_cantor + ' ' + nome_album
     return full_dicionary

while True:
     print("\n album")
     print("(digite '1' a qualquer momento para sair)")
     nome_cantor = input('nome do cantor: ')
     if nome_cantor == '1':
         break
     nome_album = input('nome do àlbum: ')
     if nome_album == '1':
         break
     info = {'nome do grupo_cantor: ': nome_cantor,'nome do album: ' : nome_album}
     print (info)

     