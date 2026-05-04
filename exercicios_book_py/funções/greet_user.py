def greet_user():
     """exibe uma saudação"""
     print("hello!")
greet_user()


def greet_user(username):# parametro 
     """exibe uma saudação"""
     print("hello, " +  username.title() + " ! ")
greet_user('joao') # aqui é um tipo de ARGUMENTO
# ARGUMENTO é uma informação passsada para uma função em sua chamada