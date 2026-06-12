# Calcular e exibir o perímetro de uma circunferência recebendo seu raio. A
# fórmula para o cálculo é C=2* W *r (utilizar M = 3.14).

PI =3.14
r = int(input('Digite o raio da circunferência: '))
def calculo_p(raio):
     c = 2*PI*raio
     return print("A área da circunferência é : {c}")
print(calculo_p(r))