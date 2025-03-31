from flask import render_template, url_for, request, redirect, session
from doctest import debug
from application import app
from application.data_access import get_people, add_person
from application.forms.save_data import FavColourForm


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


# to add data to the DB and to fetch data from the view
@app.route('/database', methods=['GET', 'POST'])
def people_fav_colour():
    error = ""
    fav_colour_form = FavColourForm()

    if request.method == 'POST':
        first_name = fav_colour_form.first_name.data
        last_name = fav_colour_form.last_name.data
        colour = fav_colour_form.colour.data

        if len(first_name) == 0 or len(last_name) == 0 or len(colour) == 0:
            error = 'Please supply first name, last name and colour'

        else:
            add_person(first_name, last_name, colour)
            return redirect(url_for('people_fav_colour'))

    people_from_db = get_people()  # Fetch all data from the view
    return render_template('database.html', form=fav_colour_form, people=people_from_db, title='Database People',
                           message=error)

# @app.route('/database')
# def all_people_from_db():
#     people_from_db = get_people()
#     return render_template('database.html', people=people_from_db, title='Database People')


