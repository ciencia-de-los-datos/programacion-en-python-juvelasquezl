"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    f1 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f1.append(lineas)

    s = [int(row[1]) for row in f1]

    return sum(s)



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from itertools import groupby

    f2 = []
    dict1 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f2.append(lineas)

    l = sorted([row[0] for row in f2])

    for k, g in groupby(l):
       a = (k,len(list(g)))
       dict1.append(a)
    
    return dict1



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    from operator import itemgetter
    from itertools import groupby

    f3 = []
    dict2 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f3.append(lineas)

    l1 = [[row[0], row[1]] for row in f3]

    l1 = sorted(l1, key=itemgetter(0))
    for k, g in groupby(l1, itemgetter(0)):
        lista_g = (list(g))
        b = (k,sum([int(num) for elem in lista_g for num in elem[1]]))
        dict2.append(b)

    return dict2


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    from itertools import groupby

    f4 = []
    dict3 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f4.append(lineas)
    fecha = [row[2] for row in f4]
    mes = [num[5:7] for num in fecha]
    l2 = sorted(mes)

    for k, g in groupby(l2):
        c=(k,len(list(g)))
        dict3.append(c)

    return dict3


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    from operator import itemgetter
    from itertools import groupby

    f5 = []
    dict4 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f5.append(lineas)

    l = [[row[0], row[1]] for row in f5]

    l = sorted(l, key=itemgetter(0))
    for k1, g1 in groupby(l, itemgetter(0)):
        lista_g = (list(g1))
        d= (k1,max([int(num) for elem in lista_g for num in elem[1]]),min([int(num) for elem in lista_g for num in elem[1]]))
        dict4.append(d)
    
    return dict4


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from itertools import groupby
    from operator import itemgetter

    max_min_dict = {}
    with open('data.csv','r') as f:
        for line in f:
            fields = line.split("\t")
            column = fields[4]
            elements = column.split(',')
            values = [int(element.split(':')[1]) for element in elements]
            key_value_pairs = [tuple(element.split(':')) for element in elements]
            for key, value in key_value_pairs:
                value = int(value)
                if key in max_min_dict:
                    max_val, min_val = max_min_dict[key][0], max_min_dict[key][1]
                    max_min_dict[key] = (max(value, max_val), min(value, min_val))
                else:
                    max_min_dict[key] = (value, value)
    max_min_list = [(k, v[1], v[0]) for k, v in max_min_dict.items()]
    max_min_list.sort()

    return max_min_list



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from operator import itemgetter
    from itertools import groupby

    f = []
    dict6 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f.append(lineas)

    l = [[row[1], row[0]] for row in f]

    l = sorted(l, key=itemgetter(0))
    for k, g in groupby(l, itemgetter(0)):
        lista_g = (list(g))
        a1= (int(k),[num for elem in lista_g for num in elem[1]])
        dict6.append(a1)

        
    return dict6


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    from operator import itemgetter
    from itertools import groupby

    f = []
    dict7 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f.append(lineas)

    l = [[row[1], row[0]] for row in f]

    l = sorted(l, key=itemgetter(0))
    for k, g in groupby(l, itemgetter(0)):
        lista_g = (list(g))
        a2=((int(k), sorted(list(set([num for elem in lista_g for num in elem[1]])))))
        dict7.append(a2)

    return dict7


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    count_dict = {}
    with open('data.csv','r') as f:
        for line in f:
            fields = line.split("\t")
            column = fields[4]
            elements = column.split(',')
            key_value_pairs = [tuple(element.split(':')) for element in elements]
            for key, value in key_value_pairs:
                if key in count_dict:
                    count_dict[str(key)] += int(1)
                else:
                    count_dict[str(key)] = int(1)
        
        count_dict_sorted = dict(sorted(count_dict.items()))
    return count_dict_sorted


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    from itertools import groupby
    from operator import itemgetter

    f = []
    dict9 = []
    with open('data.csv', 'r') as file:
        lineas = file.read().splitlines()
        for i in lineas:
            lineas = i.split('\t')
            f.append(lineas)


    l = [[row[0], row[3], row[4]] for row in f]

    for k, g in groupby(l, itemgetter(0,1,2)):
        lista_g = list(g)
        b2=(k[0], len([l1 for l2 in [num.split('\t') for elem in lista_g for num in elem][1] for l1 in l2 if l1 != ","]),len([num.split(',') for elem in lista_g for num in elem][2]))
        dict9.append(b2)

    return dict9

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv','r') as f:
        sum_dict = {}
        for line in f:
            fields = line.split("\t")
            letter = fields[0]
            value = int(fields[1])
            column = fields[3]
            letters = column.split(",")
            for l in letters:
                if l in sum_dict:
                    sum_dict[l] += value
                else:
                    sum_dict[l] = value
    
    return dict(sorted(sum_dict.items()))



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    with open("data.csv", "r") as archivo:
        for linea in archivo:
            fields = linea.split("\t")
            letra = fields[0]
            column = fields[4]
            elements = column.split(',')
            valores = [int(element.split(':')[1]) for element in elements]
            suma = sum(valores)
            if letra not in diccionario:
                diccionario[letra] = 0
            diccionario[letra] += suma
    return dict(sorted(diccionario.items()))
