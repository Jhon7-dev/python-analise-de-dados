# método strip remove todos os espaços extras no começi e no fim da String

nome = ' Meu Nome é João Victor Gomes De Souza '
print(nome.strip())

# metodo len
# retorna o tamanho da string
print(len(nome))
# método lower
print(nome.lower())
# métor upper
print(nome.upper())
# método swapcase()
# onde está maiúsculo, vira minúsculo
print(nome.swapcase())

print(nome.title())
# o método replace, ele substitui a string que desejarmos por outra string específica 
# primeiro informamos a string a ser substituída 
# segundo a nova string

print(nome.replace("João","Ozimar"))
print(nome.split(" "))

# join retorna a string que resulta da concatenação dos objetos em um interável separados por delimitador

filosofos = ['kant','kierkegaard','Nietzsche','leibniz']
# print(filosofos.title())
print(', '.join(filosofos))
print(' - '.join(filosofos))

list('aeiou')
'|'.join('aeiou')
# print(list)

print("Ra Ra Ja ra Ta".count("Ra"))
print("existencialismo".endswith("ismo"))
print("existencialismo".endswith("exist"))

# metodo find(), pode ser usadi para vermos se uma string contém uma substring

print('Amar, é encontrar a prórpia felicidade na felicidade alheia'.find('Amar'))
print('Amar, é encontrar a prórpia felicidade na felicidade alheia'.find('é'))
print('Amar, é encontrar a prórpia felicidade na felicidade alheia'.find('a'))

print('xyz678'.isalnum())
print('xy#z678'.isalnum())
print(''.isalnum())

print('exemplo'.isalpha())
print('exemplo 2'.isalpha())

print('33'.isdigit())
print('a33z'.isdigit())
print(''.isdigit())

print('nome'.isidentifier())
print('nome2'.isidentifier())
print('2nome'.isidentifier())
print('nome#'.isidentifier())
# print('nome')