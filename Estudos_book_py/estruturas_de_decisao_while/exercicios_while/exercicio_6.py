#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro
cont = 1
print('\n com while')

while cont < 20:
     cont+=1
     print(cont)
print('\nagora com o for')
for cont in range(1,21):
     print(cont)