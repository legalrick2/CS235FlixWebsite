
import os
from flask import Flask, redirect, url_for, render_template, request

import skeleton.utilities
import skeleton.adapters.repository as repo

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')

    repo.repoInstance = repo.MemoryRepository()

    with app.app_context():
        from .allmovies import movies
        app.register_blueprint(movies.movies_blueprint)

    @app.route("/index")
    @app.route("/home")
    @app.route("/")
    def home():
        return render_template(
            "index.html"
        )

    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            user = request.form["nm"]
            return redirect(url_for("user", usr =  user))
        else:
            return render_template("login.html")  

    @app.route("/all_genres")
    def all_genres():

        foundGenres = repo.MemoryRepository.getAllGenres(repo.repoInstance)

        return render_template(
            "genreDisplay.html",
            all_genres = foundGenres
        )

    # @app.route("/<usr>")
    # def user(usr):
    #     return f"<h1>{usr}</h1>"




    return app