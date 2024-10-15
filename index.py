personas = []


def enterData():
    continuar = int(
        input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")
    )
    while continuar != 0:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        edad = int(input("Ingrese edad: "))
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        dni = int(input("Ingrese DNI: "))
        profesion = input("Ingrese profesión: ")
        fecha_declaracion = input("Ingrese fecha de declaración (DD/MM/AAAA): ")
        monto_declarar = float(input("Ingrese monto a declarar: "))
        origen_fondos = input("Ingrese origen de fondos: ")

        personas.append(
            {
                "Nombre": nombre,
                "Apellido": apellido,
                "Edad": edad,
                "Fecha_nacimiento": fecha_nacimiento,
                "Documento": dni,
                "Profesion": profesion,
                "Fecha_declaracion": fecha_declaracion,
                "Monto_declarar": monto_declarar,
                "Origen_Fondos": origen_fondos,
            }
        )

        continuar = int(input("Para ingresar una nueva persona escriba 1, si no 0: "))
    return personas
    

def edadMaxima(personas):
    edad_maxima = max(persona["Edad"] for persona in personas)
    return edad_maxima

def edadPromedio(personas):    
    num_personas = len(personas)
    total_edad = sum(persona["Edad"] for persona in personas)
    promedio_edad = total_edad / num_personas if num_personas > 0 else 0
    return promedio_edad

def promedioMonto(personas):
    num_personas = len(personas)
    total_monto = sum(persona["Monto_declarar"] for persona in personas)
    promedio_monto = total_monto / num_personas if num_personas > 0 else 0
    return promedio_monto
 
def edadMinima(personas):
    edad_minima = min(persona["Edad"] for persona in personas)
    return edad_minima
   
def montoMaximo(personas):
    monto_maximo = max(persona["Monto_declarar"] for persona in personas)
    return monto_maximo


