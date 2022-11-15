import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3

# reminder to import sqlite when i do the db
# also remember to import sessions for cookies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "idk"
        # check against the db
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return "idk"
    else:
        return render_template("register.html")

@app.route('/submit',methods=['POST'])
def submit():
    return ""

if __name__ == '__main__':
    app.run()