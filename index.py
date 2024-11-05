nombres = []
apellidos = []
edades = []
fechas_nacimiento = []
documentos = []
profesiones = []
fechas_declaracion = []
montos_declarar = []
origenes_fondos = []


def enterData():
    continuar = int(
        input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")
    )
    while continuar != 0:
        nombres.append(input("Ingrese nombre: "))
        apellidos.append(input("Ingrese apellido: "))
        edades.append(int(input("Ingrese edad: ")))
        fechas_nacimiento.append(input("Ingrese fecha de nacimiento (DD/MM/AAAA): "))
        documentos.append(int(input("Ingrese DNI: ")))
        profesiones.append(input("Ingrese profesión: "))
        fechas_declaracion.append(input("Ingrese fecha de declaración (DD/MM/AAAA): "))
        montos_declarar.append(float(input("Ingrese monto a declarar: ")))
        origenes_fondos.append(input("Ingrese origen de fondos: "))

        continuar = int(input("Para ingresar una nueva persona escriba 1, si no 0: "))


def edadMaxima():
    if not edades:
        return None
    max_edad = edades[0]
    for edad in edades[1:]:
        if edad > max_edad:
            max_edad = edad
    return max_edad


def edadMinima():
    if not edades:
        return None
    min_edad = edades[0]
    for edad in edades[1:]:
        if edad < min_edad:
            min_edad = edad
    return min_edad


def edadPromedio():
    if not edades:
        return 0
    total_edad = 0
    for edad in edades:
        total_edad += edad
    return total_edad / len(edades)


def promedioMonto():
    if not montos_declarar:
        return 0
    total_monto = 0
    for monto in montos_declarar:
        total_monto += monto
    return total_monto / len(montos_declarar)


def montoMaximo():
    if not montos_declarar:
        return None
    max_monto = montos_declarar[0]
    for monto in montos_declarar[1:]:
        if monto > max_monto:
            max_monto = monto
    return max_monto


