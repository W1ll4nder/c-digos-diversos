'''código que mostra quais numeros são primos de 1 à m'''

m = int(input(' digite um numero inteiro: '))
cont = []
for n in range(2, m+1):
   for i in range(1, n+1):
       if n%i==0:
           cont.append(1)
   if sum(cont) == 2:
       print(n)
   del cont[:]
