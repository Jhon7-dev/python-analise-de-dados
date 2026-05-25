Exercício 1 — Sistema de Controle de Entregas Logísticas

Uma transportadora deseja automatizar parte do setor logístico.

Cada entrega possui um código e as 3 primeiras letras identificam o tipo de prioridade da entrega.

Categorias:

EXP → Entrega expressa
NOR → Entrega normal
ECO → Entrega econômica

Exemplos:

Entrega urgente → EXP45871
Entrega padrão → NOR98541
Entrega econômica → ECO15478

A empresa deseja criar um sistema que:

identifique automaticamente entregas expressas
envie essas entregas para o setor prioritário
conte quantas entregas prioritárias existem
calcule o percentual de entregas expressas
Seu objetivo
Parte 1

Crie uma função chamada:

def entrega_expressa(codigo):

A função deve:

receber um código de entrega
verificar se ele pertence à categoria EXP
retornar True ou False
Parte 2

Percorra a lista de entregas:

mostre uma mensagem para entregas expressas
informe que elas devem ir para o setor prioritário

Exemplo:

Entrega EXP45871 deve ir para o setor prioritário
Parte 3

Ao final:

mostre o total de entregas
total de entregas expressas
percentual de entregas expressas
Lista de entregas
entregas = [
'EXP45871','NOR78451','ECO99874','EXP11235','NOR44781',
'EXP77412','ECO66321','NOR90871','EXP55129','NOR44125',
'ECO22541','EXP33669','NOR11452','ECO77125','EXP99584',
'NOR22478','EXP66221','ECO44775','NOR55214','EXP99114',
'ECO14552','NOR78954','EXP11125','NOR77885','EXP22411'
]