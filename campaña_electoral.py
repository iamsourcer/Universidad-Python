#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
a) Escribir una función que reciba una tupla con nombres, y para cada nombre
imprima el mensaje - Estimado <nombre>, vote por mí. '''

nombres = (('Jonathan', 0),
           ('Pablo', 0),
           ('Martin', 0),
           ('Paula', 1),
           ('Micaela', 1),
           ('Mauricio', 0),
           ('Agustin', 0),
           ('Javier', 0),
           ('Nicolas', 0),
           ('Marcelo', 0),
           ('Hernan', 0))


def voteme(tupla_de_nombres):
    for i in range(len(tupla_de_nombres)):
        if nombres[i][1] == 0:
            print('Estimado {}, vote por mi.'.format(nombres[i][0]))
        else:
            print('Estimada {}, vote por mi.'.format(nombres[i][0]))


# voteme(nombres)


'''

b) Escribir una función que reciba una tupla con nombres, una posición de
origen p y una cantidad n, e imprima el mensaje anterior para los n nombres
que se encuentran a partir de la posición p.

'''


def voteme2(nombres, p, n):
    i = 0
    for nombre in nombres[p:]:
        if nombres[i][1] == 0:
            print('Estimado {}, vote por mi.'.format(nombres[i][0]))
        else:
            print('Estimada {}, vote por mi.'.format(nombres[i][0]))
        i += 1
        if i == n:
            break

voteme2(nombres, 3, 4)

'''
c) Modificar las funciones anteriores para que tengan en cuenta el género del
destinatario,paraello, deberán recibir una tupla de tuplas, conteniendo el
nombre y el género. '''
