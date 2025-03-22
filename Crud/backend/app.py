from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Función para conectarse a la base de datos MySQL
def conectar(vhost, vuser, vpass, vdb):
    try:
        # Se intenta conectar a la base de datos con las credenciales proporcionadas
        conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
        return conn
    except pymysql.MySQLError as e:
        # En caso de error, se imprime el mensaje de error
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ruta para obtener todas las contraseñas guardadas
@app.route("/")
def consulta_general():
    try:
        # Se conecta a la base de datos
        conn = conectar('localhost', 'root', 'root', 'gestor_contrasena')
        if not conn:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'})
        
        cur = conn.cursor()
        # Se realiza la consulta para obtener todos los registros del baúl
        cur.execute("SELECT * FROM baul")
        datos = cur.fetchall()
        data = []

        # Se recorren los datos obtenidos para estructurarlos en formato JSON
        for row in datos:
            dato = {'id_baul': row[0], 'plataforma': row[1], 'usuario': row[2], 'clave': row[3]}
            data.append(dato)

        cur.close()
        conn.close()
        return jsonify({'baul': data, 'mensaje': 'Baúl de contraseñas'})
    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error al obtener los datos'})

# Ruta para obtener una contraseña específica según su ID
@app.route("/consulta_individual/<codigo>", methods=['GET'])
def consulta_individual(codigo):
    try:
        conn = conectar('localhost', 'root', 'root', 'gestor_contrasena')
        if not conn:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'})
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM baul WHERE id_baul=%s", (codigo,))
        datos = cur.fetchone()

        cur.close()
        conn.close()

        if datos:
            # Se estructura la respuesta con los datos obtenidos
            dato = {'id_baul': datos[0], 'plataforma': datos[1], 'usuario': datos[2], 'clave': datos[3]}
            return jsonify({'baul': dato})
        else:
            return jsonify({'mensaje': 'Registro no encontrado'})
    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error en la consulta'})

# Ruta para agregar un nuevo registro de contraseña
@app.route("/registro/", methods=['POST'])
def registro():
    try:
        conn = conectar('localhost', 'root', 'root', 'gestor_contrasena')  
        if not conn:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'})
        
        cur = conn.cursor()
        # Se insertan los datos en la base de datos
        cur.execute("""
            INSERT INTO baul (plataforma, usuario, clave)
            VALUES (%s, %s, %s)
        """, (request.json['plataforma'], request.json['usuario'], request.json['clave']))
        
        conn.commit()  # Confirmar la inserción de la información
        cur.close()
        conn.close()

        return jsonify({'mensaje': 'Registro agregado exitosamente'})
    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error al agregar el registro'})

# Ruta para eliminar un registro de contraseña
@app.route("/eliminar/<codigo>", methods=['DELETE'])
def eliminar(codigo):
    try:
        conn = conectar('localhost', 'root', 'root', 'gestor_contrasena') 
        if not conn:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'})
        
        cur = conn.cursor()
        cur.execute("DELETE FROM baul WHERE id_baul=%s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'mensaje': 'Registro eliminado exitosamente'})
    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error al eliminar el registro'})

# Ruta para actualizar un registro existente
@app.route("/actualizar/<codigo>", methods=['PUT'])
def actualizar(codigo):
    try:
        conn = conectar('localhost', 'root', 'root', 'gestor_contrasena')
        if not conn:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'})
        
        cur = conn.cursor()
        cur.execute("""
            UPDATE baul
            SET plataforma=%(plataforma)s, usuario=%(usuario)s, clave=%(clave)s
            WHERE id_baul=%(id_baul)s
        """, {
            'plataforma': request.json['plataforma'],
            'usuario': request.json['usuario'],
            'clave': request.json['clave'],
            'id_baul': codigo
        })

        conn.commit()  # Confirmar los cambios
        cur.close()
        conn.close()

        return jsonify({'mensaje': 'Registro actualizado exitosamente'})
    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error al actualizar el registro'})

if __name__ == '__main__':
    app.run(debug=True)
