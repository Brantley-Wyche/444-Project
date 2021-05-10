from flask import Flask, request, Response
from bson.objectid import ObjectId
import pymongo, json

app = Flask(__name__)

# Connect to the database
try:
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS=1000)
    
    # Database
    db = mongo.movies

    # Container
    moviedb = db.movies

    mongo.server_info()

except Exception as ex:
    print("ERROR - Cannot connect to the DB")
    print(ex)


# CREATE MOVIE
@app.route("/movie", methods=["POST"])
def create_movie():
    try:
        movie = request.get_json()
        dbResponse = moviedb.insert_one(movie)
        return Response(
            response=json.dumps({"_id":f"{dbResponse.inserted_id}", "message":"movie created"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        send_error_response("Cannot create movie")


# GET ALL MOVIES
@app.route("/movies", methods=["GET"])
def get_all_movies():
    try: 
        dbResponse = moviedb.find()
        movies = list(dbResponse)

        # Convert movie id to a json serializable string
        for movie in movies:
            movie["_id"] = str(movie["_id"])

        return Response(
            response=json.dumps(movies),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        send_error_response("Cannot read movies")


# GET A MOVIE
@app.route("/movie/<movie_id>", methods=["GET"])
def get_movie(movie_id):
    try:
        movie = moviedb.find_one({"_id": movie_id})
        print(movie)
        return Response(
            response = json.dumps(movie),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        send_error_response("Cannot find movie")


# UPDATE A MOVIE
@app.route("/movie/<movie_id>", methods=["PUT"])
def update_movie(movie_id):
    try:
        movie = request.get_json()
        dbResponse = moviedb.update_one(
            {"_id":ObjectId(movie_id)},
            {"$set":{movie}}
        )
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps({
                    "message":"movie updated",
                    "movie":movie
                }),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({
                    "message":"nothing to update"
                }),
                status=200,
                mimetype="application/json"
            )

    except Exception as ex:
        print(ex)
        send_error_response("Cannot update movie")


# DELETE A MOVIE
@app.route("/movie/<movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    try:
        dbResponse = moviedb.delete_one({"_id":ObjectId(movie_id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps({
                    "message":"movie deleted",
                    "_id":f"{movie_id}"
                }),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({
                    "message":"no movie deleted"
                }),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        send_error_response("Cannot delete movie")


# function to send an error response
def send_error_response(message):
    return Response(
        response=json.dumps({"message":message}),
        status=500,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
