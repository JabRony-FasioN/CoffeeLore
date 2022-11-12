from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class data_input(FlaskForm):
    name = StringField("name:  ", validators=[DataRequired()])
    last_name = StringField("last_name:  ", validators=[DataRequired()])