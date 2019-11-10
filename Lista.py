# -*- coding: utf-8 -*-
import random


nos = int(input('Informe número de nós servidores: '))
print('Número de nós na simulação: {}'.format(nos))
tempo = int(input('Informe intervalo de tempo em minutos: '))
print('Intervalo de tempo: {} min'.format(tempo))
for i in range(tempo):
    array = []
    array = random.sample(range(0,nos), random.randint(0, nos))
    #random.sample(população(intervalo), amostra(intervalo))  
    if 0 in array:
        array.remove(0)
    if 1 in array:
        array.remove(1)
    print('minuto {} / evento nos nós: {} '.format(i, array))

'''
Falta jogar dados do laço para um arquivo (é necessário criar uma lista para cada iteração?)
Tem algum minuto que não ocorre evento? (como interagir listas vazias com C?)
'''
