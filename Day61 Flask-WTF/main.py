from flask import Flask, render_template, url_for
from forms import MyForm

app = Flask(__name__)
app.secret_key= 'adsadsadasdsadsadsadsadsadsadsakjgjdskl'


@app.route("/login", methods=['GET','POST'])
def home():
    form = MyForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = form)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
