#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dadas dos cadenas... escribir una funcion que indique si la segunda cadena es
subcadena de la primera
"""


def subcadena1(string1, string2):
    # if string2 in string1:
    #     return True
    # return False
    return string2 in string1  # retorno directamente la condicion


def subcadena2(string1, string2):
    # usar index para simplificar esta version
    for i1 in range(len(string1)):
        if string1[i1] == string2[0]:

            largo2 = len(string2)
            sub1 = string1[i1:i1+largo2]
            print('sub1', sub1)
            if sub1 == string2:
                return True
    return False


def subcadena3(string1, string2):
    for i1 in range(len(string1)):
        if string1[i1] == string2[0]:

            largo2 = len(string2)
            sub1 = string1[i1:i1+largo2]
            print('sub1', sub1)
            if sub1 == string2:
                return True
    return False


def subcadena4(string1, string2):
    for i1 in range(len(string1)):
        if string1[i1] == string2[0]:

            coincide = True
            for i2 in range(len(string2)):
                j = i1 + i2
                if j == len(string1) or string2[i2] != string1[j]:
                    coincide = False
                    break
            if coincide:
                print('la coincidencia arranca en el indice:', i1)
                return True
    return False


print(subcadena('la barca era una barcaza', 'caza'))
