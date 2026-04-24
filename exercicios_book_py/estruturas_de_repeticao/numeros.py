#  função RANGE()
# facilita gerar uma série de números

for valor in range(1,5):
     print(valor)
#  a função range conta no primeiro valor que for fornecido e termina no último valor especifícado
# não conterá o valor final, 5
# 'começa no 1 e termina no 4'

# usando RANGE() para criar uma lista de números
#  pode converter os resultados de range() diretamente em uma lista usando a função list().
# quando colocamos list() em torno de uma chamada à função range(), a saída será uma lista de números.

numeros = list(range(1,6))
print(numeros)

# listando os PARES de 1 a 10
numeros_pares=(list(range(2,11,2)))
print(numeros_pares)
#  a função RANGE() começa com o valor 2 e então soma 2 a esse valor.
# o valor 2 é somado repetidamente até o valor final, que é 11, ser alcaçado 

#  colocando os 10 primeiros quadrados perfeitos
quadrados=[]
for valor in range(1,11):
     quadrado = valor**2
     quadrados.append(quadrado)
print(quadrados)

# list comprehension 
# combina a criação de laço for e criação de novos elementos em um linha e concatena cada novo elemento automaticamente

cubos = [valor**3 for valor in range(2,11)]
print(cubos)

#  para essa sintaxe, comece com um nome descritivo para a lista, por exemplo, cubos.
