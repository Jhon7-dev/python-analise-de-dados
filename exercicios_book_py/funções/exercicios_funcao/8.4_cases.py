# modifique a função anterior de modo que as camisetas sejam grandes por default, com uma mensagem 'eu amo python'. Crie uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquier tamanho com uma mensagem diferente

def make_shirt(size_shirt ='g',text='eu amo python'):
     print("Camisa de tamanho " + size_shirt.title() + " e texto de estampa " + text.title())
make_shirt()
make_shirt('m','luar,estrelar,sol e mar')
make_shirt(size_shirt='p',text='amo viajar')