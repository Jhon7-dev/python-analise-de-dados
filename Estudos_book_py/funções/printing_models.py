# MODIFICANDO UMA LISTA EM UMA FINÇÃO
# QUALQUER ALTERAÇÃO NA LISTA E NO CORPO DA FUNÇÃO É PERMANENTE, PERMITINDO TRABALHAR DE MODO EFICIENTE


#  EXEMPLO UMA EMPRESA QUE CRIA MODELOS DE DESINGS SUBMETIDOS PELO USUÁRIO E QUE SÃO IMPRESSOS EM 3D.
# oS DESIGNS SÃO ARMAZENADOS EM UMA LISTA 
# E, DEPOIS IMPRESSOS,
# SÃO TRANSFERIDOS PARA UMA LISTA SEPARADA

# começa com alguns designs que devem ser impreessos
unprinted_designs = ['iphone case','robor pendant','dodecahedron']
completed_models = []

# simula a impressão de cada design, até que não haja mais nenhum
# transfere cada,'pop()' design para completed_models
# após a impressão

while unprinted_designs:
     current_desing = unprinted_designs.pop()
     
     # simula a criação de uma impressão 3D a partir do design
     print('printando modelo: ' + current_desing)
     completed_models.append(current_desing)
     
# exibe todos os modelos finalizados
print("\nsegue os modelos que estão sendo printados")
for completed_model in completed_models:
     print(completed_model)

#  esse programa começa com uma lsita de designs que devem ser impressos em uma lista vazia chamda completed_models
# para cada design será transferido apóis a impressão.
# enquanto houver designs em unprited_designs, o laço while simulará a impressão de cada um deles removendo um design do final da lista
# armazenando-o em current_desing e exibindo uma mensagem informando que o design atual está sendo impresso.
#  o design então adicioando a lista de modelos finalizados. 
#  quando o laço acava de executar uma lista de designs impressos é exibida
     
