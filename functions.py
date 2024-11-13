nombres = []
apellidos = []
edades = []
fechas_nacimiento = []
documentos = []
profesiones = []
fechas_declaracion = []
montos_declarar = []
origenes_fondos = []
validacion_fondos =  [ "Ahorro", "Inversion", "Ingresos", "Alquileres","Herencia"]
def enterData():
    continuar = input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")
    
    while continuar not in ('1', '0'):
        print("Entrada inválida. Debe ingresar 1 para continuar o 0 para salir.")
        continuar = input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")

    while continuar == '1':
        """ nombre = input("Ingrese nombre: ")
        while not nombre:
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese nombre: ")
        nombres.append(nombre)

        apellido = input("Ingrese apellido: ")
        while not apellido:
            print("El apellido no puede estar vacío.")
            apellido = input("Ingrese apellido: ")
        apellidos.append(apellido)

        edad = int(input("Ingrese edad: "))
        while not edad or edad is not int:
            print("La edad no es valida.")
            edad = int(input("Ingrese edad: "))
        edades.append(int(edad))

        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        while not fecha_nacimiento:
            print("La fecha de nacimiento no puede estar vacía.")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        fechas_nacimiento.append(fecha_nacimiento)

        documento = input("Ingrese DNI: ")
        while not documento and documento is not int:
            print("El DNI no es valido.")
            documento = input("Ingrese DNI: ")
        documentos.append(int(documento))

        profesion = input("Ingrese profesión: ")
        while not profesion and profesion != "Ahorro":
            print("La profesión no puede estar vacía.")
            profesion = input("Ingrese profesión: ")
        profesiones.append(profesion)

        fecha_declaracion = input("Ingrese fecha de declaración (DD): ")
        while not fecha_declaracion and fecha_declaracion is not int:
            print("La fecha de declaración no es valida.")
            fecha_declaracion = input("Ingrese fecha de declaración (DD): ")
        fechas_declaracion.append(fecha_declaracion)

        monto = input("Ingrese monto a declarar: ")
        while not monto:
            print("El monto no puede estar vacío.")
            monto = input("Ingrese monto a declarar: ")
        montos_declarar.append(float(monto))
         """
        origen_fondo = input("Ingrese origen de fondos (Ahorro, Inversion, Ingresos,Alquileres, Herencia): ")
        while not origen_fondo or origen_fondo not in validacion_fondos:
            print("El origen de fondos no es valido.")
            origen_fondo = input("Ingrese origen de fondos: ")
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


def promedioMonto(montos_declarar):
    if not montos_declarar:
        return 0
    total_monto = 0
    for monto in montos_declarar:
        total_monto += monto
    return total_monto / len(montos_declarar)


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
            # Comparar elementos adyacentes
            if contador[j] < contador[j + 1]:
                # Intercambiar si están en el orden incorrecto
                contador[j], contador[j + 1] = contador[j + 1], contador[j]
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
    return ranking
    


