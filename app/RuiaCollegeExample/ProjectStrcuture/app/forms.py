from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required


# It contains forms as well imports required specifically for forms
class NameForm(Form):
   name= TextField('What is your name? ', validators= [ Required()])
