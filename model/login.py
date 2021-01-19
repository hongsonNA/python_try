from model.model import Model

import base64
import json
import hashlib
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import bcrypt

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class Login(Model):
    def createUser(self, data):
        # query = Model.create(self, data, table_name).
        enC = data['password'].encode('utf-8')
        password = bcrypt.hashpw(enC, bcrypt.gensalt())
        return password
        sql = "INSERT INTO user (user_name,password) VALUES (?,?)"
        data_insert = (data['user_name'], data['password'])
        return sql
    def form(self):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember_me = BooleanField('Remember me')
        submit = SubmitField('Sign In')
    pass

    #
    # def check_encrypted_password(password, hashed):
    #     decoded = base64.b64decode(password)
    #     return decoded