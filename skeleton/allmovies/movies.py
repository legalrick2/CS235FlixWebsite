from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

import skeleton.adapters.repository as repo

movies_blueprint = Blueprint('movies_bp', __name__)

@movies_blueprint.route('/movies/display', methods=['GET'])
def display_all():
    displayType = request.args.get('search_for')
    words = request.args.get("words")
    genreName = request.args.get("genre")
    targetStartID = request.args.get('start')
    targetEndID = request.args.get('end')
    displayingPerPage = 10 #request.args.get('displaying')

    if displayType is None:
        displayType = "all"
    if words is None:
        words = ""

    if displayType == "all":
        moviesToShow = repo.MemoryRepository.getAllMovies(repo.repoInstance)
    elif displayType == "title_search":
        moviesToShow = repo.MemoryRepository.getMoviesContainingStringTitle(repo.repoInstance, words)
    elif displayType == "genre":
        moviesToShow = repo.MemoryRepository.getMoviesWithGenre(repo.repoInstance, genreName)


    if targetStartID is None:
        #Go to start if there is nothing
        targetStartID = 0
    else:
        # convert to int
        targetStartID = (int)(targetStartID)

    maxStartID = len(moviesToShow)
    if (targetStartID+displayingPerPage >= maxStartID):
        nextStartID = None
    else:
        nextStartID = targetStartID+displayingPerPage

    if(targetStartID-1 < 0): #if we are trying to go back from the very start
        prevStartID = None
    elif(targetStartID-displayingPerPage < 0):
        prevStartID = 0
    else:
        prevStartID = targetStartID-displayingPerPage


    if targetEndID is None:
        #default of 1 page
        targetEndID = targetStartID+10
    else:
        # convert to int
        targetEndID = (int)(targetEndID)
        if (targetEndID<= targetStartID):
            targetEndID = targetStartID+1 #cant go backwards

    # if displayingPerPage is None:
    #     #Go to start if there is nothing
    #     displayingPerPage = 10
    # else:
    #     # convert to int
    #     displayingPerPage = (int)(displayingPerPage)
    #     if (displayingPerPage > 50):
    #         displayingPerPage = 50 #cant dispaly more than 50 for aesthetic purposes

    moviesToShow = moviesToShow[targetStartID:targetEndID]


    if (displayType == "all"):
        nextDisplayURL = url_for('movies_bp.display_all', start=nextStartID, search_for = displayType)
        prevDisplayURL = url_for('movies_bp.display_all', start=prevStartID, search_for = displayType)
    elif displayType == "title_search":
        nextDisplayURL = url_for('movies_bp.display_all', start=nextStartID, search_for = displayType, words = words)
        prevDisplayURL = url_for('movies_bp.display_all', start=prevStartID, search_for = displayType, words = words)
    elif displayType == "genre":
        nextDisplayURL = url_for('movies_bp.display_all', start=nextStartID, search_for = displayType, genre = genreName)
        prevDisplayURL = url_for('movies_bp.display_all', start=prevStartID, search_for = displayType, genre = genreName)

    return render_template(
        "display.html",
        selected_movies = moviesToShow,
        type = displayType,
        nextStartID = nextStartID,
        prevStartID = prevStartID,
        nextDisplayURL = nextDisplayURL,
        prevDisplayURL = prevDisplayURL
    )

@movies_blueprint.route("/random_movie")
def random_movie():
    movieID = repo.MemoryRepository.getRandomMovieID(repo.repoInstance)
    return redirect(url_for("movies_bp.movie_with_ID", ID = movieID))

@movies_blueprint.route("/movie_by_name", methods=['GET'])
def movie_by_name():
    name = request.args.get("name")
    movie = repo.MemoryRepository.getMovieWithPerfectTitle(repo.repoInstance, name)
    return render_template(
        "movie.html",
        movie = movie,
    )

@movies_blueprint.route("/movie_title_search", methods=['GET'])
def movie_title_search():
    words = request.args.get("words")
    return redirect(url_for('movies_bp.display_all', search_for = "title_search", words = words))

@movies_blueprint.route("/movie_genre_search", methods=['GET'])
def movie_genre_search():
    genreName = request.args.get("genre")
    return redirect(url_for('movies_bp.display_all', search_for = "genre", genre=genreName))


@movies_blueprint.route("/movie", methods=['GET'])
def movie_with_ID():
    try:
        ID = (int)(request.args.get("ID"))
    except ValueError:
        return redirect(url_for("home"))

    movie = repo.MemoryRepository.getMovieWithID(repo.repoInstance,ID)
    return render_template(
        "movie.html",
        movie = movie,
    )


