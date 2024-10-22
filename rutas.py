from flask import Blueprint, request, jsonify
from sistema.sistema import Sistema


rutas = Blueprint('rutas', __name__)

sistema = Sistema()

@rutas.route('/persona', methods=['POST'])
def agregar_persona():
    datos_persona = request.json
    sistema.agregar_persona(datos_persona)
    return jsonify({'mensaje': 'Persona agregada exitosamente'}), 201

@rutas.route('/persona/edad_maxima', methods=['GET'])
def obtener_edad_maxima():
    edad_max = sistema.edad_maxima()
    return jsonify({'edad_maxima': edad_max})

@rutas.route('/persona/edad_minima', methods=['GET'])
def obtener_edad_minima():
    edad_min = sistema.edad_minima()
    return jsonify({'edad_minima': edad_min})

@rutas.route('/persona/edad_promedio', methods=['GET'])
def obtener_edad_promedio():
    edad_prom = sistema.edad_promedio()
    return jsonify({'edad_promedio': edad_prom})

@rutas.route('/persona/monto_promedio', methods=['GET'])
def obtener_monto_promedio():
    monto_prom = sistema.monto_promedio()
    return jsonify({'monto_promedio': monto_prom})

@rutas.route('/persona/monto_maximo', methods=['GET'])
def obtener_monto_maximo():
    monto_max = sistema.monto_maximo()
    return jsonify({'monto_maximo': monto_max})
@rutas.route('/personas', methods=['GET'])
def obtener_personas():
    personas = sistema.obtener_personas_db()
    personas_lista = [
        {
            "nombre": persona.nombre,
            "apellido": persona.apellido,
            "edad": persona.edad,
            "fecha_nacimiento": persona.fecha_nacimiento,
            "dni": persona.dni,
            "profesion": persona.profesion,
            "fecha_declaracion": persona.fecha_declaracion,
            "monto_declarar": persona.monto_declarar,
            "origen_fondos": persona.origen_fondos
        } for persona in personas
    ]
    
    return jsonify(personas_lista), 200
