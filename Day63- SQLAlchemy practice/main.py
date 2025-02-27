from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

"""
# connect to the new database 
db = sqlite3.connect("Day63- SQLAlchemy practice/book-collection.db")

# cursor - to control database 
cursor = db.cursor() 
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
"""
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
# initialize the app with the extension
db = SQLAlchemy(app)
all_books = []

# define a model class, 
# This model will generate a table name 
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    author: Mapped[str]
    rating: Mapped[str]

# Create the table 
with app.app_context():
    db.create_all()
@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books = all_books)




@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)