# fazer uma cadeia if-elif-else
# se a cor for verde informe que ganhou 5 pontos
# se a cor  for amarelo informe que ganhou 10 pontos
# se a cor  for vermelho informe que ganhou 15 pontos

cor_alien = input("Digite um cor: ")
if cor_alien == 'verde':
     print('cor: ' + cor_alien +  ' ganhou 5 pontos')
elif cor_alien == 'amarelo':
     print('cor: ' + cor_alien + ' ganhou 10 pontos')
elif cor_alien == 'vermelho':
     print('cor: ' + cor_alien + ' ganhou 15 pontos')
else:
     print('errorr')
     