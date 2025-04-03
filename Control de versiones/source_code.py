class Month:
    month_names = {1: 'Enero', 2: 'Febrero', 3: 'Marzo',
                   4: 'Abril', 5: 'Mayo', 6: 'Junio',
                   7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
                   10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    week = ['D', 'L', 'K', 'M', 'J', 'V', 'S']
    avaible_days = {2: 'L', 3: 'K', 4: 'M', 5: 'J', 6: 'V'}
    public_holidays= [(1,1),(4,11),(5,1),(7,25),(8,2),(8,15),(9,15),(10,12),(12,25)]

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.name = self.month_names.get(month, "Invalid")
        self.position = dia_semana((year, month, 1))
        self.length = month_length(year, month)
        self.day = 1


# Desc: True si entero positivo.
def is_positive_integer(number):
    if isinstance(number, int):
        if number > 0:
            return True
        else:
            print(f"Input_Error: <{number}> no es entero positivo.")
    else:
        print(f"Input_Error: <{number}> detectado como {type(number)}")
    return False


# Desc: True si año entre rango [1582..]
def is_year(year):
    if is_positive_integer(year):
        if 1581 < year:
            return True
        else:
            print(f"Input_Error: <{year}> fuera de rango [1582..]")
    return False


# Desc: True si mes entre rango [1..12]
def is_month(month):
    if is_positive_integer(month):
        if month < 13:
            return True
        else:
            print(f"Input_Error: <{month}> fuera de rango [1..12]")
    return False


# Desc: True si dia entre rango [1..31]
def is_day(day):
    if is_positive_integer(day):
        if day < 32:
            return True
        else:
            print(f"Input_Error: <{day}> fuera de rango [1..31]")
    return False


# Desc: Devuelve cantidad de dias en un mes de un año.
def month_length(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if bisiesto(year):
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    return month_length


# Desc: Devuelve una fecha de la forma 'aaaa-mm-dd' para poder ser comparada con otra fecha
# entradas: fecha = (int, int, int)
# salidas: fecha = string
# restricciones: ninguna
def toJulianDate(fecha):
    return str(fecha[0]) + "-" + str(fecha[1]).zfill(2) + "-" + str(fecha[2]).zfill(2)


# Desc: Devuelve el (mes, dia) del jueves y viernes santo de un año dado.
# Se utilizar el algoritmo de Butcher para calcular el domingo de pascua,
# al que se le restan los dias para obtener el jueves y el viernes.
# la formula aplicada se encuentra aqui:
# https://en.wikipedia.org/wiki/Computus
def dias_santos(year):
    viernes = (0,0)
    jueves = (0,0)
    if (year == 1582):
        jueves = (4, 12)
        viernes = (4, 13)
        return [jueves, viernes]
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    for x in range(1, 4):
        day -= 1;
        if (day < 1):
            day = 31
            month = 3
        if (x == 2):
            viernes = (month, day)
        if (x == 3):
            jueves = (month, day)
    return [jueves, viernes]


# Desc: Devuelve true si es feriado y False si es un dìa habil
# entradas: fecha = (int, int, int)
# salidas: True/False
# restricciones: ninguna
def dia_feriado(date):
    year = date[0]
    month = date[1]
    day = date[2]
    d=(month,day)
    if (d in Month.public_holidays or d in dias_santos(year)):
        return True
    else:
        return False
    


# Desc: True si fecha es tupla de 3 enteros positivos.
def fecha_es_tupla(date):
    if isinstance(date, tuple) and (len(date) == 3):
        for number in date:
            if not is_positive_integer(number):
                return False
        return True
    else:
        print(f"Input_Error: <{date}> no es tupla terna.")
    return False


# Desc: True si año es bisiesto.
def bisiesto(year):
    if is_year(year):
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            return True
    return False


# Desc: True si dia en el rango de dias del mes.
def fecha_es_valida(date):
    if fecha_es_tupla(date):
        year = date[0]
        month = date[1]
        day = date[2]
        if is_year(year) and is_month(month) and is_day(day):
            days_in_month = month_length(year, month)
            if year == 1582 and month == 10 and 4 < day < 15:
                print(f"Input_Error: El {day} de Octubre de 1582 nunca existio...")
                return False
            if day <= days_in_month:
                return True
            else:
                print(f"Input_Error: El {month} del {year} es de {days_in_month} dias.")
    return False


# Desc: Fecha como tupla del dia siguiente.
def dia_siguiente(date):
    if fecha_es_valida(date):
        year = date[0]
        month = date[1]
        day = date[2]
        days_in_month = month_length(year, month)
        if year == 1582 and month == 10 and day == 4:
            return (year, month, 15)
        if day < days_in_month:
            return (year, month, day + 1)
        elif month == 12:
            return (year + 1, 1, 1)
        else:
            return (year, month + 1, 1)
    return False


# Desc: Cantidad de dias desde el primero de enero del año de una fecha.
def dias_desde_primero_enero(date):
    if fecha_es_valida(date):
        year = date[0]
        month = date[1]
        day = date[2]
        elapsed_days = day
        for elapsed_month in range(1, month):
            elapsed_days += month_length(year, elapsed_month)
        if year == 1582 and ((month == 10 and 4 < day) or 10 < month):
            return elapsed_days - 11
        else:
            return elapsed_days - 1
    return False


# Desc: Dia de la semana de una fecha tupla.
# Se usa la regla de Zeller para determinar los dias de la semana de
# cualquier fecha del calendario gregoriano.
# Notacion de Zeller's Rule tomada de
# http://www.careeranna.com/articles/find-day-for-given-date-quickly/.
# Referirse a la pagina para una explicacion detallada de la formula.
# Solo funciona para fechas del 15/10/1582 en adelante, modificado con
# desfase para las fechas anteriores del 1582 de 10 dias.
def dia_primero_enero(year):
    if is_year(year):
        k = 1
        m = 11
        d = int(str(year - 1)[-2:])
        c = int(str(year - 1)[:2])
        f = k + (13*m - 1)//5 + d + d//4 + c//4 - 2*c
        if year == 1582:
            return (f-11) % 7
        else:
            return f % 7
    return False


# Desc: Imprimir en consola el calendario de un año en filas de 4 columnas.
# Tiene como argumento opcional la cantidad de columnas en el calendario.
# Valor por defecto es 4.
def imprimir_3x4(year, size=4):
    if not is_year(year):
        return False
    if 12 % size == 0:
        calendar = [[Month(year, column + size*row) for column in
                    range(1, size + 1)] for row in range(12 // size)]
    else:
        calendar = [[Month(year, column + size*row) for column in
                    range(1, size + 1) if column + (size*row) < 13] for row in
                    range(12//size + 1)]

    print(f'Calendario del año {year} D.C')
    for row in calendar:
        # Imprime nombre de los meses
        print('|', end='')
        for month in row:
            print(f'{month.name:^22}', end='|')
        # Imprime nombre de los dias
        print('\n', end='|')
        for month in row:
            print(''.join([f'{weekday:>3}' for weekday in month.week]), end=' |')
        print()
        # Imprime dias de la semana, seis semanas por mes.
        week = 1
        while week != 7:
            print('|', end='')
            for month in row:
                print(f'{"":>3}'*month.position, end='')
                while month.position != 7:
                    if month.year == 1582 and month.month == 10 and month.day == 4:
                        print(f'{month.day:>3}', end='')
                        month.day += 11
                    elif month.day <= month.length:
                        print(f'{month.day:>3}', end='')
                        month.day += 1
                    else:
                        print(f'{"":>3}', end='')
                    month.position += 1
                month.position = 0
                print(' |', end='')
            print()
            week += 1
        print()

# Desc: Este programa recibe una tupla de 3 valores, de la forma aaaa-mm-dd y
# un numero n y retorna la fecha en n dias a partir de la fecha dada
# entradas: fecha = (int, int, int),  n = int
# salidas: fecha = (int, int, int)
# restricciones: debe ser una fecha valida, de lo contrario devueve false
def fecha_futura(fecha, n):
    if fecha_es_valida(fecha):
        if n == 0:
            return fecha
        if is_positive_integer(n):
            return fecha_futura(dia_siguiente(fecha), n - 1)
    return False


# Desc: Recibe 2 dechas en forma de tupla (aaaa,mm,dd)
# entradas: fecha = (int, int, int), (int, int, int)
# salidas: fecha = int
# restricciones: fechas deben ser validas sino retorna false.
def dias_entre(fecha1, fecha2):
    if fecha_es_valida(fecha1) and fecha_es_valida(fecha2):
        if toJulianDate(fecha1) < toJulianDate(fecha2):
            i = 0
            while dia_siguiente(fecha1) != fecha2:
                fecha1 = dia_siguiente(fecha1)
                i += 1
            return i + 1
        else:
            if toJulianDate(fecha1) == toJulianDate(fecha2):
                return 0
            else:
                i = 0
                while dia_siguiente(fecha2) != fecha1:
                    fecha2 = dia_siguiente(fecha2)
                    i += 1
                return i + 1
    else:
        return False


# Desc: Dia de la semana de una fecha tupla.
# Se usa la regla de Zeller para determinar los dias de la semana de
# cualquier fecha del calendario gregoriano.
# Notacion de Zeller's Rule tomada de
# http://www.careeranna.com/articles/find-day-for-given-date-quickly/.
# Referirse a la pagina para una explicacion detallada de la formula.
# Solo funciona para fechas del 15/10/1582 en adelante, modificado con
# desfase para las fechas anteriores del 1582 de 10 dias.
def dia_semana(date):
    if fecha_es_valida(date):
        year = date[0]
        month = date[1]
        day = date[2]
        # k = Dia a buscar.
        k = day
        # m = Numero del Mes, para la formula empieza desde marzo = 1
        if month == 1:
            m = 11
        elif month == 2:
            m = 12
        else:
            m = month - 2
        # d = Ultimos 2 digitos del año,
        # Enero y Febrero cuentan para el año pasado
        if m == 11 or m == 12:
            d = int(str(year - 1)[-2:])
        else:
            d = int(str(year)[-2:])
        # C = Primeros dos digitos del siglo
        if m == 11 or m == 12:
            c = int(str(year - 1)[:2])
        else:
            c = int(str(year)[:2])
        # F = Formula
        f = k + (13*m - 1)//5 + d + d//4 + c//4 - 2*c
        if year == 1582 and ((month == 10 and day < 15) or month < 10):
            return (f-11) % 7
        else:
            return f % 7
    return False


# recibe 1 fecha en forma de tupla (aaaa,mm,dd) y un número de días
# entradas: fecha = (int, int, int), int
# salidas: fecha habil
#
# REVISAR! - FALTA DIAS FERIADOS
def fecha_futura_habil(date, days):
    if fecha_es_valida(date):
        if days == 0:
            return date
        if is_positive_integer(days):
            while days >= 1:
                date = dia_siguiente(date)
                if dia_semana(date) != 0 and dia_semana(date) != 6 and (dia_feriado(date))!=True:
                    days -= 1
        return date


# recibe 2 dechas en forma de tupla (aaaa,mm,dd)
# entradas: fecha = (int, int, int), (int, int, int)
# salidas: Dias habiles = int
# restricciones: fechas deben ser validas sino retorna false.
def dias_habiles_entre(fecha1, fecha2):
    if fecha_es_valida(fecha1) and fecha_es_valida(fecha2):
        if toJulianDate(fecha1) < toJulianDate(fecha2):
            i = 0
            while dia_siguiente(fecha1) != fecha2:
                fecha1 = dia_siguiente(fecha1)
                if dia_semana(fecha1) != 0 and dia_semana(fecha1) != 6 and (dia_feriado(fecha1)) != True:
                    i += 1
            return i + 1
        else:
            if toJulianDate(fecha1) == toJulianDate(fecha2):
                return 0
            else:
                i = 0
                while dia_siguiente(fecha2) != fecha1:
                    fecha2 = dia_siguiente(fecha2)
                    if dia_semana(fecha2) != 0 and dia_semana(fecha2) != 6 and (dia_feriado(fecha2)) != True:
                        i += 1
                return i + 1
    else:
        return False
