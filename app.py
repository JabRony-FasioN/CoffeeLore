from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key= 'example_logister'


DB_HOST = '127.0.0.1'
DB_NAME = 'example_bd'
DB_USER = 'postgres'
DB_PASS = "password"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        print('fullname')
        print('login')
        print('password')
        print('email')
    return render_template('former.html')



if __name__ == '__main__':
    app.run(port=5005) 




    
