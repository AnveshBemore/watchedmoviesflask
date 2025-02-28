from flask import Flask, render_template, request
import firebase_admin
import os
from firebase_admin import credentials, firestore

# Initialize Firebase app with credentials
cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
firebase_admin.initialize_app(cred) 

# Initialize Firestore DB
db = firestore.client()

app = Flask(__name__, template_folder=".")

# Your Firestore collection name
MOVIES_COLLECTION = 'watchedmovies'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        movie = request.form['name']
        genre = request.form['genre']
        ww = request.form['ww']
        sd = request.form['sd']
        fl = request.form['fl']
        
        # Data to be stored in Firestore
        movie_data = {
            'Movie': movie,
            'Genre': genre,
            'Worth_Watching': ww,
            'Special_Details': sd,
            'free_link': fl
        }

        # Add data to Firestore
        db.collection(MOVIES_COLLECTION).add(movie_data)
        
        z = movie + " " + genre + " " + ww + " " + sd + " " + fl + " added successfully"
        return render_template("success.html", msg=z)


@app.route("/view")
def view():
    app.logger.info(f"Firebase key: {cred}")

    # Retrieve all movies from Firestore
    movies_ref = db.collection(MOVIES_COLLECTION)
    movies = movies_ref.stream()

    # Convert Firestore results to a list of dictionaries
    data = []
    for movie in movies:
        movie_dict = movie.to_dict()
        movie_dict['id'] = movie.id
        data.append(movie_dict)
    return render_template("view.html", data=data)


@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/searchvalue", methods=["GET", "POST"])
def searchvalue():
    if request.method == "POST":
        search_movie = request.form["search"]

        # Query Firestore for movie by name
        movies_ref = db.collection(MOVIES_COLLECTION).where('Movie', '==', search_movie)
        movies = movies_ref.stream()

        # Convert Firestore results to a list of dictionaries
        data = []
        for movie in movies:
            movie_dict = movie.to_dict()
            movie_dict['id'] = movie.id
            data.append(movie_dict)

        return render_template("view.html", data=data)


@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deletemovie", methods=["POST", "GET"])
def deletemovie():
    if request.method == "POST":
        movie_to_delete = request.form["delmovie"]

        # Query Firestore for movie to delete
        movies_ref = db.collection(MOVIES_COLLECTION).where('Movie', '==', movie_to_delete)
        movies = movies_ref.stream()

        for movie in movies:
            # Delete movie document by ID
            db.collection(MOVIES_COLLECTION).document(movie.id).delete()

        z = movie_to_delete + " deleted successfully"
        return render_template("success.html", msg=z)


if __name__ == "__main__":
    app.run(debug=True)
