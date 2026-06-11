animais = ["cachorro","gato","elefante"]

print("os animais são".upper())
for ani in animais:
     print(ani)
animais.append("pato")
print("os animais são".upper())
for ani in animais:
     print(ani)

for string in "Programaçã com Python":
     print(string)
for string in "programação in java , javacript , c , c++, cobol, go, html, css ":
     print(string,end=' ')
x = range(0,10)
print(type(x))
print(list(x))
y = range(4,30,2)
print(list(y))

for i in range(10):
     print(i)
for data in range(1995,2018):
     print(data)
albuns = ["pra ver o sol brilhar","desafio","primavera","ao vivo 10 anos","pra ser amor","seu fã","tudo mudou"]
print("Álbuns da carreira solo do Belo")
for a in albuns:
     print(a)
     
paises = ['china', 'india','tailandia','nepal','camboja','brasil']
for pais in paises:
     print(pais)
     if pais == 'nepal':
          break
import pycountry
linguagens = ["java" ," javacript" , "c" , "c++", "cobol", "go", "html", "css "]
for linguagem in linguagens:
     if linguagem == "Javascript":
          continue
     print(linguagem)
for x in range(10):
     if x % 2 == 1:
          continue
     print(x)
for x in range (100):
     print(x)
else:
     print("loop finalizado com sucesso!")
     
cores = ["azul",'verde',"amarelo"]
numeros = [1,2,3]
for cor in cores:
     for numero in numeros:
          print(f'{cor.capitalize()} - {numero}')
          
alimentos = ['arroz','feijão','batata']
for indice,alimento in enumerate (alimentos):
     print(f'{indice} -> {alimento}')
     
     
alimentos = ['arroz','feijão','batata','carré',"carne assada","limão","Feijão de corda","Baião de dois",'farofa']
for indice,alimento in enumerate (alimentos,100):
     print(f'{indice} -> {alimento.title()}')

numero = int(input('Digite um número para a tabuada '))
print(f"tabuada de número {numero}")
for num in range(1,11):
     print(numero, " x ",num," = ", num * numero, )