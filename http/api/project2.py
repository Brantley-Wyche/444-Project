from flask import Flask, request
from bson.objectid import ObjectId
import pymongo
import json

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.movies
    moviedb = db.movies
    mongo.server_info()
except Exception as ex:
    print("ERROR - Cannot connect to the DB")
    print(ex)


@app.route("/movie", methods=["POST"])
def create_movie():
    try:
        movie = request.get_json()
        dbResponse = moviedb.insert_one(movie)
        print(dbResponse.inserted_id)
        return Response(
            response= json.dumps(
                {
                    "_id": f"{dbResponse.inserted_id}"
                    "message": "movie created"
                }
            ),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)


@app.route("/movies", methods=["GET"])
def get_all_movies():
    try: 
        dbResponse = db.find()
        movies = list(dbResponse)
        for movie in movies:
            movie["_id"] = str(movie["_id"])
        return dbResponse
    except Exception as ex:
        print(ex)


@app.route("/movie/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    try:
        movie = db.find_one({"id": movie_id})
        return Response(
            response = json.dumps(
                {
                    "id": movie.id,
                    "title": movie.title,
                    "description": movie.description,
                    "imageURL": movie.imageURL,
                    "year": movie.year,
                    "director": movie.director,
                    "genre": movie.genre,
                    "duration": movie.duration
                }
            ),
            status=200,
            mimetpye="application/json"
        )
    except Exception as ex:
        print(ex)


@app.route("/movie/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    return "x"


@app.route("/movie/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    return "x"





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
