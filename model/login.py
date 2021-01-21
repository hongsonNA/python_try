from model.model import Model
from db.connect_db import connection
import base64
import json
import hashlib
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
# from flask import render_template, jsonify, request, flash
import bcrypt

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class Login(Model):
    primary_key = 'user_id'
    table_name_model = 'user'
    def createUser(self, data):
        username = data['user_name']
        passowrd = data['password'].encode('utf-8')
        passwordHash = bcrypt.hashpw(passowrd, bcrypt.gensalt())
        passwordDecoce = passwordHash.decode('utf-8').replace(" ", "")

        dataparam = {
                'user_name': username,
                'password': passwordDecoce
            }
        # createData = Model.insertData(self, dataparam, Login.table_name_model) " and password="'+passwordDecoce+'"
        query = 'where user_name="'+str(username)+'" limit 1  '
        accountLogin = Model.selectData(self, query, Login.table_name_model)
        if not accountLogin:
            mes = {
                'status' : False,
                'message' : 'Not found data'
            }
        else:
            mes = {
                'status': True,
                'message': 'Login Success'
            }
        return mes
        # getOne = Model.selectOne(self,Login.table_name_model, Login.primary_key, 15)
        return createData
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