import functions
from functions import (
    edades,
    documentos,
    profesiones,
    fechas_declaracion,
    montos_declarar,
    origenes_fondos
)

# Devolver los siguientes puntos:
# - Cuantas personas se registraron en el proceso (cant de personas)
# - Cual es la menor edad de una persona registrada (min)
# - Cual es la mayor edad de una persona registrada (max)
# - Cual es la edad promedio de las personas registradas (promedio)
# - Cual es la fecha de declaracion mas lejana (max)
# - Cual es la fecha de declaracion mas cercana (min)
# - Cual es el menor monto a declarar de una persona registrada (min)
# - Cual es el mayor monto a declarar de una persona registrada (max)
# - Cual es el monto promedio a declarar de las personas registradas (promedio)
# - Ranking de profesiones de las personas registradas
# - Ranking de origen de los fondos de las personas registradas

# Precondiciones del Algoritmo:
# - Se pueden registrar las personas entre 18 y 80 años.
#
# - La fecha de declaracion corresponde al mes de octubre del año 2024, por lo tanto obviamos el mes y el año en la fecha.
#   Solo se debe ingresar [Dia].
#
# - Se asume que el origen de los fondos pueden ser las siguientes opciones:
# [Ahorro] [Inversion] [Ingresos] [Alquileres] [Herencia].

personas = functions.enterData()

num_personas = len(documentos)
edad_minima = functions.edadMinima(edades)
edad_maxima = functions.edadMaxima(edades)
promedio_edad = functions.edadPromedio(edades)
fecha_lejana = functions.fechaLejana(fechas_declaracion)
fecha_cercana = functions.fechaCercana(fechas_declaracion)
monto_minimo = functions.montoMinimo(montos_declarar)
monto_maximo = functions.montoMaximo(montos_declarar)  
promedio_monto = functions.promedioMonto(montos_declarar)
ranking_profesiones = functions.rankingProfesiones(profesiones)
ranking_fondos = functions.rankingFondos(origenes_fondos)

print("Total de personas inscriptas:", num_personas)
print("La edad más chica es:", edad_minima)
print("La edad más alta es:", edad_maxima)
print("Promedio de edad:", promedio_edad)
print(f"La fecha de declaracion mas lejana es el {fecha_lejana}/10.")
print(f"La fecha de declaracion mas cercana es el {fecha_cercana}/10.")
print("El monto más bajo a declarar es:", monto_minimo)
print("El monto más alto a declarar es:", monto_maximo)
print("Promedio de monto a declarar:", promedio_monto)
print("El ranking de profesiones es:", functions.mostrarRanking(ranking_profesiones))
print("El origen de los fondos mas frecuente es:", functions.mostrarRanking(ranking_fondos))