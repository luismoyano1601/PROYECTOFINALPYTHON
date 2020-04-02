#CODIGO CREADO POR LUIS MOYANO ESTUDIANTE DE IECI
import requests
from flask import Flask, render_template, jsonify, request, redirect
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors
from flask.helpers import flash, url_for
from datetime import date


mysql = MySQL()
app = Flask(__name__)
app.secret_key = "super secret key"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"]  = "vacunatorio"
mysql.init_app(app)

mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor

#MOSTRAR PACIENTES 
@app.route('/pacientes')
def pacientes():
	cursor = mysql.get_db().cursor()	
	sql = "SELECT * FROM paciente"
	cursor.execute(sql)
	pacientes_ = cursor.fetchall()
	return render_template("vacunatorio.html", pacientes = pacientes_)



#MOSTRAR VACUNAS
@app.route('/listadovacunas')
def listadovacunas():
	cursor = mysql.get_db().cursor()	
	sql = "SELECT * FROM vacuna"
	cursor.execute(sql)
	listadovacunas_ = cursor.fetchall()
	return render_template("listadovacunas.html", vacunas = listadovacunas_)





#funcion para agregar pacientes
@app.route('/agregarpacientes', methods = ['POST'])
def insertar():

    if request.method == "POST":
    
        flash("Data Inserted Successfully")
        rutpaciente = request.form['rutpaciente']
        nombrepaciente = request.form['nombrepaciente']
        fechanacimiento = request.form['fechanacimiento']
        cur =  mysql.get_db().cursor()
        cur.execute("INSERT INTO paciente (rutpaciente, nombrepaciente, fechanacimiento) VALUES (%s, %s, %s)", (rutpaciente,nombrepaciente, fechanacimiento))
        
        return redirect(url_for('pacientes'))

#FUNCION PARA AGREGAR VACUNAAAAASSSSSSSSSSSS VENGA YA
@app.route('/agregarvacunas', methods = ['POST'])
def insertarvacunas():

    if request.method == "POST":
    
        
        nombreenfermedad = request.form['nombreenfermedad']
        fechallegada = date.today()
        cur =  mysql.get_db().cursor()
        cur.execute("INSERT INTO vacuna (nombreenfermedad, fechallegada) VALUES (%s, %s)", (nombreenfermedad,fechallegada))
        
        return redirect(url_for('listadovacunas'))

#FUNCION PARA VER LAS VACUNAS QUE TIENE UN PACIENTE
@app.route('/historialvacuna/<id>')
def historial_vacuna(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT v.nombreenfermedad, v.fechavacuna  FROM vacunados v, paciente p WHERE  p.rutpaciente=v.rutpaciente".format(id) )
    recibir = cursor.fetchall()
    return render_template('pacientesconvacuna.html', vacuneitor = recibir)



#FUNCION PARA VER PACIENTES QUE TIENEN CIERTA VACUNA
@app.route('/pacientesconxvacuna/<id>')
def pacientesporvacuna(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT v.rutpaciente, p.nombrepaciente, v.fechavacuna FROM vacunados v, paciente p WHERE nombreenfermedad = %s and p.rutpaciente = v.rutpaciente",(id) )
    vacunas = cursor.fetchall()
    return render_template('pacientesconxvacuna.html', vacunados = vacunas)


#FUNCION PARA MOSTRAR NOMBRE DE VACUNAS CUANDO SE VINCULA UNA ENFERMEDAD A UN PACIENTE

@app.route('/ingresarvacuna/<id>', methods = ['POST', 'GET'])
def ingresar_vacuna(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT nombreenfermedad FROM vacuna")
    ingresarvacunas = cursor.fetchall()
    return render_template('ingresarvacunas.html', vacunas = ingresarvacunas, rut = id )

#FUNCION PARA GUARDAR LA INFORMACION EN TABLA VACUNADOS
@app.route('/registrarvacunados', methods = ['POST'])
def pacientesvacunados():
    if request.method == 'POST':
        cursor = mysql.get_db().cursor()
        rutpaciente = request.form['id']
        nombreenfermedad = request.form['vacuna']
        fechavacuna = date.today()
        cursor.execute('INSERT INTO vacunados VALUES (%s, %s, %s)', (nombreenfermedad, rutpaciente, fechavacuna))
    return redirect(url_for('pacientes'))

    

if __name__ == "__main__":
    
	app.run(debug=True)
