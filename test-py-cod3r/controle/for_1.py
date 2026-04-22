# for i in range(10):
#      print(i)
# for i in range(1,10):
#      print(i)
# for i in range(1,100,5):
#      print(i) 
     
# nums = [2, 4, 6,8]

# for n in nums:
#      print ( n, end=',')

# texto = 'python !!!'

# for letra in texto:
#      print(letra, end=' ')
     
     
produto = {
     
     'nome': 'Caneta',
     'preco': 8.80,
     'desc': 0.5
}
for atrib in produto:
     print (atrib, produto[atrib])
for atrib, valor in produto.items():
     print(atrib, '=>', valor)