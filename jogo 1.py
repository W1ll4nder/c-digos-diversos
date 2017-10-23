import random

i = int(input('digite o numero de inimigos, de 1 a 10: '))
inimigo = []
selecionado = []
vida = 500
sp = 100
for j in range(1, i + 1):
    inimigo.append([j, 40])
print(inimigo)
while len(inimigo)>0 and vida>0:
        a = int(input('deseja atacar - (1) ou curar - (2)? '))
        selecionado = random.choice(inimigo)
        if a == 1:
            d = random.randint(10, 15)
            print('vc causou {} de dano ao inimigo {} !'.format(d, selecionado))
            selecionado[1] -= d
            for l in range(1, len(inimigo) + 1):
                dano = random.randint(3, 20)
                lista = [1,1,1,0]
                if random.choice(lista)!=0:
                    print('o inimigo {} errou.'.format(l))
                else:
                    print('o inimigo {} causou {} de dano a vc. '.format(l, dano))
                    vida -= dano
            print(vida)
            if selecionado[1]<=0:
                print('inimigo {} morreu '.format(selecionado))
                inimigo.remove(selecionado)
            if sp < 100:
                sp+=3
        elif a == 2:
            print('')
            if sp > 10:
                vida +=10
                sp-=10
                print(vida, sp)
if vida <= 0:
    print('vc perdeu')
else:
    print('vc venceu')


