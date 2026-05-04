

opcao = 0

while opcao != '5':
     print('CALCULADORA')
     print('1 - SOMA')
     print('2 - SUBTRAÇÃO')
     print('3 - MULTIPLICAÇÃO')
     print('4 - DIVISÃO')
     print('5 - SAIR ')
     opcao = input('Escolha a operação:  ')
  
    
    
          
     number_1= float(input('escolha o 1ª número: '))
          
     number_2 = float(input('escolha o 2ª número: '))
          
     if opcao == '1':
          print('A soma dos números é: ', number_1 + number_2)
     elif opcao == '2':
          print('A subtração dos números é: ', number_1 - number_2)
     elif opcao == '3':
          print('A multiplicação dos números é: ', number_1*number_2)
     elif opcao == '4':
          print('A divisão dos números é: ', number_1/number_2)
     else:
          print('opção 5 digitada.')
          print('carregando...')
          break
print('fim de programa.')
