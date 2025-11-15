from flask import Flask, request
from flask import render_template


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("index.html")

@app.route('/ejercicio1',methods=['GET','POST'])
def ejercicio1():
    #resultado = None
    if request.method == 'POST':
        resultado = None
        nota1= float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = ((nota1 + nota2 + nota3) / 3)
        if asistencia >=  75 and promedio >= 40:
            resultado ="APROBADO"
        else:
            resultado = "REPROBADO"
        return render_template('ejercicio1.html',nota1=nota1, nota2=nota2, nota3=nota3, promedio=promedio, asistencia=asistencia, resultado=resultado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2',methods=["GET","POST"])
def ejercicio2():
    if request.method == 'POST':
        nombre1= str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        caracteres1=len(nombre1)
        caracteres2=len(nombre2)
        caracteres3=len(nombre3)
        cantidad=''
        largo= ''

        if caracteres1 > caracteres2 and caracteres1 > caracteres3:
            largo = nombre1
            cantidad= caracteres1
        elif caracteres2 > caracteres1 and caracteres2 > caracteres3:
            largo = nombre2
            cantidad = caracteres2
        else:
            largo = nombre3
            cantidad= caracteres3

        return render_template('ejercicio2.html', nombre=largo, cantidad= cantidad, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)
    return render_template("ejercicio2.html")


if __name__ == '__main__':
    app.run(debug=True)