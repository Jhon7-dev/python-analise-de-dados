# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# nota = 0
contador = 0
while True:
     nota =float(input('digite uma nota: '))
     if (nota < '0') or  '10':
          print('Inválido!')
     else:
          print('válido')
          break
print('nota : ' ,  nota)