# **📌 Proyecto: Implementación de Series Matemáticas con Flask y Visualización en Tiempo Real**

## **📖 Descripción del Proyecto**
Este proyecto implementa y analiza dos series matemáticas fundamentales: **Serie de Taylor** (para seno y coseno) y **Serie de Fibonacci**. Utiliza **Flask** como backend para la gestión de datos en una base de datos **MySQL** y un **dashboard en Python con Plotly** para la visualización en tiempo real de los cálculos. 

El sistema permite:
- **Insertar datos** en la base de datos desde una aplicación cliente.
- **Recuperar datos** almacenados y visualizarlos en gráficos dinámicos.
- **Actualizar en tiempo real** el dashboard sin necesidad de recargar la página.

---

## **📌 Tecnologías Utilizadas**
✅ **Python** - Lenguaje principal del proyecto.  
✅ **Flask** - Framework para el backend y manejo de APIs REST.  
✅ **MySQL** - Base de datos relacional para almacenamiento de datos.  
✅ **Plotly** - Librería de visualización interactiva.  
✅ **Tkinter** - Para la interfaz gráfica en la aplicación cliente.  
✅ **Datetime** - Manejo de fechas y horas en la inserción y visualización de datos.  
✅ **GitHub** - Control de versiones y colaboración.  

---

## **📌 Estructura del Proyecto**

📂 **proyecto_series_matematicas**  
 ├── 📂 **backend** *(Contiene el servidor Flask y las APIs para el manejo de datos)*  
 │   ├── `server.py` *(Archivo principal con las rutas de la API Flask)*  
 │   ├── `database.py` *(Configuración de la conexión a MySQL)*  
 │   ├── `requirements.txt` *(Lista de dependencias del proyecto)*  
 │   └── 📂 **static** *(Archivos auxiliares, si se requieren)*  
 │
 ├── 📂 **frontend** *(Contiene la aplicación en Tkinter y el dashboard en Plotly)*  
 │   ├── `app_tkinter.py` *(Aplicación cliente para enviar datos a Flask)*  
 │   ├── `dashboard.py` *(Dashboard de visualización con Plotly)*  
 │   └── 📂 **assets** *(Recursos gráficos y estilos, si se requieren)*  
 │
 ├── `README.md` *(Este documento)*  
 ├── `.gitignore` *(Archivos y carpetas a ignorar en Git)*  
 └── `LICENSE` *(Licencia del proyecto, si aplica)*  

---

## **📌 Instalación y Configuración**

### **1️⃣ Requisitos Previos**
Asegúrate de tener instalado en tu sistema:
- Python 3.8 o superior.
- MySQL Server.
- Pip para instalar dependencias.

### **2️⃣ Clonar el Repositorio**
```bash
# Clonar el repositorio desde GitHub
git clone https://github.com/tu_usuario/proyecto_series_matematicas.git
cd proyecto_series_matematicas
```

### **3️⃣ Configurar la Base de Datos**
1. Crear la base de datos en MySQL:
```sql
CREATE DATABASE s_matematicas;
```
2. Importar la estructura de las tablas:
```sql
USE s_matematicas;

CREATE TABLE coseno (
    id INT PRIMARY KEY AUTO_INCREMENT,
    costaylor FLOAT NOT NULL,
    cosmath FLOAT NOT NULL,
    error FLOAT NOT NULL,
    sentaylor FLOAT NOT NULL,
    senmath FLOAT NOT NULL,
    error_seno FLOAT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fibonacci (
    id INT PRIMARY KEY AUTO_INCREMENT,
    posicion INT NOT NULL,
    valor BIGINT NOT NULL,
    error FLOAT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **4️⃣ Instalar Dependencias**
Ejecuta el siguiente comando dentro del proyecto:
```bash
pip install -r requirements.txt
```

### **5️⃣ Ejecutar el Servidor Flask**
```bash
cd backend
python server.py
```
El servidor Flask estará corriendo en `http://127.0.0.1:5000/`.

### **6️⃣ Ejecutar la Aplicación Cliente (Tkinter)**
```bash
cd frontend
python app_tkinter.py
```

### **7️⃣ Ejecutar el Dashboard**
```bash
python dashboard.py
```
Abre tu navegador y accede a `http://127.0.0.1:5000/visualizacion_taylor` para ver los gráficos en tiempo real.

---

## **📌 Funcionalidades**

### **🔹 API Endpoints (Flask)**
📌 **Insertar Datos en la Tabla `coseno`**
```http
POST /insertar_datos
```
**Ejemplo JSON:**
```json
{
    "datos": [
        {"costaylor": 0.98, "cosmath": 1.0, "error": 0.02, "sentaylor": 0.02, "senmath": 0.0, "error_seno": 0.02}
    ]
}
```

📌 **Consultar Datos de Taylor**
```http
GET /datos_taylor
```
📌 **Consultar Datos de Fibonacci**
```http
GET /datos_fibonacci
```

### **🔹 Visualización en el Dashboard**
- Gráficos dinámicos de **coseno, seno y errores** de la serie de Taylor.
- Gráficos de **valores y razones de la serie de Fibonacci**.
- Última actualización mostrada en tiempo real.

---

## **📌 Contribución**
Si deseas contribuir, sigue estos pasos:
1. **Haz un fork** del repositorio.
2. **Crea una rama nueva** para tu contribución:
   ```bash
   git checkout -b feature-mi-mejora
   ```
3. **Haz cambios y confírmalos:**
   ```bash
   git commit -m "Agregada nueva funcionalidad X"
   ```
4. **Sube los cambios a tu fork y haz un pull request.**

---

## **📌 Contacto y Enlace del Repositorio**
Repositorio en GitHub: **[https://github.com/tu_usuario/proyecto_series_matematicas](https://github.com/tu_usuario/proyecto_series_matematicas)**

📩 Para dudas o soporte, contactar a: **pamela.valenzuela.f@ucb.edu.bo**

---

## **📌 Licencia**
Este proyecto está licenciado bajo la **MIT License** – consulta el archivo `LICENSE` para más detalles.

🚀 **¡Gracias por contribuir y aprender con nosotros!** 🚀
