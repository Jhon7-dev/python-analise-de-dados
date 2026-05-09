# PASSANDO UMA LSITA PARA UMA FUNÇÃO
# suponha que tenhamos uma lista de usuarios e queremos exibir uma saudação a cada um. 
# exemplo envia uma lista de nomes a uma função chamda greet_users.py, que sauda cada pessoa da lista individualmente 

def greet_users(names):
     # exibe uma simples saudação a cada usuário da lista
     for name in names:
          msg = 'olá, ' + name.title() + '!'
          print (msg)
usernames = [ 'joao','victor','pedro']
greet_users(usernames)