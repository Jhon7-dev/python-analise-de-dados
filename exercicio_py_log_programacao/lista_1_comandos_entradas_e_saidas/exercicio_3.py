# Receber um comprimento em metros, convertê-lo para centímetros e
# mostrar o resultado.

comp_metros = float(input('Digite quantos metros: '))

def conversor(cm):
     cm = comp_metros*100
     return print(f'A medida convertida de Metros para Centímetros é {cm} cm')
print(conversor(comp_metros))