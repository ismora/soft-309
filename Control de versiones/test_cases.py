from source_code import (
    fecha_es_tupla,
    bisiesto,
    fecha_es_valida,
    dia_siguiente,
    dias_desde_primero_enero,
    dia_primero_enero,
    imprimir_3x4,
    fecha_futura,
    dias_entre,
    dia_semana,
    fecha_futura_habil,
    dias_habiles_entre,
)


# Cada indice de los arrays FUNCTIONS, INPUTS y RESULTS
# equivalen a la prueba de una funcion.
# Ej: FUNCTIONS[0] es fecha_es_tupla
#     INPUTS[0] es un array con los argumentos a probar
# para fecha_es_tupla
#     RESULTS[0] es un array con los resultados esperados
# de cada argumento de prueba para fecha_es_tupla.
# Si la funcion tiene mas de una entrada, poner los argumentos
# dentro de una lista,
# Ej: fecha_futura ocupa [tupla, int] entonces INPUTS para esa
# funcion es [[tupla1 int1], [tuplaN, intN]]
FUNCTIONS = [
    fecha_es_tupla,
    bisiesto,
    fecha_es_valida,
    dia_siguiente,
    dias_desde_primero_enero,
    dia_primero_enero,
    imprimir_3x4,
    fecha_futura,
    dias_entre,
    dia_semana,
    fecha_futura_habil,
    dias_habiles_entre,
]
INPUTS = [
    ["2018, 12, 31", (2018, 12), (2018.0, 12, 31), (2018, "12", 31), (2018, 12, -31), (2018, 12, 31)],
    [1581, 2018, 2020, 2100, 2000],
    [(2018, 1, 1), (2018, 4, 30), (2018, 4, 31), (1582, 10, 30), (2018, 10, 5), (1582, 10, 5), (2018, 2, 28), (2000, 2, 29), (2018, 2, 29), (2000, 2, 30)],
    [(2018, 1, 30), (2018, 1, 31), (2018, 4, 29), (2018, 4, 30), (2018, 4, 31), (1582, 10, 3), (2018, 10, 4), (1582, 10, 4), (1582, 10, 31), (2018, 2, 27), (2000, 2, 28), (2018, 2, 28), (2000, 2, 29), (2018, 2, 29), (2000, 2, 30), (2018, 12, 30), (1999, 12, 31)],
    [(1582, 12, 31), (2000, 12, 31), (2100, 12, 31)],
    [1582, 2000, 2018, 2100],
    [1582,2000,2018],
    [[(2000,2,27), 3], [(2100,2,27), 2], [(1582,10,4), 4], [(1999,12,30), 3]],
    [[(2000,1,1), (2000,12,31)], [(2100,1,1), (2100,12,31)], [(1582,1,1), (1582,12,31)], [(2000,12,31), (1999,1,1)]],
    [(2000,2,29), (2100,2,28), (1582,10,4), (2000,1,1)],
    [[(2000, 2, 27), 6], [(2018, 4, 10), 1], [(1582, 10, 4), 4], [(1999, 12, 30), 3],[(2000,1,1), 11], [(2100,1,1), 0], [(2000, 4, 24), 24], [(1999,12,30), 5]],
    [[(2000,1,1), (2000,12,31)], [(2100,1,1), (2100,12,31)], [(2000, 4, 24), (2000, 4, 19)], [(1999,12,30), (2000,1,2)]],
]
RESULTS = [
    [False, False, False, False, False, True],
    [False, False, True, False, True],
    [True, True, False, True, True, False, True, True, False, False],
    [(2018, 1, 31), (2018, 2, 1), (2018, 4, 30), (2018, 5, 1), False, (1582, 10, 4), (2018, 10, 5), (1582, 10, 15), (1582, 11, 1), (2018, 2, 28), (2000, 2, 29), (2018, 3, 1), (2000, 3, 1), False, False, (2018, 12, 31), (2000, 1, 1)],
    [354, 365, 364],
    [1, 6, 1, 5],
    [None,None,None],
    [(2000, 3, 1), (2100, 3, 1), (1582, 10, 18), (2000, 1, 2)],
    [365, 364, 354, 730],
    [2, 0, 4, 6],
    [(2000, 3, 6), (2018, 4, 12), (1582, 10, 20), (2000, 1, 4),(2000, 1, 17),(2100, 1, 1),(2000, 5, 29),(2000, 1, 6)],
    [251, 255, 1, 2],
]


def test(function, arguments, expected):
    print(f'{function.__name__:_>114}')
    result = [function(*argument) if isinstance(argument, list)
              else function(argument) for argument in arguments]
    print()
    print(f'{"INPUT__ARGUMENTS":35}',
          f'{"EXPECTED_RESULTS":35}',
          f'{"FUNCTION_RESULTS":35}')
    for position in range(len(arguments)):
        print(f'{str(arguments[position]):35}',
              f'{str(expected[position]):35}',
              f'{str(result[position]):35}', end=' ')
        if expected[position] == result[position]:
            print(f'{"PASSED"}')
        else:
            print(f'{"FAILED"}')
    print('▬'*114, end='\n\n')

if __name__ == "__main__":
    for requirement in range(len(FUNCTIONS)):
        test(FUNCTIONS[requirement], INPUTS[requirement], RESULTS[requirement])
