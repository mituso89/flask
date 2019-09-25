from flask import Flask, render_template, url_for
app = Flask(__name__)


customers = [
    {
        'author': 'Mituso',
        'title': 'Real time for real line',
        'content': 'We have two connect with flask',
        'date': '2019-05-05'
    },
    {
        'author': 'Mituso',
        'title': 'Configuration NLP',
        'content': 'We will learning step by steps about machine learning',
        'date': '2019-05-05'
    }
]









@app.route("/")
def hello():
    return render_template('home.html', customers=customers)

@app.route("/about")
def about():
    return render_template('about.html', customers=customers)


@app.route('/index')
def dien():
    return render_template('homepage.html',customers=customers)


if __name__== '__main__':
    app.run(debug=True)