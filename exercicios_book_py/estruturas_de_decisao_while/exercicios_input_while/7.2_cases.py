# pergunte ao usuário quantas pessoas estão no seu grupo para jantar.Se a resposta for maior que 8, exiba uma mensagem dizendo que eles deverão esperar por uma mesa. caso contrário a mesa está pronta
# message = int()
message = input('Quantos convidados está com você? ')
# message = int()
if message == '8':
     print("Podem entrar! temos mesas para 8 convidados disponível! ")
elif message >= '8':
     print("Podem aguardar por gentileza, ainda não temos mesas para essa quantidade de convidados. ")
else:
     print("Podem entrar! temos mesas disponíveis!")