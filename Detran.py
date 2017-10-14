mot = int(input('quantos motoristas cometeram infração: '))
print(' ')
valor_total = []
c=1
contm=1
while mot>0:
    nome = input('nome do condutor {}: '.format(c)).title()
    numc = int(input('digite o numero da carteira: '))
    numm = int(input('digite o numero de multas de {}: '.format(nome)))
    lista = []
    total = []
    d=numm
    while numm>0:
        valorm = int(input('valor da multa {}: '.format(contm)))
        lista.append(valorm)
        numm-=1
        contm+=1
    total.append(sum(lista))
    contm=1
    c+=1
    valor_total.append(sum(lista))
    numm=d
    print('''
    {}:
    carteira de numero {}
    teve {} multas
    valor total de suas multas foi {} reais.'''.format(nome,numc,numm,sum(lista)))
    print(sum(total))
    if sum(total)>sum(lista):
        print('maior')
    else:
        mot-=1
print('a soma das multas de todos condutores é de {}.'.format(sum(valor_total)))
