from flask import Flask, request
app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Flicklist</title>
    </head>
    <body>
        <h1>Flicklist</h1>
"""

page_footer = """
    </body>
</html>
"""

@app.route('/')
def index():
    edit_head = "<h3>Edit my Watchlist</h3>"
    add_form = """
    <form action = "/add" method = "post">
        I want to add 
        <input type="text" name="new-movie" />
        to my watchlist.
        <input type="submit" value = "Add It"/>
    </form>

    """
    return page_header + edit_head + add_form + page_footer

@app.route("/add", methods = ["POST"])
def add():
    new_movie = request.form['new-movie']
    content = "<p><strong>{new_movie}</strong> has been added to your watchlist.</p>"
    return page_header + content.format(new_movie = new_movie) + page_footer

app.run()