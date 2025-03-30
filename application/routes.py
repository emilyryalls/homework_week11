from flask import render_template, url_for, request, redirect, session
from doctest import debug
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/ivon')
def ivon():
    return render_template('ivon.html', title='Ivon')

@app.route('/anna')
def anna():
    return render_template('anna.html', title='Anna')

@app.route('/emily')
def emily():
    return render_template('emily.html', title='Emily')

@app.route('/malvina')
def malvina():
    return render_template('malvina.html', title='Malvina')

@app.route('/ayishat')
def ayishat():
    return render_template('ayishat.html', title='Ayishat')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('input_data')
    return render_template('submit.html', title='Submit', message=data)

