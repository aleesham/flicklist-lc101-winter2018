from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    todays_movie = get_random_movie()
    tomorrows_movie = get_random_movie()

    while todays_movie == tomorrows_movie:
        tomorrows_movie = get_random_movie()

    # build the response string
    content = "<h1>Today's Movie of the Day</h1>"
    # content = content + ...
    # content = ... + content 
    content += "<ul>"
    content += "<li>" + todays_movie + "</li>"
    content += "</ul>"

    content += "<h1>Tomorrow's Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + tomorrows_movie + "</li>"
    content += "</ul>"

    # TODO 3: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    return content

def get_random_movie():
    # TODO 1: make a list with at least 5 movie titles
    movies = ["Dumb and Dumber", "Black Panther", "Se7en", "Star Wars", "Begin Again", "Die Hard"]
    # TODO 2: randomly choose one of the movies, and return it
    return random.choice(movies)


app.run()
