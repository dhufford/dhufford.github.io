from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/construct')
def construct():
    return render_template('construct.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:author>/')
def article(author):
    return render_template('article.html', author=author)


if __name__ == '__main__':
    app.run(debug=True)
