from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Length,Email

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('PassWord',validators=[Required()])
    remember_me = BooleanField('Keep Me Login In')
    submit = SubmitField('Login In')
