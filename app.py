from flask import Flask
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Models.models import Base, MovieModel
from Repository.MovieRepo import MovieRepo
from Service import MovieService

app = Flask(__name__)

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'cinema',
    'user': 'postgres',
    'password': 'parola'
}
# for creating connection string
# Create a SQLAlchemy engine to connect to the database
engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')
Base.metadata.create_all(engine)
session = Session(autocommit=False, autoflush=False, bind=engine)

movie_repo = MovieRepo(db_session=session)
movie_service = MovieService(movie_repo)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/mata")
def hello_mata():
    return "Hello, mata!"

@app.route("/movies", methods=["GET"])
def get_movies():
    movies = movie_service.get_all_movies()
    movie_list = [{"id": movie.id, "title": movie.title} for movie in movies]
    return jsonify({"movies": movie_list})
