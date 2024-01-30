from flask import render_template, Blueprint

views = Blueprint("views", __name__)


@views.route('/')
def home_page():
    return render_template('home.html')

@views.route('/menu-1')
def menu_1():
    return render_template('menu_1.html')

@views.route('/menu-2')
def menu_2():
    return render_template('menu_2.html')

@views.route('/menu-3')
def menu_3():
    return render_template('menu_3.html')

@views.route('/menu-4')
def menu_4():
    return render_template('menu_4.html')

