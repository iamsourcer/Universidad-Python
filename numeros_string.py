#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escribir una función que reciba una cadena que contiene un largo número
entero y devuelva una cadena con el número y las separaciones de miles.
Por ejemplo, si recibe ’1234567890’, debe devolver ’1.234.567.890’.
"""


def separaciones_miles(numero):
    # assert numero.isdigit(), 'Pifiador SOLO DIGITOS'
    if not numero.isdigit():
        print('NO ingresaste un numero')
        return None

    cantidad_puntos = len(numero) // 3
    if len(numero) % 3 == 0:
        cantidad_puntos -= 1

    lnumero = list(numero)
    indice = -3
    for punto in range(cantidad_puntos):
        lnumero.insert(indice, '.')
        indice -= 4
    return ''.join(lnumero)

print(separaciones_miles('100000000000'))
