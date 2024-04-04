from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import doctor,patient
auth = Blueprint('auth',__name__)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('inputN')
        pwd = request.form.get('inputPWD')
        if(doctor.find("matricule",pwd) and doctor.find("nom",username)):
            flash('welcome', category='success')
            return redirect(url_for('views.Search'))
        else:
            flash('please retype your infos', category='error')

    return render_template("LoginPage.html")
@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/Addpatient', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        dn = request.form.get('dn')
        fnc = request.form.get('fnc')
        gn = request.form.get('gn')
        x=patient.find("nom",nom)
        if not x:
            y=patient.create(nom,prenom,dn,fnc,gn)
            if y:
                flash('Account created ', category='success')
            else:
                flash('didn\'t save ', category='success')
        else:
            flash('Account exisit ', category='success')

    return render_template("orientation.html")

@auth.route('/Search', methods=['GET', 'POST'])
def sign_Search():
     return render_template("infoPatient.html")
@auth.route('/Addpatient', methods=['GET', 'POST'])
def orienter():
     return render_template("orientation.html")

