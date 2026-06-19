cardapio = ["hamburguer","batata frita","refrigerante","sorvete"]

print("--------------------------------")
print("--- BEM VINDO AO MCFRITAS ---")
print("===== CARDÁPIO ======")

for i in range(len(cardapio)):
     print(f"[{i}]{cardapio[i]}")
print("--------------------------------")

while True:
     try:
          escolha = int(input("\nDigite o número do item desejado: "))
          item_escolhido = cardapio[escolha]
     except ValueError:
          print("Erro: Entrada inválida! por favor, digite um número inteiro.")
     except IndexError:
          print(f"Erro: este item não existe! escolha um número entre 0 e {len(cardapio)-1}.")
     else:
          print(f"ótima escolha! você selecionou: {item_escolhido}".title())
          break
     finally:
          print("Verificando sistema de pedido.....")
print("\n pedido processado, Obrigado pela preferência!")