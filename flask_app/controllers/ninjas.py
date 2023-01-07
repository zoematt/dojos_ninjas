from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():

    return render_template('ninja.html', dojos = Dojo.get_all())

@app.route('/process', methods=['post'])
def ninja_new():
    Ninja.create(request.form)
    return redirect('/dojos')