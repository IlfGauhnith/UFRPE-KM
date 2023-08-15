from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print("username: " + username)
        print("password: " + password)

        return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(port=8080)