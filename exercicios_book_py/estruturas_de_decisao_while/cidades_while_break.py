# 

message = "\n digite o name das cidades que você ja viajou: "
message +="\n digite 'quit' para sair "
while True:
     city = input(message)
     if city == 'quit':
          break
     else:
          print("Eu gostaria de ir " + city.title() + " !")
