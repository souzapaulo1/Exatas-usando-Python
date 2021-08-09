import math

e = float(input('Digite o valor da espessura da lâmina: '))
i = math.radians(float(input('Digite o valor do ângulo de incidência, em graus: ')))
r = math.radians(float(input('Digite o valor do ângulo de refração, em graus: ')))

if e > 0 and i > 0 and r > 0:
    d = e * (math.sin(i-r)/math.cos(r))
    print(f'O valor do desvio d vale: {d}')
else:
    print('Entre apenas com valores válidos!')