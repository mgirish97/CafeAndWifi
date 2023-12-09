from flask import Flask
from flask import render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
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

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# -------------------------------- Helper Functions ----------------------------------- #
def get_rand_cafe():
    rand_cafes = db.session.query(Cafe).order_by(func.random())[:3]
    return rand_cafes


# -------------------------------- Website ----------------------------------- #


# TODO Home page

@app.route('/')
def home():
    rand_cafes = get_rand_cafe()
    print(rand_cafes)
    return render_template('index.html', rand_cafes=rand_cafes)


@app.route('/all-cafes')
def get_cafes():
    all_cafes = db.session.query(Cafe).all()
    return render_template('cafes.html', cafes=all_cafes)


# Display map of all cafes


# TODO Add cafe page

# Ask for cafe input

# Add to database


# -------------------------------- RESTful API ----------------------------------- #

# TODO GET:

# /all: Gets all cafes from database
@app.route('/all')
def get_all():
    cafes = db.session.query(Cafe).all()
    all_cafes_list = []
    for cafe in cafes:
        all_cafes_list.append(cafe.to_dict())
    return jsonify(all_cafes=all_cafes_list)

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
