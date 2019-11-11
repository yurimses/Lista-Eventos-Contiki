# -*- coding: utf-8 -*-
import random


nos = int(input('Informe número de nós servidores: '))
print('Número de nós na simulação: {}'.format(nos))
tempo = int(input('Informe intervalo de tempo em minutos: '))
print('Intervalo de tempo: {} min'.format(tempo))
arq = open('Eventos.txt','w')
for i in range(tempo):
    array = []
    array = random.sample(range(0,nos), random.randint(0, nos))
    #random.sample(população(intervalo), amostra(intervalo))  
    if 0 in array:
        array.remove(0)
    if 1 in array:
        array.remove(1)
    print('minuto {} / evento nos nós: {} '.format(i, array))
    arq.write('{}\n'.format(array))
arq.close()
'''
Tem algum minuto que não ocorre evento? (como interagir listas vazias com C?)
'''
