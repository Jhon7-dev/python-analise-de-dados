import os
def salvar_na_pasta_dow(nome_arquivo, conteudo):
     
     home = os.path.expanduser("~")
     caminho_dowloads = os.path.join(home,"Downloads", nome_arquivo)
     try:
          with open(caminho_dowloads, 'w',encoding='utf-8') as arquivo:
               arquivo.write(conteudo)
          print(f"Sucesso! o arquivo foi salvo em: {caminho_dowloads}")
     except Exception as e :
          print(f" Ocorreu um erro: {e}")
print("---- gerador de notas rápidas ----")
titulo = input("Digite o nome do arquivo (ex: notas.txt): ")
texto = input("Digite o que vocÊ está pensando: ")

if len(texto)>0:
     salvar_na_pasta_dow(titulo,texto)
else:
     print("Ação cancelada! está vazio.")