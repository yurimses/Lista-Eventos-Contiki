# -*- coding: utf-8 -*-
import random

nos = int(input('Informe número de nós servidores: '))
tempo = int(input('Informe intervalo de tempo em minutos: '))
arq = open('Coord.txt','w')
for i in range(tempo):
    vetor = []
    for j in range(random.randint(2,nos)):
      vetor2 = []
      for k in range(2):
         vetor2.append(random.uniform(1,100))
      vetor.append(vetor2)
    print('Vetor de coordernadas {}: {}\n'.format(i,vetor))
    arq.write('{}\n'.format(vetor))
arq.close()
