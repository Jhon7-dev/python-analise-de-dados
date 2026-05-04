# ingredients para uma pizza: escreve um laço que peça ao usuário para fornecer uma serie de ingredientes para uma pizza até que o valor 'quit' seja fornecido. À medida que cada ingrediente é específicado, apresente uma mensagem informando que você acrescentará mais ingredientes a pizza

mss = "Forneça os ingredintes para a pizza: "

while ingredientes != 'quit':
     print(mss)
     ingredientes = input("adicionando: ")
     print('ingrediente ', ingredientes + ' adicionado')
     if ingredientes == 'quit':
          break
     
print('programa encerrado')