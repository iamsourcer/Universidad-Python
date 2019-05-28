#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 Escribir una función que reciba una tupla o lista de elementos e indique si
 se encuentran ordenados de menor a mayor o no. '''

secuencia = [1, 14, 23, 19]


def ordenamos(secuencia):
    for i in range(len(secuencia) - 1):
        if secuencia[i] > secuencia[i + 1]:
            return False
    return True


print(ordenamos(secuencia))
