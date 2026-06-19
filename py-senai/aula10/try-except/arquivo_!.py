try:
     resultado = 10/int(input("Digite um número: "))
except ZeroDivisionError:
     print("Erro: VocÊ tentou dividir por zero!")
except ValueError:
     print("Error: você digitou um número válido")