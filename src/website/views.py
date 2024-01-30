from flask import render_template, Blueprint

views = Blueprint("views", __name__)


@views.route('/')
def home_page():
    return render_template('home.html')

@views.route('/membres')
def menu_1_1():
    return render_template('menu_1_1.html')

@views.route('/bureau')
def menu_1_2():
    return render_template('menu_1_2.html')

@views.route('/commissions')
def menu_1_3():
    return render_template('menu_1_3.html')

@views.route('/coachs')
def menu_1_4():
    return render_template('menu_1_4.html')

@views.route('/seances')
def menu_1_5():
    return render_template('menu_1_5.html')

@views.route('/inscription')
def menu_1_6():
    return render_template('menu_1_6.html')





@views.route('/informations')
def menu_2_1():
    return render_template('menu_2_1.html')

@views.route('/reglement')
def menu_2_2():
    return render_template('menu_2_2.html')

@views.route('/inscription_2')
def menu_2_3():
    return render_template('menu_2_3.html')

@views.route('/resultats')
def menu_2_4():
    return render_template('menu_2_4.html')

@views.route('/photos_2')
def menu_2_5():
    return render_template('menu_2_5.html')



@views.route('/photos')
def menu_3():
    return render_template('menu_3.html')

@views.route('/comite')
def menu_4():
    return render_template('menu_4.html')

