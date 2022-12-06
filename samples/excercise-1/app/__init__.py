from flask import Flask, render_template, request

movies = {
    "ddlj": {
        "name": "Dilwale Dulhania Le Jayenge",
        "hero": "Shah Rukh Khan",
        "heroine": "Kajol",
    },
    "kgf": {
        "name": "KGF",
        "hero": "Yash",
        "heroine": "Srinidhi Shetty",
    },
    "harrypotter": {
        "name": "Harry Potter",
        "hero": "Daniel Radcliffe",
        "heroine": "Emma Watson",
    },
    "pk": {
        "name": "PK",
        "hero": "Aamir Khan",
        "heroine": "Anushka Sharma",
    },
    "3idiots": {
        "name": "3 Idiots",
        "hero": "Aamir Khan",
        "heroine": "Kareena Kapoor",
    },
}


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello World"

    # dynamic route
    @app.route('/cars/<string:car_id>')
    def car(car_id):
        return f"Car ID: {car_id}"

    # parameterized route
    @app.route('/movies')
    def movie():
        name = request.args.get('name')

        if name is None:
            return "Please provide a movie name"

        if name not in movies:
            return "Movie not found"

        if name in movies:
            return movies[name]

    return app
