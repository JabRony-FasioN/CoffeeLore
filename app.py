from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import psycopg2, re
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key= 'example_logister'


DB_HOST = '127.0.0.1'
DB_NAME = 'example_bd'
DB_USER = 'postgres'
DB_PASS = "password"

conn = psycopg2.connect(dbname= DB_NAME, user = DB_USER, password=DB_PASS, host= DB_HOST)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form and 'email' in request.form:
        fullname = request.form['fullname']
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']

        _hashed_password = generate_password_hash(password)


        cursor.execute('SELECT * FROM users WHERE login = %s', (login,)) 
        account = cursor.fetchone()
        print(account)

        if account:
            flash('Account alredy exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', login):
            flash('Login must contain only characters and numbers ')
        elif not login or not password or not email:
            flash("please fill out the forms!")
        else:
            cursor.execute("INSERT INTO users (fullname, login, password, email) VALUES (%s,%s,%s,%s)", (fullname, login, _hashed_password, email))
    elif request.method == "POST":
        flash('please fill out the form')
    return render_template('former.html')



if __name__ == '__main__':
    app.run(port=5005) 




    
