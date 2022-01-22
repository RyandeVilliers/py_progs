from flask import Flask, session
from checker import checked_logged_in

app = Flask(__name__)

app.secret_key = 'x62xSVRCF'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are logged out'

@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'
    

@app.route('/page1')
@checked_logged_in
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
@checked_logged_in
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
@checked_logged_in
def page3() -> str:
    return 'This is page 3.'

if __name__ == '__main__':
    app.run(debug = True)
