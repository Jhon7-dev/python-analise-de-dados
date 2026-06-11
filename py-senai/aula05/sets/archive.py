s = {1,1,2,3,3,4}
print(type(s))
print(s)

k = set([1,2,3,4,5])
print(type(s))
print(k)


for itens in k:
     print(itens)
k.add(8)
print('numero adicionado')
print(k)
print(len(set('cachorro')))

x = {1,2,3,9000,-1,-2323,444,100000}
y = {1,2,3,123,2441,34512513,345145124,51,34343,23523,234,15235}

print (x&y)
print (x.intersection(y))
print(x-y)
print(x.difference(y))


print(y-x)
print(y.difference(x))

print(x.symmetric_difference(y))
print(x.symmetric_difference(x))
print(x^y)
print(y^x)
print(x|y)
print(x.union(x))

print(1 in x)
print(5 in x)
print(10 not in x)
print(20 not in x)