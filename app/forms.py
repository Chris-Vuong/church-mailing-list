from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FormField, SubmitField
from wtforms.validators import DataRequired, Email

class EmailContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')