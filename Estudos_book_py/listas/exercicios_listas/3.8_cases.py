# 5 lugares do mundo que gostaria de visitar
#  armazene em um lista e q não esteja em ordem alfabetica
# exiba sua lista em ordem original.
# Utilize sorted() para exibir a lista em ordem alfabetica, sem modificar a lista propriamente dita
# mostre que sua lista manteve sua ordem original exibindo-a
# Utilize sorted() para exibir em ordem alfabetica inversa sem alterar a ordem original
# mostre que sua lista manteve sua ordem original exibindo-a
# utilize o reverse() para mudar a ordem de sua lista novamente.Exiba a lista para mostrar que ela voltou à sua ordem original
# utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética.Exiba a lista para mostrar que sua ordem mudou.
# utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa.Exiba a lista para mostrar  que sua ordem mudou
#

places = ['italia','uruguay','argentina','florianopolis','pipa']

# exibindo em ordem original
print('minha lista na ordem original é ' + str(places))

# utilizando o sorted() para exibir a lista em ordem alfabetica
places = ['italia','uruguay','argentina','florianopolis','pipa']
print(sorted(places))

# lista em ordem original
print(places)

# colocar em ordem alfabetica inversa
# places.sorted(reversed = True)
# print(places)
# mostrando em sentido original 
print(places)

# utilizando o reverse()
places = ['italia','uruguay','argentina','florianopolis','pipa']
places.reverse()
print(places)
# volta a lista normal original
places = ['italia','uruguay','argentina','florianopolis','pipa']
print(places)

# sort()
places = ['italia','uruguay','argentina','florianopolis','pipa']
places.sort()
print(places)
# volta a lista normal original
places = ['italia','uruguay','argentina','florianopolis','pipa']
print(places)
#  sort() para ordem alfabética inversa
places = ['italia','uruguay','argentina','florianopolis','pipa']
places.sort(reverse=True)
print(places)
# volta a lista normal original
places = ['italia','uruguay','argentina','florianopolis','pipa']
print(places)