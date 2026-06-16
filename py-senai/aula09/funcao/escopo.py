def externa():
     x = 13
     print(x)
     print(f'valor de x = {x}')
     def interna():
          x = 14
          print(f'valor de x = {x}')
     interna()
x = 15
externa()
print(f'valor de x = {x}')
def externa():
     global x
     x = 30
     print(f' x = {x}')
     # print(x)
     def interna():
          # x = 14
          # print(f'valor de x = {x}')
          print(f' x = {x}')
     interna()
     print(f' x = {x}')
     
x = 10
externa()
print(f' x = {x}')

# print(f'valor de x = {x}')
def f(x):
     x+=1
     print('Em f(x): x = ',x)
     return x
x=100
z = f(x)
print(z)

def func_a():
     print('dentro da func_a')
def func_b(y):
     print('dentro da func_b')
     return y
def func_c(z):
     print('dentro da func_c')
     return z()
print(func_a())
print(5+func_b(2))
print(func_c(func_a))

def f (y):
     x = 1
     x += 1
     print(x)
x=5
f(x)
print(x)

# def h(y):
#      x +=1
# h(x)
# print(x)

def anime():
     nome = 'joao'
     print(locals())
anime()
globals() is locals()


def soma(*args):
     total = 0
     for num in args:
          total += num 
     return total
print(soma(2,3,4,6))
print(soma(2,3,4,6,42,12,12,4124,12))
print(soma(2,3))
print(soma(2,101))


def pessoa (**kwargs):
     print(kwargs)
     for nome,idade in kwargs.items():
          print(f'{nome} tem atualmente {idade} anos de vida')
pessoa(joao='22',daniel='12',sandro='8',amir='11')