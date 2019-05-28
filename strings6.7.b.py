#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe ’kde’
y ’gnome’ debe devolver ’gnome’
"""


def subcadena0(string1, string2):
    # solo vale comparar chars y no strings
    # char en python no existe es un string de largo 1
    largo = min(len(string1), len(string2))
    for i in range(largo):
        if string1[i] < string2[i]:
            return string1
        elif string2[i] < string1[i]:
            return string2
    if len(string1) < len(string2):
        return string1
    else:
        return string2


print(subcadena0('barcaza', 'burcaza'))


# hacer una version mas simple y sintetica que encuentres
def subcadena4(string1, string2):
    return min(string1, string2)


# print(subcadena4('tarrico', 'notti'))


# modificar alguna de las anteriores para que funcione con una lista de strings
def subcadena5(lista_strings):
    return min(lista_strings)
