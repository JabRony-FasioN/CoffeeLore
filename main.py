from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)


#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'Admin@506070'
#app.config['MYSQL_DB'] = 'tester'

#mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
   if request.method == 'POST':
    register = request.form
    return render_template('former.html', register = register)


if __name__ == '__main__':
    app.run(port=5005) 




    
