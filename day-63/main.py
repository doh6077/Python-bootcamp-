from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy

#db = sqlite3.connect("books-collection.db")
#cursor = db.cursor()

#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap= Bootstrap4(app)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
all_books = []
##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'



#CREATE RECORD
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

class BookForm(FlaskForm):
    name = StringField('Book name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    global all_books
    return render_template("index.html", all_books = all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = {
            "title": form.name.data,
            "author": form.author.data,
            "rating": form.rating.data
        }
        all_books.append(book)
    print(all_books)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

