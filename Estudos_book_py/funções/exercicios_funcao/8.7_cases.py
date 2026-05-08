# escreva uma função chamada make_album() que construa um dicionário descrevendo um album músical. A função deve aceitar o nome de uma artista e o título do álbum e deve devolver um dicionário contendo essas duas informações
# acrescente o parametro que permita armazenar o número de faixas em um album

def make_album(name_group,name_album,number_faixas=''):
     info = {'nome': name_group, 'nome_album':name_album}
     if info:
        info['number_faixas'] = number_faixas
     return info
cantor = make_album('guns n roses ', 'appetite for destruction',number_faixas=9)
cantor_2 = make_album('belo ', 'pra ver o sol brilhar',number_faixas=6)
cantor_3 = make_album('sorriso maroto ', 'por você',number_faixas=12)
print(cantor)
print(cantor_2)
print(cantor_3)