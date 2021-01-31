from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL, TextAreaField

species = ["Cat", "Dog", "Hamster"]


class AddPet(FlaskForm):
    '''Form to add a new Pet'''

    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[(sp, sp) for sp in species])
    photo_url = StringField("Add Photo URL", validators=[URL(
        require_tld=True, message='URL is invalid, try again')])
    age = IntegerField('Age', validators=[NumberRange(
        min=0, max=30, message='Only pets from 0 to 30 months old are accepted')])
    notes = TextAreaField(
        'Type any notes here')
