from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Hardcoded employee credentials (in a real app, use a database)
employees = {
    'employee1': {'password': 'password1'},
    'employee2': {'password': 'password2'}
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in employees and employees[username]['password'] == password:
        return f'Logged in as {username}'
    else:
        return 'Invalid credentials. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)

