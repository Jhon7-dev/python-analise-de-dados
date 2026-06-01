# escreva uma função que aceite uma lista de itens que uma pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos itens quantos forem fornecidos pela chamada da função e deve apresentar um resumo do sanduíche pedido
# chame a função três vezes usando o número difeente de argumentos a cada vez

def fazer_sanduba(*ingredientes):
     print('escolhendo os ingredientes para o sanduíche')
     for ingrediente in ingredientes:
             print('- ', ingrediente)
     print('A quantidade de ingredientes para fazer o sanduíche é ', len(ingrediente))
fazer_sanduba('pão','requeijão','queijo','tomate','alface')
fazer_sanduba('pão','manteiga','alface','salame')
fazer_sanduba('pão','manteiga','queijo','salame')

          