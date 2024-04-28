from flask import Flask, render_template
from forms import MyForm

app = Flask(__name__)
app.secret_key= 'adsadsadasdsadsadsadsadsadsadsakjgjdskl'


@app.route("/", methods=['GET','POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        return "<h1> good </h1>"
    return render_template('login.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)
