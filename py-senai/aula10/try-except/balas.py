try:
     balas = int(input("Digite a quantidade de balas: "))
     alunos = int(input("Digite a quantidade de alunos: "))
     
     resultado = balas/alunos
except ValueError:
     print("Erro: Por favor, digite apenas números inteiros. ")
except ZeroDivisionError:
     print("Erro: Não é possível dividir balas por zero alunos. ")
except Exception as e: 
     print(f"Ocorreu um erro inesperado: {e}")
else:
     print(f"Cada aluno receberá {resultado:.2f} balas.")
finally:
     print("operação finalizada")