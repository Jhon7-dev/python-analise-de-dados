cars = ['audi','bmw','toyota','subaru']
for car in cars:
     if car == 'bmw':
          print(car.upper())
     else:
          print(car.title())

# verificando igualdade
# maioria dos testes condicionais comapra o valor aual de uma variável com valor específico de interesse

car ='bmw'
car == 'bmw'

# verificando se um valor está em uma lista
# toda vez que eu quiser verificar se um novo nome de usuário ja existe 
# utiliza a palavra IN 

ingredientes = ['queijo','cebloa','alface']
'queijo' in ingredientes
if 'queijo' in ingredientes:
     print('hi')
else:
     print('loves')

# verificando se um valor não está em uma lista
# usa a palavra NOT
ingredientes = ['queijo','cebloa','alface']
ing = 'picles'
if ing not in ingredientes:
     print('não tem na lista picles')
else:
     print('erro, tem na lista')