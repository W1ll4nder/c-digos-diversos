'''código que mostra quais numeros são primos e quais não são de 1 à m'''

m = int(input(' digite um numero inteiro: '))
cont = []
for n in range(2, m+1):
   #print(n)
   for i in range(1, n+1):
       #print(i)
       if n%i==0:
           cont.append(1)
   if sum(cont) == 2:
       print(n, 'é primo')
   elif sum(cont) > 2:
       print(n, 'não é primo')
   del cont[:]
