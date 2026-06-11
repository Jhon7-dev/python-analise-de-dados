n = int(input("Informe o número de termos: "))
a,b= 0,1
count = 0
while count<n:
     print(a)
     c = a + b
     a,b = b,c
     count +=1 
print('numero de termos',len(a))
