from flask import render_template, request, Blueprint, url_for
from flaskblog.model import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    posts = Post.query.all()
    return render_template('about.html', posts=posts)
