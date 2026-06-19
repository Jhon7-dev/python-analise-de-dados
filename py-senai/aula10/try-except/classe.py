class SaldoInsulficienteError(Exception):
     "execeção lançada quando um sque excede o saldo da conta."
     
     pass 
def sacar(valor,saldo):
     if valor > saldo:
          raise SaldoInsulficienteError(f'Tentativa de sacar R${valor} com saldo R${saldo}')
try:
     sacar(1000,500)
except SaldoInsulficienteError as e:
     print(e)