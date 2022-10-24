from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    subject = StringField("Subject")
    message = TextAreaField("Message", validators=[InputRequired()])
    submit = SubmitField("Send")