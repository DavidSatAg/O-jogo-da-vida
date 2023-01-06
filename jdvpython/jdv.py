import time
from random import randint
import os

m = [[randint(0, 1) for col in range(20)] for lin in range(20)]
cont = 0


def imprimeMatriz(m):
    unicode = ['\U00002B1B', '\U0001F7E9']
    for lin in range(len(m)):
        print(''.join([unicode[e] for e in m[lin]]))


def vizinhos_vivos(m, x, y):
    vivos = 0
    for eixox in range(-1, 2):
        for eixoy in range(-1, 2):
            vizx = x + eixox
            vizy = y + eixoy
            if (eixox != 0 or eixoy != 0) and 0 <= vizx < len(m) and 0 <= vizy < len(m[0]) and m[vizx][vizy] == 1:
                vivos += 1
    return vivos


def atualiza(m):
    nm = [[0 for e in lin] for lin in m]
    for lin in range(len(m)):
        for col in range(len(m[0])):
            vivos = vizinhos_vivos(m, lin, col)
            if m[lin][col] == 1:
                if  1 < vivos < 4:
                    nm[lin][col] = 1
            else:
                if vivos == 3:
                    nm[lin][col] = 1
    return nm


while True:
    os.system('clear')
    imprimeMatriz(m)
    time.sleep(0.3)
    nm = atualiza(m)
    if nm == m:
        print('Equilíbrio estático!')
        print(f'Geração {cont}')
        break
    else:
        m = nm
        cont += 1
