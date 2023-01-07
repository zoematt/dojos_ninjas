from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():

    return render_template("dojos.html", dojos = Dojo.get_all())

@app.route('/dojo_new', methods=['post'])
def dojo_new():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def get_one(id):
    dojo_data = {
        "id": id
    }
    one_dojo=Dojo.get_one(dojo_data)
    return render_template('dojo_show.html', one_dojo= one_dojo)




