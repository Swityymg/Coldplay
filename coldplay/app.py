from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',           
        password='ingeswity', 
        database='Examen2'     
    )
    return conn

# CANCIONES
@app.route('/canciones')
def canciones():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('''
        SELECT 
            c.titulo AS Cancion, 
            g.genero AS Genero, 
            a.nombre_album AS Album,
            a.anio AS Anio
        FROM canciones c
        JOIN genero g ON c.PK_genero = g.ID_genero
        JOIN album_cancion ac ON c.ID_canciones = ac.PK_cancion
        JOIN album a ON ac.PK_album = a.ID_album
    ''')
    canciones = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('canciones.html', canciones=canciones)

# MERCANCÍA
@app.route('/merch')
def merch():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('''
        SELECT 
            nombre_mercancia,
            precio,
            producto,
            nombre_album
        FROM vista_mercancia_album_producto
    ''')
    merch = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('merch.html', merch=merch)

# PREMIOS
@app.route('/premios')
def premios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('''
        SELECT 
            nombre_premio,
            categoria,
            anio,
            titulo
        FROM vista_premios_canciones
    ''')
    premios_data = cursor.fetchall()  

    cursor.close()
    conn.close()

    return render_template('premios.html', premios=premios_data)  
