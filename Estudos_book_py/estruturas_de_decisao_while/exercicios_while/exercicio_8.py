# Faça um programa que leia 5 números e informe a soma e a média dos números
cont = 0
soma = 0
média = 0
while cont<3:
     cont+=1

     number = float(input('digite o número: '))
     
     soma  +=number
     media = soma/number

print('a média dos números é: ', media)
print('programa finalizado')