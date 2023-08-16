from flask import Flask, render_template, request, redirect, url_for
from persistence import init_db, auth, getAllBeachs
from model import User

app = Flask(__name__)

app.config['DATABASE'] = 'turismo.db'
app.config['SECRET_KEY'] = 'root'
init_db(app)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit_login', methods=['POST'])
def submit_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = auth(app, User(username, password))
        if user:
            app.user = user
            return redirect(url_for('menu'))

        return redirect(url_for('/'))


@app.route('/menu')
def menu():
    beaches = getAllBeachs()
    return render_template('menu.html', user=app.user, beaches=beaches)


if __name__ == '__main__':
    app.run(port=8080)
