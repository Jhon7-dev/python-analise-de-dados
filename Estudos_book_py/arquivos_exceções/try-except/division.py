# obs: qualquer cód que dependa do sucesso do TRY é adicionado no bloco else
#  se a operação do bloco try for bem sucedida, usamos o bloco ELSE para exibir o resultado
# o bloco except diz como deve responder um ZeoDivisionError
# Se a instrução try não for bem-sucedida por causa de um erro de divisão por zero, mostraremos uma mensagem
print('digite dois números e irá dividí-los')
print("digite 'q' para sair.")
while True:
     num1 = input("\nNúmero 1: ")
     if num1 == 'q':
          break
     num2 = input("\nNúmero 2: ")
     if num2 == 'q':
          break
     try:
          calculo = int(num1)/ int(num2)
     except ZeroDivisionError:
          print('Nãp pode efetuar a divisão por zero!')
     else:
          print(calculo, '\ndivisão efetuada com sucesso! ')
print('Encerrando Programa....')
print("Programa encerrado!")