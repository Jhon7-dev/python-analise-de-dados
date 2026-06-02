l = ['M','O','N','T','Y','','P','y','t','h','o','n']
print(l)
print('Essa lista tem ', len(l), 'elementos')

alfabeto = []
alfabeto.append('a')
alfabeto.append('b')
alfabeto.append('c')
alfabeto.append('d')
alfabeto.append('e')
alfabeto.append('f')
alfabeto.append('g')
alfabeto.append('h')
alfabeto.append('i')
print(len(alfabeto))
alfabeto.insert(0,"l")
print(alfabeto)
print(len(alfabeto))

nome = ''.join(l)
print(nome)

ciencias = ['física','química','matemática']
numeros = [1,2,3,4,5,6,7,8,9,10]
hibrida = [1,2.3,'joao']
print('as matérias de ciencias são: ', ciencias)
print('os números  são: ', numeros)
print('a lista mista é : ', hibrida)

print(ciencias[0:2])
print(numeros[2])
print(hibrida[-1])
print(ciencias[:])
print(numeros[:6])
print(numeros[2:])
print(numeros[0:10:2])
ciencias[slice(0,2)]
print(ciencias[slice(0,2)])
print(numeros[slice(0,10,2)])
ciencias +=['astronomia','biologia','fisica quantica']
print(ciencias)

for n in numeros:
     print (n)
numeros.append(11)
numeros.append(12)
numeros.append(13)
numeros.append(14)
numeros.append(15)
numeros.append(16)
print(numeros)
numeros.extend([50,40])
print(numeros)
hibrida.insert(0,"Gabriel")
print(hibrida)

lista_1 = [2,1,6,3,24,23,2412]
lista_1.remove(2)
print(lista_1)
lista_1.remove(3)
print(lista_1)
del(lista_1[2])
print(lista_1)
lista_1.pop()
print(lista_1)

ciencias.remove("química")
print(ciencias)
ciencias.clear() # vai limpar a lista
print(ciencias)

pares = list((2,4,6,8))
print(pares)

primos = [2,7,11,13,17]
negativos  = [-1,-2,-5,8,-3]
reais  = [1.5,3.9,3/4,1,-0.1]

print('os numeros primos são ')
for primo in primos:
     print(primo)
print('os numeros negativos são ')
for negativo in negativos:
     print(negativo)
print("Os reais são")
for real in reais:
     print(reais)

print('concatenando primos e negativos fica')
concate = primos + negativos 
for conca in concate:
     print(conca)
print(primos*2)
reais.sort
print(reais)
print(sorted(negativos))
print(sorted(negativos,reverse=True))
total = 0
print('a soma dos números primos são: ')
for i in range(len(primos)):
     total+=primos[i]
print(total)

total = 0
for i in primos:
     total+=i
     print(total)