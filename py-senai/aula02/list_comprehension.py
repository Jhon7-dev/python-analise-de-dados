quadrados = []
valores = [-1,-1333,21,-23123,23,-1.235,6,7,8,9,10,11,12]
for v in valores:
     quadrados.append(v**2)
print(quadrados)
print('os quadrados dos números são: ')
print([v**2 for  v in valores])

print([v for v in valores if v%2 == 0])
print([v for v in valores if v>0])
print([v for v in valores if v<=0])

matriz = [[i for i in range(10)] for _ in range(100)]
print(matriz)

celsius=[33.2,26.7,38.5,40.5]
fah = [((float(9)/5)*t+32) for t in celsius]
print(fah)
print('lista de animais e alimentos - PRODUTO CRUZADO')
animais = ['gato','cachorro','lagarto']
alimentos = ['tomate','alface','abacate']
print([(animal,alimentos)for animal in animais for alimento in alimentos])

from math import sqrt
print([sqrt(n) for n in range(1000)])


print("---------------------------------------------")
print('os números primos de 2 até 1000 são '.upper())
print([x for x in range (2,1000) if all(x % y != 0 for y in range(2,x))])