from flask import render_template, redirect, request
from pymdb import app, db
from pymdb.models import Movie


@app.route('/')
def index():
    movies = db.session.query(Movie).all()
    return render_template("movies/index.html", movies=movies)


@app.route('/movies/new')
def new_movie():
    return render_template("movies/new.html")


@app.route('/movies/create', methods=['POST'])
def create_movie():
    movie = Movie(**request.form.to_dict())
    db.session.add(movie)
    db.session.commit()
    return redirect('/')


@app.route('/movies/edit/<int:id>')
def edit_movie(id):
    movie = db.session.query(Movie).get(id)
    return render_template('movies/edit.html', movie=movie)


@app.route('/movies/update/<int:id>', methods=['POST'])
def update_movie(id):
    movie = db.session.query(Movie).get(id)
    movie.name = request.form.get('name')
    movie.rating = request.form.get('rating')
    db.session.commit()
    return redirect('/')


@app.route('/movies/remove/<int:id>')
def remove_movie(id):
    movie = db.session.query(Movie).get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
