from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE


@app.route("/")
def get_start_info():
    """ Renders home page, gets user's name to populate elsewhere on site """

    return render_template("homepage.html")

@app.route("/get-name")
def render_name():
    """ Print username """
    name = request.args.get("name")
    session["name"] = name.title()
    return redirect("/top-melons")


@app.route("/top-melons")
def show_top_melons():
    """ Renders list of most beloved melons """

    if "name" in session:
        return render_template("top-melons.html", loved_melons=MOST_LOVED_MELONS)
    else:
        flash("You haven't entered your name yet! Please try again.")
        return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0")
