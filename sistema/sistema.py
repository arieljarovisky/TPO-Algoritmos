import pymysql
from personas.persona import Persona
import uuid
from datetime import datetime


class Sistema:
    def __init__(self):
        self.personas = []
        self.db_connection = (
            self.connect_db()
        )  # Establecer la conexión a la base de datos

    def connect_db(self):
        try:
            print("Intentando conectar a la base de datos...")
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="26052104",
                database="tpopersonas",
                port=3306,
            )
            print("Conexión exitosa a la base de datos.")
            return connection
        except pymysql.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return None

    def agregar_persona(self):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        edad = int(input("Ingrese edad: "))
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        dni = int(input("Ingrese DNI: "))
        profesion = input("Ingrese profesión: ")
        fecha_declaracion = input("Ingrese fecha de declaración (DD/MM/AAAA): ")
        monto_declarar = float(input("Ingrese monto a declarar: "))
        origen_fondos = input("Ingrese origen de fondos: ")
        nueva_persona = Persona(
            nombre,
            apellido,
            edad,
            fecha_nacimiento,
            dni,
            profesion,
            fecha_declaracion,
            monto_declarar,
            origen_fondos,
        )

        self.insert_persona_db(nueva_persona)

        self.personas.append(nueva_persona)

    def insert_persona_db(self, persona):
        try:
            if not self.db_connection:
                print("No hay conexión a la base de datos.")
                return

            cursor = self.db_connection.cursor()

            fecha_nacimiento = datetime.strptime(
                persona.fecha_nacimiento, "%d/%m/%Y"
            ).date()
            fecha_declaracion = datetime.strptime(
                persona.fecha_declaracion, "%d/%m/%Y"
            ).date()

            persona_id = str(uuid.uuid4())

            query = """
                INSERT INTO persona (ID, nombre, apellido, edad, fecha_nacimiento, dni, profesion, fecha_declaracion, monto_declarar, origen_fondos)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                persona_id,
                persona.nombre,
                persona.apellido,
                persona.edad,
                fecha_nacimiento,
                persona.dni,
                persona.profesion,
                fecha_declaracion,
                persona.monto_declarar,
                persona.origen_fondos,
            )

            cursor.execute(query, values)
            self.db_connection.commit()

            print(
                f"Persona {persona.nombre} {persona.apellido} agregada a la base de datos."
            )
        except pymysql.connect.Error as err:
            print(f"Error al insertar datos: {err}")

    def obtener_personas_db(self):
        if not self.db_connection:
            print("No hay conexión a la base de datos.")
            return []

        cursor = self.db_connection.cursor()
        query = "SELECT nombre, apellido, edad, fecha_nacimiento, dni, profesion, fecha_declaracion, monto_declarar, origen_fondos FROM persona"
        cursor.execute(query)
        result = cursor.fetchall()

        personas = []
        for row in result:
            persona = Persona(*row)
            personas.append(persona)

        return personas

    def ingresar_datos(self):
        print("Ingreso")
        continuar = int(
            input("Si quiere ingresar al sistema apriete el 1, para salir ingrese 0: ")
        )
        while continuar != 0:
            self.agregar_persona()
            continuar = int(
                input("Para ingresar una nueva persona escriba 1, si no 0: ")
            )

    def edad_maxima(self):
        if not self.personas:
            return None
        return max(persona.edad for persona in self.personas)

    def edad_minima(self):
        if not self.personas:
            return None
        return min(persona.edad for persona in self.personas)

    def edad_promedio(self):
        if not self.personas:
            return 0
        total_edad = sum(persona.edad for persona in self.personas)
        return total_edad / len(self.personas)

    def monto_promedio(self):
        if not self.personas:
            return 0
        total_monto = sum(persona.monto_declarar for persona in self.personas)
        return total_monto / len(self.personas)

    def monto_maximo(self):
        if not self.personas:
            return None
        return max(persona.monto_declarar for persona in self.personas)
