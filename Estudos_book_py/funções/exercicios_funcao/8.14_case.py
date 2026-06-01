# escreva uma função que armazene info sobre um carro em um dicionário. A função sempre deve recever o nome de um fabricante e um modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
# chame a função com as informações necessárias e dois outros pares nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma chamada como esta:
# car = make-car('subaru','outback,color='blue',tow_package=True)

def fabrica_carro(marca,modelo,**info_car):
     carro_info = {} # aqui, to criando um, dicionário vazio
     carro_info ['marca_carro'] = marca #adiciono uma chave 'marca_carro' ao dicionário
     carro_info ['modelo_carro'] = modelo
     
     for chave,valor in info_car.items():
          carro_info[chave] = valor
     return carro_info
carro1 = fabrica_carro ('BMW','M3',cor='azul',potencia='440cv',velociadade_max='340km/h',valor='250.000')
carro2 = fabrica_carro ('VOLVO', 'XC 60',cor='preto',potencia='240cv',velociadade_max='220km/h',valor='150.000')
carro3 = fabrica_carro ('MERCEDEZ-BENZ', 'C63',cor='branco',potencia='540cv',velociadade_max='320km/h',valor='420.000')
print(carro1)
print(carro2)
print(carro3)