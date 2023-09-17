import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for
from persistence import init_db, auth, getAllBeachs, signup
from model import User

app = Flask(__name__)

app.config['DATABASE'] = 'turismo.db'
app.config['SECRET_KEY'] = 'root'
init_db(app)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup_handler():
    if request.method == 'POST':
        username = request.form.get('signup-username')
        password = request.form.get('signup-password')
        nome = request.form.get('signup-nome')
        profilePicture = request.files['profile-picture']

        filename = secure_filename(profilePicture.filename)
        profilePicture.save(os.path.join('static/images', filename))

        signup(app, User(username=username, password=password, nome=nome, profile_pic_path=os.path.join('static/images', filename)))
        return render_template('index.html')
    
@app.route('/login', methods=['POST'])
def login_handler():
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
