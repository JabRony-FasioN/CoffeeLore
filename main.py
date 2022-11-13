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
    return render_template('former.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = data_input(request.form)
    if form.validate_on_submit():
        name = form.name.data
        last_mame = form.name.data
        print(name, last_mame)
        return redirect(url_for('name'))
    return render_template('former.html', form = form)
if __name__ == '__main__':
    app.run(port=5005) 




    
