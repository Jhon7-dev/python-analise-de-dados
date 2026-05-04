# laço while
# contador = 1

# while contador <= 5:
#      print(contador)
#      contador +=1
     
#  deixando o usuário decidir se quer sair ou não 
prompt = "\ndiga algo que eu vou repetir: "
prompt += "\ndigite 'quit' para o fim do programa. "
active = True

# defino active como True para o programa começar ativo
# enquanto tiver ativo vai executar

message = " "
while active:
     message = input(prompt)
     if message == 'quit':
          # aqui no if, verificamos se o valor de messege depois do usuário fornece sua entrada
          # se o usuário fornecer 'quit',definimos active com False e o laço while é encerrado
          active = False
     else:
          print(message)
                    
print('programa encerrado')
          # print('programa encerrado')

# usando break para sair do laço 
