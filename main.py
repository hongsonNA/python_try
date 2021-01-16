# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import flask
from model.model import Model
from flask import Flask, render_template

app = flask.Flask(__name__, template_folder='views')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    getListRoom = Model.listRoom()
    return render_template('chat/room_chat.html', listData=getListRoom)

if __name__ == '__main__':
    app.run()