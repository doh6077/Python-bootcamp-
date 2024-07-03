from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager.init_app(app)



    
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method =="POST":
        password = generate_password_hash(request.form['password'], method='pbkdf2', salt_length=8)
        new_info = User(name=request.form['name'],
                        email=request.form['email'],
                        password=password)
        print(password)
        db.session.add(new_info)
        db.session.commit()
        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
       
        password = request.form['password']
        email=request.form['email']
        user = User.query.filter_by(email=email).first()

        if check_password_hash(user.password,password):
            login_user(user)
            print("The login is successfull")
            return redirect(url_for('secrets'))
                        
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
@login_required
def download():
    return app.send_static_file('files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
