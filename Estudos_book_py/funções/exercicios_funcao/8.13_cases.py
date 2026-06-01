# perfil do usuário comece com a cópia do user_PROFILE.crie um seu perfil chamado build_profile(, usando seu primeiro nome e sobrenome, além de três outros pares chave-valor que o descrevam

def build_profile(first,last,**user_info):
     profile = {}
     profile['first_name'] = first
     profile['last_name'] = last
     
     for key, value in user_info.items():
          profile[key] = value
     return profile
user_profile = build_profile('joao','victor',location='Sorocaba',field='developer',borned='Rio De Janeiro',work_in='Apple',age='22')
print(user_profile)
