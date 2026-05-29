from datetime import datetime


print(('gabriel\tFelippe'.isprintable()))
print(('gabriel\tFelippe'.isprintable()))
print("".isprintable())
print()

print(''.isspace())
print('x'.isspace())
print(' '.isspace())
print('\t\n'.isspace())

print("STRING".isupper())
print("String".isupper())
print("String".islower())
print("Srting".islower())

'python'.center(20)

print('python'.center(25,'.'))
print('python'.center(20))

print('javascript'.rjust(20))
print('javascript'.rjust(20,','))
print('letra'.zfill(7))

print('-------------------')
nome = "João Victor Gomes De Souza"
profissao = "Programador"
print("a profissão de {0} é {1}".format(nome,profissao))

# tag = 'p'
# texto = 'Este é um paragrafo'
# sentenca = '<{0}>{1}</{0}}'.format(tag,texto)
# print(sentenca)
valor = '1 GB É IGUAL A {:,} bytes'.format(10**9)
print(valor)
print("{:d}".format(4))
print("{:x}".format(15))

print("{:}".format([20,30]))

nome = "joao"
amigo = "lennon"
print("%s é amigo de %s"%(nome,amigo))

print("%3.5f"%(3.12345678))
print("%2.4f"%(3.12345678))

first_name = "alan"
last_name = "delon"
sentanca = f'meu nome é {first_name.upper()} {last_name.lower()}'
print(sentanca)


pessoa={'nome':'joao victor','idade':22}
sentenca = f'Meu nome é {pessoa["nome"]} e eu tenho {pessoa["idade"]}anos de idade'
print(sentenca)

calculo = f'4 vexes 11 é igual a {4*11}'
print(calculo)

nascimento = datetime(1991,6,6)
sentenca = f'o nascimento é no dia {nascimento:%B %d,%Y}'
print(sentenca)

x = 10 
y =[1,3.14,17,13]
print(type(repr(x)))
print(type(str(y)))
print("meu nome é \njoão victor")
print("olá, my friends")

nome = "carl"
sobrenome = "jhonson"


print(nome+ " " + sobrenome)
print(nome*10)

print("C" in nome)
print("C" not in nome)

print("Carregando", end='....')
print('feito!')