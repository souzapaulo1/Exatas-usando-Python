
x_fake = float(input('Digite o valor da posição da imagem: '))
n_obs = float(input('Digite o valor do índice de refração onde o observador está: '))
n_obj = float(input('Digite o valor do índice de refração onde o objeto está: '))

if x_fake > 0 and n_obs > 0 and n_obj > 0:
    x = (n_obj / n_obs) * x_fake
    print(f'O valor da posição real do objeto é: {x}')
else:
    print('Entre apenas com valores válidos!')