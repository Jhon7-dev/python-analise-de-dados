# Fatiando uma lista
# especifique o índice do primeiro e do último elemento com os quais você quer trabalhar
# para exibir os três primeiros elementos de uma lista, solicite os índices de 0 a 3;
# os elementos 0, 1 e 2 serão desenvolvidos

jogadores = ['arrascaeta','zico','rossi','gabi','cr7']
print(jogadores[0:3])

#  subconjunto de umalista. Por exemplo, se quiser o segundo, terceiro e o quarto item de uma lista, comece a fatia no índice 1 e termine no 4 
jogadores = ['arrascaeta','zico','rossi','gabi','cr7']
print(jogadores[1:4])
# ['zico', 'rossi', 'gabi']

# OBS: se o primeiro índice for omitido , a fatia vai começar do ínicio]
jogadores = ['arrascaeta','zico','rossi','gabi','cr7']
print(jogadores[:4])

# se eu quiser uma fatia que inclua o final de uma lista. posso começar com o índice 2 e omitir o segundo índice
jogadores = ['arrascaeta','zico','rossi','gabi','cr7']
print(jogadores[2:])

# percorrendo uma fatia com um laço
jogadores = ['arrascaeta','zico','rossi','gabi','cr7']
print('aqui estão os jogadores do meu time:')
for jogador in jogadores:
     print(jogador.title())
