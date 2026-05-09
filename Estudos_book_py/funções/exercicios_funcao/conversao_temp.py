# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa.
# Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
# Conversão entre Celsius e Farenheit

def converter_fah(temp_celsius):
     f = (temp_celsius*1.8) + 32
     return f
def converter_celsius(temp_f):
     c = 5/9 *(temp_f-32)
     return c
# temperatura_fare = converter_fah(40) // 104
# print(temperatura_fare)
# temperatura_celsius = converter_celsius(104) //40
# print(temperatura_celsius)
opcao= ''
while opcao != '3':
     print('=== Conversor ===')
     print('1 - F => C')
     print('2 - C => F')
     print('3 - SAIR')
     opcao = input('escolha a opção: ')    
     if opcao == '1':
          print('ok, vamos converter Farenheit em Celsius')
          print('Digite o valor da temperatura em ºF: ')
          celsius = input(float(('temperatura: ' + ' º '))) 
          if celsius == 3:
               break
          conversao_celsius = converter_celsius(celsius)
          print('Temperatura convertida!')
          print('Temperatura é ' , conversao_celsius , ' graus Celsius')
     elif opcao == '2':
          print('ok, vamos converter Celsius em  Farenheit')
          print('Digite o valor da temperatura em ºC: ')
          farenheit = input(float('temperatura: ' + 'º '))
          if farenheit == 3:
               break
          conversao_farenheit = converter_fah(farenheit)
          print('Temperatura convertida!')
          print('Temperatura é ', conversao_farenheit , ' Farenheit')
     else:
          break
print('programa encerrado!')