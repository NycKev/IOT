from flask import Flask, render_template, jsonify, request
import mysql.connector
import plotly.graph_objs as go
import plotly.io as pio
from datetime import datetime

app = Flask(__name__)

# 📌 Función para conectar a MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="s_matematicas"
    )

# 📌 Insertar datos de Taylor
@app.route('/insertar_datos', methods=['POST'])
def insertar_datos():
    try:
        datos = request.json["datos"]
        print(f"📥 Datos recibidos en /insertar_datos: {datos}")

        conexion = conectar()
        cursor = conexion.cursor()

        sql = "INSERT INTO coseno (costaylor, cosmath, error, sentaylor, senmath, error_seno) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = [(d["costaylor"], d["cosmath"], d["error"], d["sentaylor"], d["senmath"], d["error_seno"]) for d in datos]

        cursor.executemany(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Datos de Taylor insertados correctamente"}), 200

    except Exception as e:
        print(f"❌ ERROR en /insertar_datos: {str(e)}")
        return jsonify({"error": str(e)}), 500

# 📌 Insertar datos de Fibonacci
@app.route('/insertar_fibonacci', methods=['POST'])
def insertar_fibonacci():
    try:
        datos = request.json["datos"]
        print(f"📥 Datos recibidos en /insertar_fibonacci: {datos}")

        conexion = conectar()
        cursor = conexion.cursor()

        sql = "INSERT INTO fibonacci (posicion, valor, error) VALUES (%s, %s, %s)"
        valores = [(d["posicion"], d["valor"], d["error"]) for d in datos]

        cursor.executemany(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Datos de Fibonacci insertados correctamente"}), 200

    except Exception as e:
        print(f"❌ ERROR en /insertar_fibonacci: {str(e)}")
        return jsonify({"error": str(e)}), 500

# 📌 Obtener datos de Taylor
@app.route('/datos_taylor', methods=['GET'])
def datos_taylor():
    conexion = conectar()
    cursor = conexion.cursor()

    sql_taylor = "SELECT * FROM (SELECT * FROM coseno ORDER BY nres DESC LIMIT 500) sub ORDER BY nres ASC"
    cursor.execute(sql_taylor)
    resultados_taylor = cursor.fetchall()

    cursor.close()
    conexion.close()

    fig = go.Figure()

    if resultados_taylor:
        nres, costaylor, _, error, sentaylor, _, _ = zip(*resultados_taylor)

        fig.add_trace(go.Scatter(x=nres, y=costaylor, mode='lines', name='Coseno (Taylor)', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=nres, y=sentaylor, mode='lines', name='Seno (Taylor)', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=nres, y=error, mode='lines', name='Error', line=dict(color='purple', dash='dash')))

    fig.update_layout(title=f'Gráfico de Taylor - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    return jsonify(pio.to_json(fig))

# 📌 Obtener datos de Fibonacci (CORREGIDO)
@app.route('/datos_fibonacci', methods=['GET'])
def datos_fibonacci():
    conexion = conectar()
    cursor = conexion.cursor()

    sql_fibonacci = "SELECT * FROM (SELECT * FROM fibonacci ORDER BY nres DESC LIMIT 100) sub ORDER BY nres ASC"
    cursor.execute(sql_fibonacci)
    resultados_fibonacci = cursor.fetchall()

    cursor.close()
    conexion.close()

    fig = go.Figure()

    if resultados_fibonacci:
        nres_fibo, posicion, valores, _ = zip(*resultados_fibonacci)

        # 📌 🔥 CORRECCIÓN: Calcular la razón entre términos consecutivos (Φ = 1.618)
        razones = [valores[i] / valores[i-1] if valores[i-1] != 0 else 0 for i in range(1, len(valores))]

        # 📌 🔥 GRAFICAR LOS VALORES DE FIBONACCI
        fig.add_trace(go.Scatter(
            x=posicion, 
            y=valores, 
            mode='lines+markers', 
            name='Fibonacci', 
            line=dict(color='blue')
        ))

        # 📌 🔥 GRAFICAR LAS RAZONES ENTRE TÉRMINOS CONSECUTIVOS
        fig.add_trace(go.Scatter(
            x=posicion[1:], 
            y=razones, 
            mode='lines+markers', 
            name='Razón Fibonacci (Φ)', 
            line=dict(color='magenta')
        ))

        # 📌 🔥 AGREGAR LÍNEA DE REFERENCIA EN Φ (1.618)
        fig.add_trace(go.Scatter(
            x=posicion, 
            y=[1.618] * len(posicion), 
            mode='lines', 
            name='Límite Teórico (Φ = 1.618)', 
            line=dict(color='black', dash='dash')
        ))

        # 📌 Ajustar la escala del eje Y para visualizar mejor
        fig.update_yaxes(type='linear')

    fig.update_layout(
        title=f'Gráfico de Fibonacci - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        xaxis_title="Índice en la serie",
        yaxis_title="Valor / Razón",
        legend_title="Leyenda"
    )

    return jsonify(pio.to_json(fig))

# 📌 Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
