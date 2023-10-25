#Lista 5 - Exercício 4

import math
def p1 (x, y):
    p = math.pow(x - y, 2)
    return p
def p2 (x, y):
    p = math.pow(x - y, 2)
    return p
def dist (x, y):
    d = math.sqrt(x + y)
    return d

x1 = int(input('Insira a coordenada do Ponto 1 no eixo X: '))
y1 = int(input('Insira a coordenada do Ponto 1 no eixo Y: '))
x2 = int(input('Insira a coordenada do Ponto 2 no eixo X: '))
y2 = int(input('Insira a coordenada do Ponto 2 no eixo Y: '))

D = dist(p1(x1, x2), p2(y1, y2))

print(f'A distância entre os pontos informados no plano cartesiano é de {D:.2f}.')
