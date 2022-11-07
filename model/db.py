from flask_mysqldb import MySQL
from app import app
from MySQLdb import Cursor


#conexion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'coltis_movie_flask'
app.config['MYSQL_PORT'] = '3307'

mysql = MySQL(app)

#execute inicializa la tarea, me devuelve la informacion
def execute(sql: str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    return cursor

def commit():
    mysql.connection.commit()
    


