import index

personas = index.enterData()

promedio_edad = index.edadPromedio(personas)
promedio_monto = index.promedioMonto(personas)
num_personas = len(personas)
edad_minima = index.edadMinima(personas)
edad_maxima = index.edadMaxima(personas)
monto_minimo = min(persona["Monto_declarar"] for persona in personas)
monto_maximo = index.montoMaximo(personas)

print("Promedio de edad:", promedio_edad)
print("Promedio de monto a declarar:", promedio_monto)
print("Total de personas inscriptas:", num_personas)
print("La edad más chica es:", edad_minima)
print("La edad más alta es:", edad_maxima)
print("El monto más bajo a declarar es:", monto_minimo)
print("El monto más alto a declarar es:", monto_maximo)
