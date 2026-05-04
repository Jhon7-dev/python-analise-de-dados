# escreva uma função chamada make_shirt() que aceita um tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.a função deve exibir a frase que mostre o tam da camiseta e a mensagem estampada. 
# chame a função uma vez usando argumentos posicionais para criar uma camiseta
# chame a função uma segunda vez usando argumentos nomeados

def make_shirt(size_shirt,text):
     print("Camisa de tamanho " + size_shirt.title() + " e texto de estampa " + text.title())
make_shirt('m','luar,estrelar,sol e mar')
make_shirt(size_shirt='p',text='amo viajar')

     