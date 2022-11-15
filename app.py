import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
