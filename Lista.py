# -*- coding: utf-8 -*-
import random


nos = int(input('Informe número de nós servidores: '))
print('Número de nós na simulação: {}'.format(nos))
#nos: determinar o número de nós servidores que estão sendo executados no Cooja 
tempo = int(input('Informe intervalo de tempo em minutos: '))
print('Intervalo de tempo: {} min'.format(tempo))
#tempo: determinar intervalo de tempo de ocorrência de eventos na simulação
arq = open('Eventos.txt','w')
for i in range(tempo):
    array = []
    array = random.sample(range(0,nos), random.randint(0, nos))
    if 0 in array:
        array.remove(0)
    if 1 in array:
        array.remove(1)
    print('minuto {} / evento nos nós: {} '.format(i, array))
    arq.write('{}\n'.format(array))
arq.close()

'''
array: utilizando estratégia de população e amostra
1º argumento: intervalo da população e 2º argumento: amostra, responsável por determinar o tamanho de array (número de índices)
random.sample(população(intervalo), amostra(intervalo))
linhas 15 a 18: responsáveis por eliminar os numeros 0 e 1 (border router) dos vetores 
'''