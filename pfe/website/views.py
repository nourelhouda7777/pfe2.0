from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("LoginPage.html")
@views.route('/Search')
def Search():
    return render_template("Search.html")
