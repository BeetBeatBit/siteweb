from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route('/verificar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Recupera los datos ingresados por el usuario en el input
        email = request.form['email']
        password = request.form['contraseña']
        
        # Establecer la conexión a la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Daniel98@",
            database="clinica"
        )
        
        # Crear una consulta SQL para seleccionar los valores de correo y contraseña desde la tabla de usuarios
        sql = "SELECT username, password FROM users WHERE username = %s AND password = %s"
        values = (email, password)
        
        # Ejecutar la consulta SQL y obtener los resultados
        cursor = db.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        # Comparar los valores de correo y contraseña
        if result and result[0] == email and result[1] == password:
            print("Si encontre")
            error = 'Credenciales válidas. Bienvenido.'
            return render_template('/index.html', error=error)
            # Credenciales válidas, redirigir al usuario a la página de inicio de sesión
            #return redirect(url_for('inicio'))
        else:
            print("NO encontre")
            # Credenciales no válidas, mostrar un mensaje de error
            error = 'Credenciales no válidas. Intente de nuevo.'
            return render_template('/index.html', error=error)
    else:
        return render_template('/index.html', error=error)

if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0")