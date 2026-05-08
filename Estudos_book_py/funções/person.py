# DEVOLVENDO UM DICIONÁRIO
# UMA FUNÇÃO PODE DEVOLVER UM QUALQUER TIPO DE VALOR, INCLUINDO LISTAS E DICIONÁRIO
def build_person(first_name,last_name):
     person = {'first':first_name, 'last': last_name}
     return person
musico = build_person('jimi','hendrix')
print(musico)

# POSSO COLOCAR VALORES DEFAULT, OPCIONAIS
# POSSO COLOCAR IDADE, PROFISSÃO OU QUALQUER OUTRA INFORMAÇÃO

def build_person(first_name,last_name,age=''):
      person = {'first':first_name, 'last': last_name}
      if age: 
           person['age'] = age 
           return person
musico = build_person('jimi','hendrix',age=27)
print(musico)






















