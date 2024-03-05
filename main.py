from flask import Flask,render_template,request
from flask import flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from wtforms import validators
 
from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
 
@app.before_request
def before_request():
    print("before 1")
   
@app.after_request
def after_request(response):
    print("after 3")
    return response
 
@app.route("/")
def calor():
        return render_template("index.html")
   
@app.route("/alumnos")
def alumnos():
        titulo="UTL!!!"
        nombres=["mario","pedro","juan","dario"]
        return render_template("alumnos.html",titulo=titulo,nombres=nombres)
 
@app.route("/alumnos2", methods=["GET", "POST"])
def alumnos2():
 
    nom = ''
    apa = ''
    ama = ''
 
    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST'and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        print('Nombre: {}'.format(nom))
        print('Apaterno: {}'.format(apa))
        print('Amaterno: {}'.format(ama))
       
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos2.html", form=alumno_clase, nom = nom, apa = apa, ama = ama)
  
@app.route("/resultado",methods=["GET","POST"])
def resul():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return"La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
   


@app.route('/index',methods=['GET', 'POST'])
def index():
     create_form=forms.UserForm2(request.form)
     if request.method=='POST':
          alum=Alumnos(nombre=create_form.nombre.data,
                       apaterno=create_form.apaterno.data,
                       email=create_form.email.data)
          db.session.add(alum)
          db.session.commit()
     return render_template('index.html', form=create_form)

@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
     alum_form=forms.UserForm2(request.form)
     alumno=Alumnos.query.all()

     return render_template("ABC_Completo.html",alumno=alumno)

@app.route('/eliminar',methods=['GET','POST'])
def eliminar():
     create_form=forms.UserForm2(request.form)
     if request.method=='GET':
        id=request.args.get('id')
        # select *from alumnos where id== id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apaterno.data=alum1.apaterno
        create_form.email.data=alum1.email

     if request.method=='POST':
        id=create_form.id.data
        alum= Alumnos.query.get(id) 
        #delete from alumnos where id=id
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
     return render_template('eliminar.html',form=create_form)   

@app.route('/modificar',methods=['GET','POST'])
def modificar():
     create_form=forms.UserForm2(request.form)
     if request.method=='GET':
        id=request.args.get('id')
        # select *from alumnos where id== id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apaterno.data=alum1.apaterno
        create_form.email.data=alum1.email

     if request.method=='POST':
        id=create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()   
        alum1.nombre=create_form.nombre.data
        alum1.apaterno=create_form.apaterno.data
        alum1.email=create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
     return render_template('modificar.html',form=create_form) 



if __name__== "__main__":
    csrf.init_app(app)
    db.init_app(app)
    

    with app.app_context():
         db.create_all()
    app.run()