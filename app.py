from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"
debug = DebugToolbarExtension(app)


@app.route('/home')
def madlib_form():
    """function that displays form on /home route when user gets to webpage"""
    prompts = story.prompts
    return render_template("home.html",prompts=prompts)

@app.route('/story')
def add_story():
    """shows the story result"""

    the_story = story.generate(request.args)
    return render_template("story.html", text=the_story)

