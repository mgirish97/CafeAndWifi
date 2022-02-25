from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from typing import Callable


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String, nullable=False)

# -------------------------------- Website ----------------------------------- #


# TODO Home page
all_cafes = db.session.query(Cafe).all()


@app.route('/')
def home():
    return render_template('index.html', cafes=all_cafes)

# Show all cafes

# Display map of all cafes


# TODO Add cafe page

# Ask for cafe input

# Add to database


# -------------------------------- RESTful API ----------------------------------- #

# TODO GET:

# /all: Gets all cafes from database


print(db.session.query(Cafe).all())

# /search: Get all cafes in a particular location or name

# /random: Get a random cafe from the database


# TODO POST:

# /add: Add new cafe to database


# TODO PATCH:

# /update-price/<cafe_id>: Updates price of coffee based on id.


# TODO DELETE:

# /report-closed/<cafe_id>: Deletes cafe from database


if __name__ == '__main__':
    app.run(debug=True)
