# usando argumentos nomeados arbitrários
# eu quero cirar um perfil de usários mas não sei quanto info vou usar 

def build_profile(first,last,**user_info):
     profile = {}
     profile['first_name'] = first
     profile['last_name'] = last
     
     for key, value in user_info.items():
          profile[key] = value
     return profile
user_profile = build_profile('joao','victor',location='Sorocaba',field='developer')
print(user_profile)
#  a definição da função build_profile() espera um primeiro nome e um sobrenome e permite que o usiário passe tatnos pares nome-valor quantos ele quiser. 
# Os asteriscos duplos antes do parâmetro **USER_INFO fazem python criar um dicionário vazio chamado user_info.
# nessa função, podemos acessar os pares nome-valor recebidos nesse dicionário.