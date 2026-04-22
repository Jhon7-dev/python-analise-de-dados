nota = float((input('DIGITE SUA NOTA: ')))
comportado = True if input('Comportado (y/n): ' ) == 'y' else False
if nota>=9:
     print('Parabéns, você está aprovado!')
elif nota >= 7:
     print('aprovado')
elif nota >= 5.5:
     print('Recuperação')
elif nota >= 3.5:
     print('recuperação + trabalho')
else:
     print('Reprovado!')
print(nota)