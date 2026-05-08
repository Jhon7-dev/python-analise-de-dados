# mudando para letras maiusculas e minusculas em uma string usaando métodos

name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

# esse método title(), ele coloca as primeiras letras maisculas "Ada Lovelace"
# lower() deixa as letras minusculas
# upper() deixa as letras maiusculas

#  concatenando strings

primeiro_nome = 'joão'
segundo_nome = 'victor'
nome_todo = primeiro_nome + " " + segundo_nome
print(nome_todo)
print(nome_todo.title())

message = "olá, " + nome_todo.title() + " ! "
print(message)

# tabulações 

print("linguagens de programação: \nPython\nC++\nC#\nJavaScript")

#  removendo espaços em branco

linguagem_favorita = 'python '
print(linguagem_favorita)
print(linguagem_favorita.rstrip)