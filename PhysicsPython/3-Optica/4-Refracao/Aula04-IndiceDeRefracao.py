print('Entre com o valor da velocidade no meio abaixo em m/s.'
      '\nPode ser escrito "2e8" para duzento milhões, por exemplo.')
v = float(input('\nDigite o valor da velocidade da luz no meio: '))
if v > 0:
      c = 3e8
      n = c/v
      print(f'O valor do índice de refração vale: {n}')
else:
      print('Entre apenas com valores válidos!')