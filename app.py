from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        print('name')
        print('login')
        print('password')
        print('email')
    return render_template('former.html')



if __name__ == '__main__':
    app.run(port=5005) 




    
