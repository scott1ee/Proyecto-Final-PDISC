from flask_socketio import SocketIO
from flask import Flask, jsonify, request, render_template
#from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
import config

app = Flask(__name__)
#login_manager = LoginManager()
#login_manager.init_app(app)
app.config['MYSQL_HOST']='192.168.43.35'
app.config['MYSQL_USER'] ='pruebas'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='usuarios'
app.config['SECRET_KEY'] = 'secret'
app.debug=True
socketio= SocketIO(app,cors_allowed_origins="*",async_mode=None)
conexion=MySQL(app)

#renderiza los templates HTML para la visualizacion de la pagina

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviarDatos', methods=['POST'])
def enviarDatos():
   cursor=conexion.connection.cursor()
   nombre = request.form['nombre']
   contrasena = request.form["contrasena"]
   correo = request.form["correo"]
   print(nombre, contrasena, correo)
   sql="INSERT INTO `usuarios`(`usuario`, `contrasena`, `correo`) VALUES ('<{id}>','{0}','{1}','{2}')".format(nombre,contrasena,correo)
   cursor.execute(sql)
   conexion.connection.commit()
   return jsonify({"respuestas":"OK"})

if __name__ == '__main__' :
    app.run(host="0.0.0.0", port=5001)
