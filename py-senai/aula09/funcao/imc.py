def imc (peso,altura):
     calculo_imc = peso / (altura**2)
     if calculo_imc < 18.5:
          return 'Abaixo do peso'
     elif calculo_imc <24.9:
          return 'peso normal'
     else:
          return 'sobrepeso'
# print(imc(peso_pessoa,altura_pessoa))
peso_pessoa = int(input('digite seu peso: '))
altura_pessoa = float(input('digite sua altura:  '))
print(f'O calculo do Imc é : {imc(peso_pessoa,altura_pessoa)}')  
