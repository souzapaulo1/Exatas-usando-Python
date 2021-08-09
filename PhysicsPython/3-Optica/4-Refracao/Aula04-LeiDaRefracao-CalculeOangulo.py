import math

sair = False
while not sair:
    perg = float(input('Você deseja calcular qual ângulo?'
                       '\n->Digite 1 para calcular o theta1;'
                       '\n->Digite 2 para calcular o theta2;'
                       '\n>>>Sua escolha: '))
    n1 = float(input('Digite o valor de n1: '))
    n2 = float(input('Digite o valor de n21: '))
    if n1 > 0 and n2 > 0:
        if perg == 1:
            theta2 = float(input('Digite o valor de theta2, em graus: '))
            if theta2 > 0:
                theta1 = math.degrees(math.asin((n2/n1)*math.sin(math.radians(theta2))))
                print(f'\nO valor de theta1 vale: {theta1}')
                sair = True
            else:
                print('Entre apenas com valores válidos!\n')
        elif perg == 2:
            theta1 = float(input('Digite o valor de theta1, em graus: '))
            if theta1 > 0:
                theta2 = math.degrees(math.asin((n1/n2)*math.sin(math.radians(theta1))))
                print(f'\nO valor de theta2 vale: {theta2}')
                sair = True
            else:
                print('Entre apenas com valores válidos!\n')
        else:
            print('Entre apenas com valores válidos!\n')
    else:
        print('Entre apenas com valores válidos!\n')