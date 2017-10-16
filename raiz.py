print('todo numero elevado ao cubo é igual há soma de uma sequência de números ímpares')
m = int(input('digite um numero inteiro: '))
num = 1
lista = [num]
for n in range(1, m+1):
    cont = True
    if num%2 == 0:
        num+=1
    else:
        print(' ')
    while cont == True:
        if sum(lista) == n**3:
            print('{}**3 = {}'.format(n, lista))
            num +=2
            lista = [num]
            cont = False
        elif sum(lista)<n**3:
            num+=2
            lista.append(num)
        elif sum(lista)>n**3:
            del lista[0]




