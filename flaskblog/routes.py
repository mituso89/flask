from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.model import User, Post


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


@app.route('/home')
def home():
    return render_template('home.html', customers=customers)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data == 'admin@blog.com' and
                form.password.data == 'password'):
            flash('You have been logged in!', 'success')
            print('dien')
            return redirect(url_for('home'))
        else:
            print('chap')
            flash('Login Unsuccessful. Please check username and password',
                  'danger')
    return render_template('login.html', title='Login', form=form)


