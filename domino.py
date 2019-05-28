#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 7.2. Dominó.
a) Escribir una función que indique si dos fichas de dominó encajan o no.
 Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)

b) Escribir una función que indique si dos fichas de dominó encajan o no.
 Las fichas son recibidas enunacadena,porejemplo:3-4 2-5.
 Nota:utilizar la función split de lascadenas.

"""


def encajan(ficha1, ficha2):
    for i in ficha1:
        for j in ficha2:
            if i == j:
                print('Encajan en el valor:', i)
                return True
    return False


# print(encajan((3, 3), (5, 3)))


def encajan2(string1, string2):
    ficha1 = string1.split('-')
    ficha2 = string2.split('-')

    for i in ficha1:
        for j in ficha2:
            if i == j:
                print('Las fichas encajan en:', i)
                return True
    print('Las fichas ingresadas no encajan')
    return False


# print(encajan2('3-4', '3-5'))

def encajan3(string1, string2):
    # agrego la correccion de mauri, llamo a la otra funcion para no repetir
    ficha1 = string1.split('-')
    ficha2 = string2.split('-')
    return encajan(ficha1, ficha2)


encajan3('3-4', '3-5')
