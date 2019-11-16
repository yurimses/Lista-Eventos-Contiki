# -*- coding: utf-8 -*-
import random

nos = int(input('Informe número de nós servidores: '))
print('Número de nós na simulação: {}'.format(nos))
tempo = int(input('Informe intervalo de tempo em minutos: '))
print('Intervalo de tempo: {} min'.format(tempo))
arq = open('Eventos.txt','w')
for i in range(tempo):
    vetor = []
    vetor = random.sample(range(nos+1), random.randint(0, nos+1))  
    if 0 in vetor:
        vetor.remove(0)
    if 1 in vetor:
        vetor.remove(1)
    print('minuto {} / evento nos nós: {} / {} no total'.format(i+1, vetor, len(vetor)))
    arq.write('{}\n'.format(vetor))
arq.close()
