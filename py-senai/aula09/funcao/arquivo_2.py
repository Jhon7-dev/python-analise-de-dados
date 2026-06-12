def cumprimentar(nome):
    return  print("ola {0} seja bem vindo".format(nome))
print(cumprimentar('Gabriel'))

def padrao(valor = 100):
     print("o valor definido foi: " + str(valor))
padrao()
padrao(10)
padrao(20)
print(padrao.__doc__)

def func():
    return
x = func()
print(x)

x = 13
print(id(13))
print(id(x))

print(f'id(x) = {id(x)}')
x = x+1
print(f'id(x) = {id(x)}')
print(f'id(14) = {id(14)}')
y = 13
print(f'id(13) = {id(13)}')