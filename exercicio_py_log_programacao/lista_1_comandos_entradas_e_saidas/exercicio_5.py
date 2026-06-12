# Criar um programa em Linguagem C que receba dois números inteiros e
# retorne: o valor da divisão e o resto da divisão.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

def calculo(num1,num2):
     try:
          if num1 > num2:
               resto =  num1 % num2
               div = num1 / num2
          return print(f'a divisão do número {num1} pelo {num2} é {div} e o resto é {resto}')
     except:
          print('erro!')
print(calculo(numero_1,numero_2))