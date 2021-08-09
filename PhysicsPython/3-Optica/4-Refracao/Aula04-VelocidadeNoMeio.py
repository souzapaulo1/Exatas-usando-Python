n = float(input('Digite o valor do índice de refração do meio: '))
if n > 0:
    c = 3e8
    v = c/n
    print(f'O valor da velocidade no meio vale: {v}')
else:
    print('Entre com valores válidos!')