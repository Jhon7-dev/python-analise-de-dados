def define_idade(idade):
     if idade < 0:
          raise ValueError("A idade não pode ser negativa! ")
     return define_idade
try:
     define_idade(-5)
except ValueError as e:
     print(f'Erro de validação {e}')