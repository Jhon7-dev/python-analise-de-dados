# conversor de temp
# 

print('---- conversor de temperatura ----')
# temperatura = float(input("DIGITE A TEMPERATURA: "))
def conversor_temp(temp):
     f = (temp *9/5) + 32
     return f

temp_c = float(input("temperatura em celsius: "))
print(f'{temp_c} a Temperatura convertida de Fahnheit para Celsius é {temp_c}°F')
# print(conversor_temp(celsius))
# celsius = conversor_temp(70.76)
# print(celsius)