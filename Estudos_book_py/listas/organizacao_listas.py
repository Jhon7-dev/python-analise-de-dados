#  ordenando uma lista em ordem alfabetica
# altera de forma permanente
#  SORT()

carros =['bmw','ferrari','volvo','toyota','honda','audi']
carros.sort()
print(carros)

# ordenando inversamente
carros =['bmw','ferrari','volvo','toyota','honda','audi']
carros.sort(reverse=True)
print(carros)

# ordenando uma lista temporariamente
# SORTED()
carros =['bmw','ferrari','volvo','toyota','honda','audi']
print('Aqui está a lista original ' + str(carros))
print('\n Aqui está a sorted list: ')
print(sorted(carros))
print('aqui está a lista original novamente: ')
print(carros)

# exibindo uma lista em ordem original
# método REVERSE()
# ele inverte a ordem
# mas se quisermos mudar a ordem original so aplicar o reverse() à lista de novo
carros =['bmw','ferrari','volvo','toyota','honda','audi']
carros.reverse()
print(carros)

# Tamanho de uma lista
#  função LEN()
carros =['bmw','ferrari','volvo','toyota','honda','audi']
# len(carros)
print(len(carros))
