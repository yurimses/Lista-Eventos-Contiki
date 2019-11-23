# -*- coding: utf-8 -*-
import random

nos = int(input('Informe número de nós servidores: '))
print('Número de nós na simulação: {}'.format(nos))
tempo = int(input('Informe intervalo de tempo em minutos: '))
print('Intervalo de tempo: {} min'.format(tempo))
arq = open('Eventos.h','w')
arq.write('int numero_Motes='+str(nos)+'\n')
arq.write('int id_nodes_ev['+str(tempo)+']['+str(nos)+']={')
for i in range(tempo):
    array = []
    array = random.sample(range(0,nos), random.randint(0, nos))
    #random.sample(população(intervalo), amostra(intervalo))  
    if 0 in array:
        array.remove(0)
    if 1 in array:
        array.remove(1)
    print('minuto {} / evento nos nós: {} '.format(i, array))
    array=str(array).replace('[','{').replace(']','}')
    arq.write('{},\n'.format(array))
arq.write('}\n')
arq.close()
