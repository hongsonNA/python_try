import flask
from handle.handleMessageSocket import handleMessageSocket
from flask import render_template, jsonify, request, flash
from model.login import LoginForm
# from flask import Flask, request, Response, jsonify
import  requests
from model.login import Login
app = flask.Flask(__name__, template_folder='views')
app.config["DEBUG"] = True

class Controller:
    def home(self):
        handle_socket = handleMessageSocket.getIpClient(self='')
        return handle_socket
    def login(self):
        form = LoginForm()
        # data = {}
        # return  form.password.data
        data = {}
        if form.validate_on_submit():
            flash('Yeu cau dang nhap tu user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        if form.validate_on_submit() and form.username:
            data = {
                    'user_name': form.username.data,
                    'password': form.password.data,
                }
            login = Login.createUser(self, data)
            return login
        # return form.validate_on_submit()


        return render_template('login/login.html', form=form)