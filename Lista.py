'''
       Lista.py is a generator of events
       Copyright (c) 2019 Yuri M. Ses <your-email@icen.ufpa.br>
       Copyright (c) 2019 Marlon W. Santos <marlon.santos.santos@icen.ufpa.br>


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


# -*- coding: utf-8 -*-
import random

  #Recebe do teclado o número de motes
nos = int(input('Informe número de nós servidores: '))
  #Exibe números de motes digitado
print('Número de nós na simulação: {}'.format(nos))
  #Recebe do teclado quantos eventos vão ocorrer por minutos
tempo = int(input('Informe intervalo de tempo em minutos: '))
  #Exibe o tempo escolhido
print('Intervalo de tempo: {} min'.format(tempo))

  #Cria o arquivo em modo de escrita
arq = open('Eventos.h','w')
  #Escreve no arquivo a variável numero_Motes
arq.write('int numero_Motes='+str(nos)+';\n')
  #Escreve no arquivo a matriz de eventos
arq.write('int id_nodes_ev['+str(tempo)+']['+str(nos)+']={')

	
for i in range(tempo):
     #Cria uma lista vazia
    array = []
    #De forma aleatória, cria lista de diversos tamanhos e
    #insere nessas listas valores aleatórios de zero até o número de motes definido
    #random.sample(população(intervalo), amostra(intervalo))  
    array = random.sample(range(0,nos), random.randint(0, nos))

    #Se houver zeros e um na lista, eles serão removidos
    if 0 in array:
        array.remove(0)
    if 1 in array:
        array.remove(1)

    #O vetor é convertido em String e são substituídos colchetes por chaves
    array=str(array).replace('[','{').replace(']','}')
    #Exibe os vetores gerados
    print('minuto {} / evento nos nós: {} '.format(i, array))
	
    #Se número mote atual não for o último, insere a lista com vírgula no final
    if i<tempo-1:
       arq.write('{},\n'.format(array))
    else:
    #Se for o último, não insere vírgula no fim da lista
       arq.write('{}\n'.format(array))

  #Insere a última chave da matriz
arq.write('};\n')
  #Fecha o arquivo
arq.close()
