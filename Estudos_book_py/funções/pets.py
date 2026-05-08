# ARGUMENTOS POSICIONAIS

def describe_pet(animal_type, pet_name):
     #  exibe as informações dos animais
     print("\neu tenho um " + animal_type + ".")
     print("meu " + animal_type + " o nome dele é " + pet_name.title() + ".")
describe_pet('pastor alemão','lennon')
# posso chamar mais de uma vez a função
describe_pet('papagaio','loro')

# ARGUMENTOS NOMEADOS
# é um par-valor passado para uma função
# não precisa se preocupar com a ordem correta de seus argumentos na chamada da função e deixam claro  o papel de cada valor na chamada

describe_pet(animal_type='coelho',pet_name='gigante')

#  VALORES DEFAULT 
# podemos definir valores default para cada parâmetro


def describe_pet(pet_name,animal_type='dog'):
           print("\neu tenho um " + animal_type + ".")
           print("meu " + animal_type + " o nome dele é " + pet_name.title() + ".")
describe_pet(pet_name='wallace')
