contador = 0
# while contador < 10:
#      contador +=1
#      print(contador)
# print('acabou')

# cont = 0

# var = input('digite um número para tabuada ')

# while cont <= 10:
#      cont +=1
#      mult = cont**var
#      print(var + ' x ' + cont + ' = ' + mult)
# print('acabou')

while contador <= 100: 
     contador +=1 # ESSA LINHA É IMPORTANTE POR CAUSA DO 'CONTINUE'
     print(contador)
     if contador == 6:
          print('não mostrar o 6.')
          continue
     if contador == 40:
          break
print('acabou')