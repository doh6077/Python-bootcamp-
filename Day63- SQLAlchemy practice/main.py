from flask import Flask, render_template, request, redirect, url_for
import sqlite3 

# connect to the new database 
db = sqlite3.connect("Day63- SQLAlchemy practice/book-collection.db")

# cursor - to control database 
cursor = db.cursor() 
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books = all_books)




@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        
        #NOTE: You can use the redirect method from flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
      
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)