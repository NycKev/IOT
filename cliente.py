import requests
from tkinter import *
from tkinter import messagebox
import math

# ✅ Direcciones del servidor Flask
FLASK_TAYLOR_SERVER = "http://192.168.0.10:5000/insertar_datos"
FLASK_FIBONACCI_SERVER = "http://192.168.0.10:5000/insertar_fibonacci"

# ✅ Función para calcular coseno y seno con Taylor
def aproximacion_cos_taylor(x, num_terminos):
    cos_taylor = 0
    for n in range(num_terminos):
        termino = ((-1) ** n * x ** (2 * n)) / math.factorial(2 * n)
        cos_taylor += termino
    return cos_taylor

def aproximacion_sen_taylor(x, num_terminos):
    sen_taylor = 0
    for n in range(num_terminos):
        termino = ((-1) ** n * x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sen_taylor += termino
    return sen_taylor

# ✅ Función para enviar datos de Taylor
def enviar_datos_taylor():
    try:
        x_max = int(entry_x.get())  # Grados máximos
        num_terminos = int(entry_terminos.get())  # Términos en la serie

        datos = []

        for xxx in range(0, x_max + 1):
            x_rad = math.radians(xxx)

            costaylor = aproximacion_cos_taylor(x_rad, num_terminos)
            cosmath = math.cos(x_rad)
            error = abs(costaylor - cosmath)

            sentaylor = aproximacion_sen_taylor(x_rad, num_terminos)
            senmath = math.sin(x_rad)
            error_seno = abs(sentaylor - senmath)

            datos.append({
                "costaylor": costaylor,
                "cosmath": cosmath,
                "error": error,
                "sentaylor": sentaylor,
                "senmath": senmath,
                "error_seno": error_seno
            })

        response = requests.post(FLASK_TAYLOR_SERVER, json={"datos": datos})

        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Datos de Taylor enviados correctamente.")
        else:
            messagebox.showerror("Error", "Error en el servidor Flask para Taylor.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ✅ Función para calcular Fibonacci
def calcular_fibonacci(n, start_at):
    fibonacci_series = [0, 1]
    for _ in range(2, n):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[start_at:]

# ✅ Función para enviar datos de Fibonacci
def enviar_datos_fibonacci():
    try:
        n_max = int(entry_fibonacci.get())
        start_at = int(entry_start.get())

        if n_max <= 0 or start_at < 0:
            messagebox.showerror("Error", "Los valores deben ser positivos")
            return

        serie_fibonacci = calcular_fibonacci(n_max, start_at)

        text_area_fibonacci.delete("1.0", END)
        text_area_fibonacci.insert(END, "\n".join(map(str, serie_fibonacci)))

        datos = [{"posicion": i + start_at, "valor": serie_fibonacci[i], "error": 0} for i in range(len(serie_fibonacci))]

        response = requests.post(FLASK_FIBONACCI_SERVER, json={"datos": datos})

        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Serie de Fibonacci enviada correctamente.")
        else:
            messagebox.showerror("Error", "Error en el servidor Flask para Fibonacci.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ✅ Crear la interfaz en Tkinter
root = Tk()
root.title("Calculadora de Taylor y Fibonacci")
root.geometry("400x500")

# 📌 Sección de Taylor
Label(root, text="Generar valores de 0 a X grados (Taylor)").grid(row=0, column=0, padx=10, pady=5)
entry_x = Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="N° de términos en Taylor").grid(row=1, column=0, padx=10, pady=5)
entry_terminos = Entry(root)
entry_terminos.grid(row=1, column=1, padx=10, pady=5)

btn_enviar_taylor = Button(root, text="Calcular y Enviar Taylor", command=enviar_datos_taylor)
btn_enviar_taylor.grid(row=2, column=0, columnspan=2, pady=10)

# 📌 Sección de Fibonacci
Label(root, text="Número de términos en Fibonacci").grid(row=3, column=0, padx=10, pady=5)
entry_fibonacci = Entry(root)
entry_fibonacci.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Iniciar desde").grid(row=4, column=0, padx=10, pady=5)
entry_start = Entry(root)
entry_start.grid(row=4, column=1, padx=10, pady=5)

btn_enviar_fibonacci = Button(root, text="Calcular y Enviar Fibonacci", command=enviar_datos_fibonacci)
btn_enviar_fibonacci.grid(row=5, column=0, columnspan=2, pady=10)

# 📌 Área de texto para mostrar Fibonacci
Label(root, text="Serie Fibonacci:").grid(row=6, column=0, padx=10, pady=5)
text_area_fibonacci = Text(root, height=10, width=30)
text_area_fibonacci.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()