frase = 'O python é uma linguagem de programação '\
          'multiparadigma. '\
          'python foi criado por guido van rossum'
print(frase.count('a')) #quantas vezes a palavra 'a' apareceu nas frases
i = 0
while i<len(frase):
     letra_atual = frase[i]
     qtd_vezes_letra_apareceu = frase.count(letra_atual)
     print(letra_atual,qtd_vezes_letra_apareceu)
     i+=1