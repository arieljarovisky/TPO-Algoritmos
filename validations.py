validacion_fondos =  ["Ahorro", "Inversion", "Ingresos", "Alquileres", "Herencia"]

def validarNombre():
    nombre = input("Ingrese nombre: ")
    while not nombre or nombre == " ":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre: ")
    return nombre

def validarApellido():
    apellido = input("Ingrese apellido: ")
    while not apellido or apellido == " ":
        print("El apellido no puede estar vacío.")
        apellido = input("Ingrese apellido: ")
    return apellido

def validarEdad():
    while True:
        edad = input("Ingrese edad: ")
        try:
            edad = int(edad)
            if edad < 18 or edad > 80:
                print("La edad es inválida. La persona tiene que tener entre 18 y 80 años.")
            else:
                return edad
        except ValueError:
            print ("La edad es inválida: escribe un numero entero.")

def validarFechaNacimiento():
    while True:
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")

        try:
            dia = int(fecha_nacimiento[0:2])
            mes = int(fecha_nacimiento[3:5])
            año = int(fecha_nacimiento[6:10])

            if fecha_nacimiento[2] == '/' and fecha_nacimiento[5] == '/':
                if año >= 1944 and año <= 2006:
                    if mes == 2:
                        if dia >= 1 and dia <= 28:
                            return fecha_nacimiento
                        else:
                            print("La fecha ingresada es inválida. [Revise el día]")

                    elif mes in [1,3,5,7,8,10,12]:
                        if dia >= 1 and dia <= 31:
                            return fecha_nacimiento
                        else:
                            print("La fecha ingresada es inválida. [Revise el día]")

                    elif mes in [4,6,9,11]:
                        if dia >= 1 and dia <= 30:
                            return fecha_nacimiento
                        else:
                            print("La fecha ingresada es inválida. [Revise el día]")
                    else:
                        print("La fecha ingresada es inválida. [Revise el mes]")
                else:
                    print("La fecha ingresada es inválida. [Revise el año]")
            else:
                print ("El formato de la fecha es inválido. [Ingrese '/']")
        except ValueError:
            print ("La fecha de nacimiento es inválida (DD/MM/AAAA).")

def validarDNI():
    while True:
        documento = input("Ingrese DNI: ")
        try:
            if len(documento) < 7 or len(documento) > 8:
                print("El DNI no es válido. El numero debe tener entre 7 y 8 caracteres.")
            else:
                documento = int(documento)
                return documento
        except ValueError:
            print ("El DNI no es válido: escribe un numero entero sin puntos ni espacios.")

def validarProfesion():
    profesion = input("Ingrese profesión: ")
    while not profesion or profesion == " ":
        print("La profesión no puede estar vacía.")
        profesion = input("Ingrese profesión: ")
    return profesion

def validarFechaDeclaracion():
    while True:
        fecha_declaracion = input("Ingrese fecha de declaración (DD): ")
        try:
            fecha_declaracion = int(fecha_declaracion)
            if fecha_declaracion <= 0 or fecha_declaracion > 31:
                print("La fecha no es válida: ingrese un dia correspondiente al mes de Octubre.")
            else:
                return fecha_declaracion
        except ValueError:
            print ("La fecha no es válida: ingrese un dia correspondiente al mes de Octubre.")

def validarMonto():
    while True:
        monto = input("Ingrese el monto a declarar: $")
        try:
            monto = float(monto)
            if monto <= 0:
                print("El monto no es válido: ingrese un numero mayor a 0.")
            else:
                return monto
        except ValueError:
            print ("El monto no es válido: ingrese un numero.")

def validarOrigenFondos():
    origen_fondo = input("Ingrese el origen de los fondos (Ahorro, Inversion, Ingresos, Alquileres, Herencia): ")
    while not origen_fondo or origen_fondo not in validacion_fondos:
        print("El origen de fondos no es valido.")
        origen_fondo = input("Ingrese el origen de los fondos (Ahorro, Inversion, Ingresos, Alquileres, Herencia): ")
    return origen_fondo