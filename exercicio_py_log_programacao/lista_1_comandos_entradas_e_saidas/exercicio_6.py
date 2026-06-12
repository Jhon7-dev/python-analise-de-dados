# Receber base e altura de um triângulo, calcular sua área e exibir o valor
# calculado.
num_1 = int(input("Digite a base do triângulo: "))
num_2 = int(input("Digite a Altura do triângulo: "))

def calcula_area(base,l):
     try: 
          if l > base:
               area = (base * l) / 2
               return print(f'a Base do triângulo é {base} e a Altura é {l}. A área do Triangulo é {area}')
     except:
          print('erro! base menor que a altura')
print(calcula_area(num_1,num_2))