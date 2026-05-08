# escreva uma função chamada city_country() que aceite o nome de uma cidade e seu país. tem que voltr formatada assim assim: 
# Santiago, Chile

def city_country(name_city,name_country):
     full_name = name_city + ', ' + name_country
     return full_name.title()
cidade_pais = city_country('santiago','chile')
cidade_pais_2 = city_country('rio de janeiro','brasil')
cidade_pais_3 = city_country('rosário','argentina')
cidade_pais_4 = city_country('montevidéo','uruguay')
print(cidade_pais)
print(cidade_pais_2)
print(cidade_pais_3)
print(cidade_pais_4)