"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
        Hi! This is the home page. Jump to <a href="/hello">Hello</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Want a compliment?</h1>
        <form action="/greet">
            What's your name? <input type="text" name="person"><br>
            What kind of compliment do you want? 
            <select name="compliment">
              <option value = "awesome">Awesome </option>
              <option value = "terrific">Terrific </option>
              <option value = "fantastic">Fantastic </option>
              <option value = "neato">Neato </option>
              <option value = "wonderful">Wonderful </option>
              <option value = "lovely">Lovely </option>
            </select>
            <input type="submit" value="Compliment Me">
        </form>

        <h1>Want an insult??</h1>
        <form action="/diss">
            What's your name? <input type="text" name="person"><br>
            What kind of insult do you want? 
            <select name="insult">
              <option value = "a loser">A Loser</option>
              <option value = "dumb">Dumb</option>
              <option value = "ugly">Ugly</option>
            </select>
            <input type="submit" value="Insult Me">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")


    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route('/diss')
def insult_person():
    """Get user by name."""
    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
