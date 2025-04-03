"""Todas las fechas serán presentadas como tuplas de tres números enteros positivos (ternas),
en este orden: (año, mes, día). El resultado debe ser un valor booleano, True o False. """

def fecha_es_tupla(fecha):
    es_valida = False
    if(type(fecha) == tuple and len(fecha) == 3):
        if(type(fecha[0]) == int and type(fecha[1]) == int
           and type(fecha[2]) == int):
            es_valida = True
    return es_valida

"""Dado un año perteneciente al rango permitido,
determinar si este es bisiesto.
El resultado debe ser un valor booleano, True o False."""

def bisiesto(año):
    fecha = (año,1,1)
    if (fecha_es_valida(fecha)):
        if (año % 4 == 0):
            return True
        elif (año % 400 == 0) and (año % 100 != 0):
            return True
        else:
            return False
    return False


"""Dada una fecha, determinar si ésta es válida.
El resultado debe ser un valor booleano, True o False."""

def fecha_es_valida(fecha):
    meses_31_dias = [1,3,5,7,8,10,12]
    meses_30_dias = [4,6,9,11]
    es_valida = False
    if(fecha_es_tupla(fecha)):
        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
                                                                                #validamos que cada terna tenga el largo correcto
        if(len(str(año)) == 4 and len(str(mes)) < 3 and len(str(dia)) < 3):
                                                                                #solo fechas despues de esta
            if(fecha >= ((1582,10,15))):
                                                                                #validamos que el dia corresponda al mes correcto y al año correcto en caso de los bisiestos
                if((mes in meses_31_dias and dia < 32) or (mes in meses_30_dias and dia < 31)
                   or (mes == 2 and bisiesto(año) and dia < 30) or (mes == 2 and not(bisiesto(año)) and dia < 29)):
                    es_valida = True
    return es_valida

"""Dada una fecha válida, determinar la fecha del día siguiente.
El resultado debe ser una fecha válida (tupla) de tres números enteros positivos q
ue corresponde a una fecha en el Calendario gregoriano. """

def dia_siguiente(fecha):
    meses_31_dias = [1,3,5,7,8,10,12]
    meses_30_dias = [4,6,9,11]
    if(fecha_es_valida(fecha)):
        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
                                                                                #en caso de ser el ultimo dia del año el dia siguiente va a ser el primero del año siguiente
        if(mes == 12 and dia == 31):
                año += 1
                mes = 1
                dia = 1
                fechaResultado = (año,mes,dia)
                return fechaResultado
                                                                                #en caso de que el dia sea el ultimo de febrero se valida si es bisiesto
        if((mes == 2 and bisiesto(año) and dia == 29) or (mes == 2 and not(bisiesto(año)) and dia == 28)):
            mes += 1
            dia = 1
            fechaResultado = (año,mes,dia)
            return fechaResultado
                                                                                #en caso de que el dia sea el ultimo de cualquier mes excepto febrero y diciembre se le suma uno al mes
                                                                                #y el dia queda en uno
        if((mes != 12 and mes in meses_31_dias and dia == 31) or (mes in meses_30_dias and dia == 30)):
            dia = 1
            mes += 1
            fechaResultado = (año,mes,dia)
            return fechaResultado
                                                                                #en otro caso solo se suma un dia
        if((mes in meses_31_dias and dia < 31) or (mes in meses_30_dias and dia < 30)
           or (mes == 2 and dia < 29 and bisiesto(año)) or
           (mes == 2 and not(bisiesto(año)) and dia < 28)):
            dia += 1
            fechaResultado = (año,mes,dia)
            return fechaResultado    
    else:
        return "FECHA INVALIDA"

"""Dada una fecha válida, determinar
el número de días transcurridos desde el primero de enero de su
año (el número de días transcurridos entre el primero de enero
y el primero de enero, dentro de un mismo año, es 0). El resultado
debe ser un número entero."""

def dia_desde_primero_enero (fecha):
    mes31 = [1,3,5,7,8,10,12]
    mes30 = [4,6,9,11]
    if (fecha_es_valida(fecha)):
        mesActual = 1
        dias = 0
        while mesActual < fecha[1]:
            if mesActual in mes31:
                dias += 31
            elif mesActual in mes30:
                dias += 30
            elif mesActual == 2 and bisiesto(fecha):
                dias += 29
            else:
                dias += 28
            mesActual += 1
        return dias + fecha[2] - 1
    else:    
        print ("Fecha no valida")


"""Dado un año perteneciente al rango permitido,
determinar el día de la semana que le corresponde, con la siguiente
codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles,
4 = jueves, 5 = viernes, 6 = sábado. El resultado debe ser un número
entero, conforme a la codificación indicada."""

def dia_primero_enero (año):
                                                                                #algoritmo usado, congruencia de Zeller
    año -= 1
    dia = 1
    mes = 13
    centuria = año // 100
    año_centuria = año % 100
    resultado = (dia+ (((mes+1)*26)//10) + año_centuria + (año_centuria//4) + (centuria//4) - (2*centuria)) % 7
    resultado -= 1
    if (resultado < 0):
        return 6
    return resultado

"""Dado un año perteneciente al rango permitido,
desplegar en consola el calendario de ese año en formato de 3 secuencias (‘filas’) de 4 meses cada una."""

def imprimir_3x4(año):
    fecha = (año,1,1)
    if(fecha_es_valida(fecha)):                                                 #esta validación del and es en caso de que el año sea 1582, ya que aunque una parte de este año es valido, los primeros 10 meses no lo son
        calendario = cargar_Calendario(año, bisiesto(año), dia_primero_enero(año)+1)
        meses = ["           Enero                          Febrero                        Marzo                          Abril",
                 "           Mayo                           Junio                          Julio                          Agosto",
                 "           Septiembre                     Octubre                        Noviembre                      Diciembre"]
        encabezado = "|  D   L   K   M   J   V   S   |  D   L   K   M   J   V   S   |  D   L   K   M   J   V   S   |  D   L   K   M   J   V   S"
        indice_linea = 0
        indice_bloque = 0
        indicador_mes = 0
        print("Calendario del año", año, "D.C.", "\n")
        while (indice_bloque<3):
            print(meses[indice_bloque])
            print(encabezado)
            posicion_en_linea = 0
            indice_linea = 0
            while (indice_linea < 6):                                           #cada mes tiene como máximo 6 líneas, en caso de que no tenga la quinta o sexta se pone en blanco con espacios
                print(print_Linea_Mes(posicion_en_linea, calendario[indicador_mes]),print_Linea_Mes(posicion_en_linea, calendario[indicador_mes +1 ]),print_Linea_Mes(posicion_en_linea, calendario[indicador_mes +2]),print_Linea_Mes(posicion_en_linea, calendario[indicador_mes+3]))
                posicion_en_linea += 30
                indice_linea += 1
            print("\n")                                                         #salto de línea por cuestiones visuales
            indicador_mes += 4
            indice_bloque += 1
    else:
        print("AÑO INVALIDO")

def cargar_Calendario(año, bisiesto, dia_inicio):
    calendario = ["","","","","","","","","","","",""]                          #inicialización de los campos correspondientes a cada mes
    contador_mes = 1
    while (contador_mes <= 12):
        if(contador_mes == 2):
            if(bisiesto):
                calendario[contador_mes-1] = crear_Mes(dia_inicio,29)
                dia_inicio = calcular_dia_inicio_sgt_mes(dia_inicio,29)
            else:
                calendario[contador_mes-1] = crear_Mes(dia_inicio,28)
                dia_inicio = calcular_dia_inicio_sgt_mes(dia_inicio,28)
        else:
            if (contador_mes in [1, 3, 5, 7, 8, 10, 12]):
                calendario[contador_mes-1] = crear_Mes(dia_inicio,31)
                dia_inicio = calcular_dia_inicio_sgt_mes(dia_inicio,31)
            else:
                calendario[contador_mes-1] = crear_Mes(dia_inicio,30)
                dia_inicio = calcular_dia_inicio_sgt_mes(dia_inicio,30) 
        contador_mes += 1
    return calendario

def calcular_dia_inicio_sgt_mes(dia_inicio, dias):
    while(dias!=0):
        if(dia_inicio==7):
            dia_inicio = 1
        else:
            dia_inicio += 1
        dias-= 1
    return dia_inicio

def crear_Mes(dia_inicio, dias):
    mes = "|  "                                                                 #inicialización del mes, con su encabezado
    dia_actual = 1
    dia_semana = dia_inicio
    if(dia_inicio != 1):                                                        #sino empieza domingo, se debe ubicar en el día de la semana correcto
        mes += ((4*(dia_inicio-1))*" ")                                         #ubicación con espacios en blanco en el día de la semana en que empieza un mes 
    while(dia_actual<= dias):
        mes += str(dia_actual)
        if(dia_semana == 7):                                                    #verificación de que una semana ya ha sido llenada
            if(dia_actual+1<10):
                mes += "  |  "
            else:
                mes += "  | "
            dia_semana = 1
        else:
            if(dia_actual+1<10):
                mes += "   "
            else:
                mes += "  "
            dia_semana += 1
        dia_actual += 1
    return completar_espacios_mes(mes)

def completar_linea(mes, n):
    while(len(mes)<n):
        mes += " "    
    return mes
        
def completar_espacios_mes(mes):
    if(len(mes)>150):                                                           #completar los espacios que faltan de un mes, para que se llene la última semana
        mes = completar_linea(mes,180)
    else:                                                                       #validación en caso de que un mes no completa la 5ta fila, o la 4 si el año es bisiesto y además febrero empieza domingo 
        mes = completar_linea(completar_linea(mes, 150) + "|",180)
    return mes

def print_Linea_Mes(posicion, mes):
    linea = ""
    indice = 0
    while (indice<30):                                                          #30 es el largo de cada fila de un mes
        linea = linea + mes[posicion + indice]
        indice += 1
    return linea


#R7 (fecha_futura)
"""Dada una fecha válida f y un número entero no-negativo n,
determinar la fecha que está n días (naturales) en el futuro.
El resultado debe ser una fecha válida."""

def fecha_futura(fecha,dias):
    if (fecha_es_valida(fecha)):
        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        for diaSgte in range(0,dias):
            fecha = dia_siguiente(fecha)
        return fecha
    else:
        return "Fecha invalida"

"""Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1,
determinar el número de días (naturales) entre las dos fechas. Si f1 = f2,
entonces días_entre(f1, f2) = 0. El resultado debe ser un número entero
no negativo."""

def dias_entre (fecha1, fecha2):
    if(fecha_es_valida(fecha1) and fecha_es_valida(fecha2)):
        añoF1 = fecha1[0]
        añoF2 = fecha2[0]
        dif_años = abs(añoF1 - añoF2)
        cant_dias_en_añoF1 = dia_desde_primero_enero(fecha1)
        cant_dias_en_añoF2 = dia_desde_primero_enero(fecha2)
        res = abs(cant_dias_en_añoF1 - cant_dias_en_añoF2) + 360 * dif_años
        return res
    else:
        return "Fecha invalida"

"""Dada una fecha válida,determinar el día de la semana que
le corresponde, con la siguiente codificación: 0 = domingo,
1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes,
6 = sábado. El resultado debe ser un número entero, conforme a
la codificación indicada."""

def dia_semana(fecha):
    if fecha_es_valida(fecha):
        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        if mes == 1:
            mes = 13
            año -= 1
        elif mes == 2:
            mes = 14
            año -= 1
        centuria = año // 100
        año_centuria = año % 100
        resultado = (dia+ (((mes+1)*26)//10) + año_centuria + (año_centuria//4) + (centuria//4) - (2*centuria)) % 7
        resultado -= 1
        if (resultado < 0):
            resultado = 6
        return resultado
    else:
        return "Fecha invalida"

"""Dada una fecha válida f y un número entero no-negativo n,
determinar la fecha que está n días hábiles en el futuro. El
resultado debe ser una fecha válida que corresponda a un día
hábil. Note que f puede corresponder a la fecha de un día no hábil."""

def semana_santa(año):
    a = año % 19
    b = año // 100
    c = año % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) //3
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 22*l) // 451
    n = h + l - 7*m + 114
    mes = n//31
    dia = 1 + (n % 31)
    return (año, mes, dia)

# Resta dias a una fecha, unicamente valido para restar dias a abril
def viaje_en_el_tiempo(fecha, dias):
    m = fecha[1]
    d = fecha[2]
    for i in range (0,dias):
        if (d == 1):
            m -= 1
            d = 31
        else:
            d -= 1
    return (fecha[0],m,d)

def feriados (año):
    dias_no_habiles = [ (año,1,1), (año,4,11), (año,5,1),
            (año,7,25), (año,8,2), (año,8,15),
            (año,9,15), (año,10,12), (año,12,25),
            viaje_en_el_tiempo(semana_santa(año),2),
            viaje_en_el_tiempo(semana_santa(año),3)]
    dias_no_habiles.sort()
    return dias_no_habiles

def fecha_futura_habil(fecha, dias):
    dias_no_habiles = [ (fecha[0],1,1), (fecha[0],4,11), (fecha[0],5,1),
            (fecha[0],7,25), (fecha[0],8,2), (fecha[0],8,15),
            (fecha[0],9,15), (fecha[0],10,12), (fecha[0],12,25),
            viaje_en_el_tiempo(semana_santa(fecha[0]),2),
            viaje_en_el_tiempo(semana_santa(fecha[0]),3)]
    dias_no_habiles.sort()
    año = fecha[0]
    while dias > 0:
        fecha = dia_siguiente(fecha)
        if (fecha[0] > año):
            dias_no_habiles = feriados(fecha[0])
        if fecha in dias_no_habiles:
            continue
        elif (dia_semana(fecha) == 0) or (dia_semana(fecha) == 6):
            continue
        else:
            dias -= 1    
    return fecha


"""Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1,
determinar el número de días hábiles entre las dos fechas. Si f1 = f2,
entonces días_habiles_entre(f1, f2) = 0. El resultado debe ser un número
entero no negativo."""
def dias_habiles_entre(fecha1,fecha2):
    if fecha_es_valida(fecha1) and fecha_es_valida(fecha2):
        dias_no_habiles = []
        cont = 0;    
        if (fecha1 < fecha2):
            año = fecha1[0]
            dias_no_habiles = feriados(año)
            while fecha1 != fecha2:
                fecha1 = dia_siguiente(fecha1)
                if (fecha1[0] > año):
                    dias_no_habiles = feriados(fecha1[0])
                if fecha1 in dias_no_habiles:
                    continue
                elif (dia_semana(fecha1) == 0) or (dia_semana(fecha1) == 6):
                    continue
                else:
                    cont += 1
        else:
            año = fecha2[0]
            dias_no_habiles = feriados(año)
            while fecha2 != fecha1:
                fecha2 = dia_siguiente(fecha2)
                if (fecha1[0] > año):
                    dias_no_habiles = feriados(fecha1[0])
                if fecha2 in dias_no_habiles:
                    continue
                elif (dia_semana(fecha2) == 0) or (dia_semana(fecha2) == 6):
                    continue
                else:
                    cont += 1
        return cont
    else:
        return "Fecha invalida"
