print('As linguagens de programação em tupla são'.upper())
linguagens = ("Python","Java","Javascript","Ruby","Perl","CSS") #tuplas são mutáveis nao da para alterar dentro da lista
print(linguagens)
print(type(linguagens))
print(linguagens[0:2])
print(linguagens[-1])
print(linguagens[:-2])
print(linguagens[:])
# print(linguagens[0] = 'c++')
x = (1,2)
y = (3,4)
z = x+y
print(z)
# imprimindo elementos em uma tupla
print('===========================================')
print('dados do estudante'.upper())
estudante = ('joao',29,2003,"brasil")
print(estudante)
print('===========================================')
print('dados do estudante'.upper())
print('===========================================')

for e in estudante:
     print(e)
print([e for e in estudante])
print('gabriel' in estudante)
print(1990 in estudante)
print('japão' not in estudante)
print('brasil' not in estudante)
print(len(estudante))

# del estudante
# print(estudante)

numeros = tuple(x for x in range(1,20,3))
print(numeros)
print(numeros.count(7))# retorna a quantidade de vezes que um número repete
print(numeros.index(19))# retorna o indece do elemento
