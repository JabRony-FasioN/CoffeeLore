from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class MessageForm(FlaskForm):
    name = StringField("name:  ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField("submit")