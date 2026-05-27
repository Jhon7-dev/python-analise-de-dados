import cmath
import random
nome = "joão victor"
sobrenome = "gomes de souza"
idade = 22
altura = 1.76
print("Meu nome é ", nome.title(),sobrenome.title(), 'tenho ', idade, ' anos e minha altura é ', altura )

a,b,c = 22,7.7777," hello , world"
print(a,b,c)

meuNome = "joão Victor gOmes DE sOuZa"
minhaIdade = 22
meuEnd = "Rua carlos reinaldi"

print('meu nome é', meuNome.title(),', minha idade é ', minhaIdade,'e meu endereço fica na', meuEnd)

PI = 3.14
GRAVIDADE = 9.8

print('O valor de pi é', PI, ' e a gravidade da lua é ', GRAVIDADE)

v= 120
print(v)
v = 'agora eu sou string'
print (v)

a= 27
b=1.434
c = 3j

print(a)
print(b)
print(c)
print('-------------------')
print(type(a))
print(type(b))
print(type(c))
print('-------------------')
a=23.3
b=232.3
c=-232323.3
print(type(a))
print(type(b))
print(type(c))
print('-------------------')
a=23
b=232
c=232323
print(type(a))
print(type(b))
print(type(c))
print('-------------------')
e = 34101e4
print(type(e))
print(e)
print('-------------------')
E = 3.4242e-2
print(type(E))
print(E)
print('-------------------')
print(1.789e308)
print(1.89e308)
print('-------------------')
print(5e-324)
print(5e-325)
print('-------------------')
a = 2+4j
b = -4j
c = complex(3,5)
print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)
print('-------------------')
print(c.real)
print(c.imag)
print('-------------------')
x = complex(4,3)
y = complex(-1,4)
z = complex(2,1)
print(x+y+z)
print(x*y*z)
print(x*2)

print('-------------------')
print(cmath.phase(x))
print(cmath.phase(complex(-1.0,0.0)))
print(cmath.phase(complex(-1.0,-0.0)))
print(cmath.pi)
print(cmath.e)
print('-------------------')
print(random.randrange(1,100))
print(random.randrange(1,90))
print(random.randrange(1,100000000))
print('-------------------')
k=3
i=7.53
z = 4j
x=4
y=4
d=4
print(type(k))
print(type(i))
print(type(z))
print(complex(k))
print(complex(x))
print(complex(y))
print(complex(d))
print('-------------------')
print(float(k))
print(int(i))

print('-------------------')
print(0b01111111)
print(0b01111111)
print(0o10)
print(0o10)
print(0xff)
print(0xffff)
print(0xfff)
print(0xaaa)
# print(255)
print('-------------------')
print(int('0xff',16))
print(ord('A'))
print(ord('X'))
print(ord('<'))
print('-------------------')
print('String é um elemento importante da programação')
print("String é um elemento importante da programação")
print("""String é um elemento importante da programação e podemos ultilizar até para digitar cpfs """)
print('-------------------')
print("podemos usar aspas dentro das\"strings\"")
print('podemos usar aspas dentro das\'strings\'')

s = "Rafael"
print(s[0])
print(s[-6])
print(s[5])
print(s[-1])


nome = "John Von Neumann"
print(nome[5:14])
print(nome[5:9])
print(nome[::-1])
print(nome[::-2])
print(nome[::-3])