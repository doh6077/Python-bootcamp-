from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    print("this is length", cafes)
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

@app.route("/all")
def get_all():
    cafes_all=[]
    cafes = db.session.query(Cafe).all()
    for i in cafes:
        cafe = {
        "id": i.id,
        "name": i.name,
        "map_url": i.map_url,
        "img_url": i.img_url,
        "location": i.location,
        "seats": i.seats,
        "has_toilet": i.has_toilet,
        "has_wifi": i.has_wifi,
        "has_sockets": i.has_sockets,
        "can_take_calls": i.can_take_calls,
        "coffee_price": i.coffee_price,
        }
        cafes_all.append(cafe)
    
    return jsonify(cafes_all)

@app.route("/serach/<location>", methods=['GET','POST'])
def search(location):
    cafes = Cafe.query.filter_by(location=location)
    cafes_all=[]
    for i in cafes:
        cafe = {
        "id": i.id,
        "name": i.name,
        "map_url": i.map_url,
        "img_url": i.img_url,
        "location": i.location,
        "seats": i.seats,
        "has_toilet": i.has_toilet,
        "has_wifi": i.has_wifi,
        "has_sockets": i.has_sockets,
        "can_take_calls": i.can_take_calls,
        "coffee_price": i.coffee_price,
        }
        cafes_all.append(cafe)
    
    return jsonify(cafes_all)
# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record



if __name__ == '__main__':
    app.run(debug=True)
