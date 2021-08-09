import math

sair = False
while not sair:
    perg = float(input('Você deseja calcular qual índice de refração?'
                       '\n->Digite 1 para calcular o n1;'
                       '\n->Digite 2 para calcular o n2;'
                       '\n>>>Sua escolha: '))
    theta1 = float(input('Digite o valor do theta1, em graus: '))
    theta2 = float(input('Digite o valor do theta2, em graus: '))
    if theta1 > 0 and theta2 > 0:
        if perg == 1:
            n2 = float(input('Digite o valor do n2: '))
            if n2 > 0:
                n1 = ((math.sin(math.radians(theta2)))/(math.sin(math.radians(theta1))))*n2
                print(f'\nO valor de n1 vale: {n1}')
                sair = True
            else:
                print('Entre apenas com valores válidos!\n')
        elif perg == 2:
            n1 = float(input('Digite o valor do n1: '))
            if n1 > 0:
                n2 = ((math.sin(math.radians(theta1))) / (math.sin(math.radians(theta2)))) * n1
                print(f'\nO valor de n1 vale: {n2}')
                sair = True
            else:
                print('Entre apenas com valores válidos!\n')
        else:
            print('Entre apenas com valores válidos!\n')
    else:
        print('Entre apenas com valores válidos!\n')