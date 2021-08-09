import math


sair = False
while not sair:
    n1 = float(input('Digite o valor do índice de refração de um dos meios: '))
    n2 = float(input('Digite o valor do índice de refração do outro meio: '))
    i = float(input('Digite o valor do ângulo de incidência que você quer disparar, em graus: '))
    if n1 > 0 and n2 > 0:
        if n1 < n2:
            seno = n1/n2
            L = math.degrees(math.asin(seno))
            print(f'>>>O valor do ângulo limite para esse sistema vale: {L}')
            sair = True
        elif n2 < n1:
            seno = n2/n1
            L = math.degrees(math.asin(seno))
            print(f'>>>O valor do ângulo limite para esse sistema vale: {L}')
            sair = True
        elif n1 == n2:
            print('>>>Os índices são iguais. Teoricamente o ângulo vale 90°.')
            sair = True
    else:
        print('>>>Entre com valores válidos!')
if i > 0:
    if i > L:
        print('>>>Ocorrerá Reflexão!')
    elif i == L:
        print('>>>Teoricamente ainda é refração.')
    elif i < L:
        print('>>>Ocorrerá Refração!')