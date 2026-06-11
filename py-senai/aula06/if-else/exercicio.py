from datetime import date

atual = date.today().year

nascimento = int(input("Ano de Nascimento: "))

idade = atual - nascimento

if idade <= 9:
     print("Atleta MIRIM")
elif idade<= 14:
     print("Atleta INFANTIL")
elif idade <= 19:
     print('Atleta JÚNIOR')
elif idade <= 25:
     print("Atleta Sênior")
else:
     print("Atleta MASTER")
print(f'o atleta tem {idade} anos')