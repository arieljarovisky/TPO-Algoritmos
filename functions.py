import validations

nombres = []
apellidos = []
edades = []
fechas_nacimiento = []
documentos = []
fechas_declaracion = []
montos_declarar = []
origenes_fondos = []
profesiones = []

def enterData():
    continuar = input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")
    
    while continuar not in ('1', '0'):
        print("Entrada inválida. Debe ingresar 1 para continuar o 0 para salir.")
        continuar = input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")

    while continuar == '1':
        nombre = validations.validarNombre()
        nombres.append(nombre)

        apellido = validations.validarApellido()
        apellidos.append(apellido)

        edad = validations.validarEdad()
        edades.append(int(edad))

        fecha_nacimiento = validations.validarFechaNacimiento()
        fechas_nacimiento.append(fecha_nacimiento)

        documento = validations.validarDNI()
        documentos.append(int(documento))

        profesion = validations.validarProfesion()
        profesiones.append(profesion)

        fecha_declaracion = validations.validarFechaDeclaracion()
        fechas_declaracion.append(int(fecha_declaracion))

        monto = validations.validarMonto()
        montos_declarar.append(float(monto)) 

        origen_fondo = validations.validarOrigenFondos()
        origenes_fondos.append(origen_fondo)

        continuar = input("Para ingresar una nueva persona escriba 1, si no 0: ")
        while continuar not in ('1', '0'):
            print("Entrada inválida. Debe ingresar 1 para continuar o 0 para salir.")
            continuar = input("Para ingresar una nueva persona escriba 1, si no 0: ")

def edadMaxima(edades):
    if not edades:
        return None
    max_edad = edades[0]
    for edad in edades[1:]:
        if edad > max_edad:
            max_edad = edad
    return max_edad

def edadMinima(edades):
    if not edades:
        return None
    min_edad = edades[0]
    for edad in edades[1:]:
        if edad < min_edad:
            min_edad = edad
    return min_edad

def edadPromedio(edades):
    if not edades:
        return 0
    total_edad = 0
    for edad in edades:
        total_edad += edad
    return total_edad / len(edades)

def fechaLejana(fechas_declaracion):
    if not fechas_declaracion:
        return None
    fecha_lejana = fechas_declaracion[0]
    for fecha in fechas_declaracion[1:]:
        if fecha < fecha_lejana:            # la fecha mas lejana posible seria el primer dia del mes (01)
            fecha_lejana = fecha
    return fecha_lejana

def fechaCercana(fechas_declaracion):
    if not fechas_declaracion:
        return None
    fecha_cercana = fechas_declaracion[0]
    for fecha in fechas_declaracion[1:]:
        if fecha > fecha_cercana:           # la fecha mas cercana posible seria el ultimo dia del mes (31)
            fecha_cercana = fecha
    return fecha_cercana    

def montoMaximo(montos_declarar):
    if not montos_declarar:
        return None
    max_monto = montos_declarar[0]
    for monto in montos_declarar[1:]:
        if monto > max_monto:
            max_monto = monto
    return max_monto

def montoMinimo(montos_declarar):
    if not montos_declarar:
        return None
    min_monto = montos_declarar[0]
    for monto in montos_declarar[1:]:
        if monto < min_monto:
            min_monto = monto
    return min_monto

def promedioMonto(montos_declarar):
    if not montos_declarar:
        return 0
    total_monto = 0
    for monto in montos_declarar:
        total_monto += monto
    return total_monto / len(montos_declarar)

def contadorProfesiones(lista_profesiones):
    profesionesFiltradas = []
    conteos = []

    for profesion in lista_profesiones:
        profesion_normalizada = profesion.lower()
        if profesion_normalizada in profesionesFiltradas:
            indice = profesionesFiltradas.index(profesion_normalizada)
            conteos[indice] += 1
        else:
            profesionesFiltradas.append(profesion_normalizada)
            conteos.append(1)

    return profesionesFiltradas, conteos

def rankingProfesiones(lista_profesiones):
    profesionesFiltradas, conteos = contadorProfesiones(lista_profesiones)
    n = len(conteos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if conteos[j] < conteos[j + 1]: 
                conteos[j], conteos[j + 1] = conteos[j + 1], conteos[j]
                profesionesFiltradas[j], profesionesFiltradas[j + 1] = profesionesFiltradas[j + 1], profesionesFiltradas[j]

    return profesionesFiltradas

def contadorFondos(origenes_fondos):
    ahorro = 0
    inversion = 0
    ingresos = 0
    alquileres = 0
    herencia = 0
    for origen in origenes_fondos:
        if origen == "Ahorro":
            ahorro += 1
        elif origen == "Inversion":
            inversion += 1
        elif origen == "Ingresos":
            ingresos += 1
        elif origen == "Alquileres":
            alquileres += 1
        elif origen == "Herencia":
            herencia += 1
    return [ahorro, inversion, ingresos, alquileres, herencia]

def rankingFondos(origenes_fondos):
    contador = contadorFondos(origenes_fondos)
    ranking = ["Ahorro", "Inversion", "Ingresos", "Alquileres", "Herencia"]
    n = len(contador)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contador[j] < contador[j + 1]:
                contador[j], contador[j + 1] = contador[j + 1], contador[j]
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
    return ranking

def mostrarRanking(lista_raking):
    ranking = ""
    for puesto in lista_raking:
        i = lista_raking.index(puesto) + 1
        ranking+=(f"{i}° {puesto} ")
    return ranking