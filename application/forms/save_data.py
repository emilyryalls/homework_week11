from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FavColourForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    colour = StringField('Favourite Colour')
    submit = SubmitField('Add Person and Colour')