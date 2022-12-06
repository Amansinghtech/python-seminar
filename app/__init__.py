from flask import Flask, render_template, request, redirect, url_for


usersData = {
    'admin': {
        'username': 'admin',
        'password': 'admin',
        'email': 'admin@anb.com'
    },
    'siddhant': {
        'username': 'siddhant',
        'password': 'sid@123',
        'email': 'sid@gmail.com'
    }
}


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():

        form_data = request.form

        username = form_data.get('username')
        email = form_data.get('email')
        password = form_data.get('password')
        confirm_password = form_data.get('confirm')

        if request.method == 'POST':
            if not len(username) or username == '':
                return render_template('signup.html', title='Sign Up', error={"message": 'Username is required'})

            if not len(email) or email == '':
                return render_template('signup.html', title='Sign Up', error={"message": 'Email is required'})

            if not len(password) or password == '':
                return render_template('signup.html', title='Sign Up', error={"message": 'Password is required'})

            if not len(confirm_password) or confirm_password == '':
                return render_template('signup.html', title='Sign Up', error={"message": 'Confirm Password is required'})

            if password != confirm_password:
                return render_template('signup.html', title='Sign Up', error={"message": 'Password and Confirm Password must match'})

            # check if user already exists

            if username in usersData:
                return render_template('signup.html', title='Sign Up', error={"message": 'User already exists'})

            usersData[username] = {
                "username": username,
                "password": password,
                "email": email
            }

            print(usersData)
            return render_template('signup.html', title='Sign Up', success={"message": 'User created successfully'})

        return render_template('signup.html', title='Sign Up')

    @app.route('/login', methods=['GET', 'POST'])
    def login():

        if request.method == 'POST':
            form_data = request.form

            username = form_data.get('username')
            password = form_data.get('password')

            if not len(username) or username == '':
                return render_template('login.html', title='Login', error={"message": 'Username is required'})

            if not len(password) or password == '':
                return render_template('login.html', title='Login', error={"message": 'Password is required'})

            if username not in usersData:
                return render_template('login.html', title='Login', error={"message": 'Username or password incorrect'})

            if usersData[username]['password'] != password:
                return render_template('login.html', title='Login', error={"message": 'Username or password incorrect'})

            return redirect(url_for('home'))

        return render_template('login.html', title='Login')

    @app.route('/home')
    def home():
        users = []
        for user in usersData:
            print(user)
            users.append(usersData[user])

        return render_template('home.html', title='Home', users=users)

    return app
