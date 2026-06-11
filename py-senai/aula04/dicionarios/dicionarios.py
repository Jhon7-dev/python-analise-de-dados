# album={'nome':'pra ver o sol brilhar','artista':'Belo','lançamento':2008}
# print(type(album))
# print(album)
# print(album['nome'].title())
# print(album['artista'].title())
# print(album['lançamento'])
# album_1={'nome':'desafio','artista':'Belo','lançamento':2000}
# print(album_1)
# print(album_1['nome'].title())
# print(album_1['artista'].title())
# print(album_1['lançamento'])
# album_2={'nome':'seu fã','artista':'Belo','lançamento':2004}
# print(album_2)
# print(album_2['nome'].title())
# print(album_2['artista'].title())
# print(album_2['lançamento'])

# elemento = {
#      "nome":"ouro",
#      "símbolo":"Au",
#      "número atômico":79
     
# }
# print(elemento)
# print(elemento["nome"])
# print(elemento["símbolo"])
# print(elemento["número atômico"])
# print(elemento.get("nome"))


# elemento =["nome"] = "prata"
# elemento =['símbolo'] = 'Ag'
# elemento =['número atômico'] = 47
# print(elemento)


# personagem = {
#      "name" : "Jack Dawson",
#      "filme": "Titanic",
#      "ano": "1997"
# }
# personagem_2 = {
#      "name" : "Rose",
#      "filme": "Titanic",
#      "ano": "1997"
# }
# personagem['nacionalidade'] = 'inglês'
# print("Dicionário")
# for key in personagem:
#      print(personagem[key])
# print(personagem)
# print("Dicionário")
# for key in personagem_2:
#      print(personagem_2[key])
# personagem_2['nacionalidade'] = 'inglês'
# print(personagem_2)

# personagem_2.pop('ano')
# print(personagem_2  )
# personagem_2.popitem()
# print(personagem_2  )
# del personagem_2['filme']
# print(personagem_2)
# del personagem_2
# print(personagem_2)
# personagem_3 = dict(nome="chaves",idade=8)
# print(personagem_3)
# personagem_4 = dict(nome="kiko",idade=9,nacionalidade="mexicano",lugar_preferido='Acapulco')
# print(personagem_4)
# personagem_3.update({'nome':'seu madruga'})
# print(personagem_3)
# personagem_3.clear()
# print(personagem_3)
# personagem_4.clear()
# print(personagem_4)

# banda_guns_n_roses = [
#      {'nome' : 'alx rose','função':'vocalista',
#       'nome': 'duff mackgan','função':'baixista',
#       'nome': 'slash','função':'guitarrista',
#       'nome': 'izzy stranlin','função':'guitarrista 2'
#      }
# ]
# for key in banda_guns_n_roses:
#      print(banda_guns_n_roses[key])
# print(banda_guns_n_roses)
# ordenados = sorted(banda_guns_n_roses,key = lambda x: x['tipo'])
# print(ordenados)

autores = ['Aldous Huxley','Geoge Orwell','Ray Bradbury','William Gibson']
livros = ['Brave new world','2009','Fahrenheit 451', 'Neuromancer']
autores_livros = {autor: livro for autor, livro in zip(autores,livros)}
print(autores_livros)

quadrados_pares = {x:x*x for x in range(11) if x % 2 == 0 }
print(quadrados_pares)

filme = {'titulo':'o segredo','genero':'ação'}
copia_filme = filme.copy()
print(copia_filme)
filme['genero'] = 'Fantasia'
print(filme)
print(copia_filme)
copia_filme = dict(filme)
print(copia_filme)
filme['titulo'] = 'velozes e furiosos'
print(filme)
print(copia_filme)