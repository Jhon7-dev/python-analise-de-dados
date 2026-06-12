# . Receber dois valores, calcular sua média aritmética e exibir o resultado

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

def calculo_media(num1,num2):
     soma = num1 + num2
     media = (soma)/ 2
     return  print(f'a soma do número {num1} com o número {num2} é {soma} e a média é {media}')
print(calculo_media(num_1,num_2))