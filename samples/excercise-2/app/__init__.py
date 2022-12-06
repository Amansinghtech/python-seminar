from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/signup')
    def signup():
        return render_template('signup.html', title='Sign Up')

    @app.route('/login')
    def login():
        return render_template('login.html', title='Login')

    @app.route('/home')
    def home():
        return render_template('home.html', title='Home')

    return app
