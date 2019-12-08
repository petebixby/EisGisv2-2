from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField("Sign in")
    
    
class GeoCodeAddress(FlaskForm):
    fulladdress = StringField("Full Address", validators=[DataRequired])
    city = StringField("City", validators=[DataRequired])
    state = StringField("State", validators=[DataRequired])
    zipCode = StringField("Zip Code")
    submit = SubmitField("Look up")
    