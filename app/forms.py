from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Email, DataRequired

class ContactForm(FlaskForm):
  name = StringField(validators=[DataRequired()], description='Your Name *')
  email = StringField(validators=[DataRequired(), Email()], description='Your Email *')
  phone = IntegerField()
  subject = StringField()
  message = TextAreaField(validators=[DataRequired()])
  submit = SubmitField('SEND MESSAGE')