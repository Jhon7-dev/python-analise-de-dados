# valores de retorno 
# uma função pode processar alguns dados e devolver um valor ou um conjunto de valores
#  valor devolvido = valor de retorno
# DEVOLVENDO UM VALOR SIMPLES

def get_formatted_name(primeiro_nome,segundo_nome):
     # devolve um nome compelto mais elegante
     nome_completo = primeiro_nome + ' ' + segundo_nome
     return nome_completo.title()
musico = get_formatted_name('alx','rose')
print(musico)

#  DEIXANDO UM ARGUMENTO OPCIONAL 
# POSSO DEIXAR COMO DEFAULT

def get_formatted_name(first_name,last_name,middle_name=''):
     if middle_name:
          full_name = first_name + ' ' + middle_name + ' ' + last_name
     else:
          full_name = first_name + ' ' + last_name
     return full_name.title()
musico_2 = get_formatted_name('jimi','hendrix')
musico_3 = get_formatted_name('jhon','winston','lennon')
print(musico_2)
print(musico_3)

