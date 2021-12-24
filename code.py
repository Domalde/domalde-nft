import random
from lista_crt import ls

a = int(input())

def imprime_matriz(x,y):
    linha = [0]*a
    matriz = [linha]*a

    for l in range(a):
        linha = []
        for c in range(a):
            b = str(random.choice(ls()))
            crt = b
            linha.append(crt)
        matriz[l] = linha
    
    print("+"+"-"*(2*a+1)+'+')

    for i in range(a):
        for j in range(a):
            if(j == 0):
                print("|",matriz[i][j], end = " ")
            if(j == a-1):
                print(matriz[i][j],"|")
            if(0<j<a-1):
                print(matriz[i][j], end = " ")
    
    print("+"+"-"*(2*a+1)+'+')

imprime_matriz(a,ls())
''
