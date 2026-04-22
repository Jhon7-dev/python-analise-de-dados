# supondo que eu tenho uma lista de magicos e quero percorrer essa lista
# usa-se o FOR
magicos = ['alice','davi','joão']
for magico in magicos:
     print(magico)
     
# na linha do for magico in magicos:
# diz para extrair um nome da list magicos e armazená-lo em magico.
# "para todo magico na lista de magicos, exiba o nome do magico"

# obs: usar uma variável genérica para ser conveniente
# for gato in gatos

magicos = ['alice','davi','joão']
for magico in magicos:
     print(magico.title() + ", esse foi um grande truque!")
     print("eu não posso esperar para ver seu próximo truque, " + magico.title() + ".\n")
print("Obrigado por assitirem ao show!")