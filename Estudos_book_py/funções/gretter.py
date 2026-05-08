# usando laço WHILE
def build_person(first_name,last_name):
     full_name =  first_name + '  ' + last_name
     return full_name.title()

while True:
     print("\ninsira o seu nome ")
     f_name = input('Primeiro nome: ')
     l_name = input('Último nome: ')
     
     formatted_name = build_person(f_name, l_name)
     print("\nOi , " + formatted_name + " !")
     
     