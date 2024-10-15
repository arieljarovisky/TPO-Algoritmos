

from sistema.sistema import Sistema 

sistema = Sistema()

sistema.ingresar_datos()

print("Edad máxima:", sistema.edad_maxima())
print("Edad mínima:", sistema.edad_minima())
print("Promedio de edad:", sistema.edad_promedio())
print("Promedio de monto a declarar:", sistema.monto_promedio())
print("Monto máximo a declarar:", sistema.monto_maximo())
