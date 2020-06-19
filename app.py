from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:348275723@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 
migrate = Migrate(app, db)


class Article(db.Model):
    __tablename__ = "Article"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    intro = db.Column(db.String(300), nullable = False)
    text = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles = articles)

@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post.html', article = article)

@app.route('/posts/<int:id>/del')
def post_del(id):
    article = Article.query.get_or_404(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts') 
    except:
        return 'Произошла ошибка удаления'

    
    return render_template('post.html', article = article)

@app.route('/posts/<int:id>/update',methods = ['POST', "GET"])
def post_update(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/posts')

        except:
            return 'Неудалось изменить'

    else:
        article = Article.query.get(id)
        return render_template('post_update.html', article = article)

@app.route('/create-article', methods = ['POST', "GET"])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title= title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')

        except:
            return 'Неудалось добавить'

    else:
        return render_template('create-article.html')


if __name__ == "__main__":
    app.run(debug=True)