# x = 10

while x != -1:
     x = float(input('informe o nª ou -1 para sair: '))
     if x != -1:
          qtd += 1
          total += x
     
print(f'A média da turma é {total/qtd}')
     