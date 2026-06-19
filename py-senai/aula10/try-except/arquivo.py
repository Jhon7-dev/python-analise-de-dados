try: 
     lista = [1,2,3]
     print(lista[10])
except IndexError as erro:
     print(f"Tipo do erro: {type(erro)}")
     print(f"Mensagem detalhada: {erro}")