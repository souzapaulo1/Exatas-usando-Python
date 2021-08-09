i = float(input('Digite o valor de i, em graus:'))
i_ = float(input("Digite o valor de i', em graus: "))
A = float(input('Digite o valor de A, em graus:'))
if i > 0 and i_ > 0 and A > 0:
    delta = i + i_ - A
    print(f'O valor de delta vale: {delta} graus.')

