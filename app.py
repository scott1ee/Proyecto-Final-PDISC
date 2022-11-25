from flask_socketio import SocketIO
from flask import Flask, jsonify, request, render_template, redirect
#from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
import config
from flask_cors import CORS, cross_origin

app = Flask(__name__)

#login_manager = LoginManager()
# login_manager.init_app(app)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins="*", async_mode=None)
conexion = MySQL(app)

# renderiza los templates HTML para la visualizacion de la pagina


@app.route('/login')
def login():
    nombre = 'sa'
    contrasena = 'asd'
    correo = 'asd@gmail.com'
    return redirect('http://g6.pwd.tecnica4berazategui.edu.ar/qery/alta.php?nombre='+nombre + '&&contrasena='+contrasena+'&&correo='+correo)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/enviarDatos', methods=['POST'])
def enviarDatos():
    nombre = request.form['nombre']
    contrasena2 = request.form["contrasena2"]
    correo = request.form["correo"]
    print(nombre, contrasena2, correo)
    return redirect('http://g6.pwd.tecnica4berazategui.edu.ar/qery/alta.php?nombre='+nombre + '&&contrasena='+contrasena2+'&&correo='+correo)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
