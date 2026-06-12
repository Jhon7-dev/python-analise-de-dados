#  Receber uma temperatura em Fahrenheit e convertê-la para Celsius
# através da seguinte fórmula: Celsius = (Fahrenheit - 32) / 1.8. Exibir o
# valor em Celsius.

print('---- conversor de temperatura ----')
temperatura = float(input("DIGITE A TEMPERATURA: "))
def conversor_temp(temp):
     return(temp - 32)*(5/9)
print('a Temperatura convertida de Fahnheit para Celsius é ',conversor_temp(74))
celsius = float(input("temperatura em celsius: "))
print(conversor_temp(celsius))
celsius = conversor_temp(70.76)
print(celsius)