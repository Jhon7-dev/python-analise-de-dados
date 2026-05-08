#  Escreva uma função describe_city() que aceite o nome de uma cidade e seu país. A função deve exibir uma frase simples, com 'santiago está localizado no chile'. chame sua função para 3 cidades diferentes em que pelo menos uma delas não esteja no pai´s default

def describe_city(name_city,country_city):
     print('A ' + name_city.title() + ' está localizada no país ' + country_city.title())
describe_city('rio de janeiro','brasil')
describe_city('buenos aires','argentina')
describe_city('miami','estados unidos')
     