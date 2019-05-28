#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def unidad(nro):
    """
    Retorna la unidad, ej: 123 > 3
    """
    nro = str(nro)
    unidad = nro[-1]

    return int(unidad)


def decena(nro):
    nro = str(nro)
    decena = nro[-2]
    return int(decena)


def unidades(nro, digito):
    """
    Tomo un numero X y retorno el digito solicitado teniendo en cuenta que:
    1 es para la unidad
    10 es para la decena
    100 es para la centena
    1000 es para la unidad de Mil
    """

    nro = str(nro)
    digito = str(digito)
    dic = {'1': -1, '10': -2, '100': -3, '1000': -4}

    if digito not in dic.keys():
        print('ERROR! ingresa un digito que sea  1, 10, 100 o 1000')
        return None
    else:
        unidad = int(nro[dic[digito]])
        return unidad


"""
Funcion que genera N numeros aleatorios y me dice el maximo y el promedio de
uno de sus digitos.
Por ejemplo: 41, 102, 63 y yo imprimo en este caso 6 y el promedio es 3.33
"""


def num_aleatorios(n, min=0, max=1000):
    lista = []
    for numero in n:
        lista.append(random.randint(min, max))
    return lista


def lista_digitos(lista_numeros, digito):
    # toma una lista de numeros y retorna una de digitos
    # ver funcion map()
    lista_digitos = []
    for numero in lista_numeros:
        lista_digitos.append(unidades(numero, digito))
    return lista_digitos


def num_max_average(lista_digitos):
    max = 0
    suma = 0
    for num in lista_digitos:
        suma += num
        if num > max:
            max = num
    return max, suma//len(lista_digitos)


n = range(random.randint(1, 10))
lista_numeros = num_aleatorios(n, min=10)
lista_digitos = lista_digitos(lista_numeros, 10)

print(num_max_average(lista_digitos))
