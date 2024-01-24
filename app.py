from flask import Flask, request
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Models.models import Base, MovieModel, TicketsModel
from Repository.CinemaRepo import CinemaRepo
from Repository.MovieRepo import MovieRepo
from Repository.ClientRepo import ClientRepo
from Repository.TicketRepo import TicketRepo
from Repository.ScheduleRepo import ScheduleRepo
from Service.MovieService import MovieService
from Service.CinemaService import CinemaService
from Service.ClientService import ClientService
from Service.ScheduleService import ScheduleService
from Service.TicketService import TicketService
from Statistics import DatabaseStatistics
import json
import datetime

def serialize_datetime(obj):
    if isinstance(obj, (datetime.date, datetime.time)):
       return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


app = Flask(__name__)
# app.json_encoder = CustomJSONEncoder

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'CT',
    'user': 'postgres',
    'password': 'password'
}
# for creating connection string
# Create a SQLAlchemy engine to connect to the database
engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')
Base.metadata.create_all(engine)
session = Session(autocommit=False, autoflush=False, bind=engine)

movie_repo = MovieRepo(db_session=session)
movie_service = MovieService(movie_repo)

cinema_repo = CinemaRepo(db_session=session)
schedule_repo = ScheduleRepo(db_session=session)
ticket_repo = TicketRepo(db_session=session)
client_repo = ClientRepo(db_session=session)

cinema_service = CinemaService(cinema_repo)
schedule_service = ScheduleService(schedule_repo)
ticket_service = TicketService(ticket_repo)
client_service = ClientService(client_repo)


@app.route("/movies", methods=["GET"])
def get_movies():
    movies = movie_service.get_all_movies()
    movie_list = [{"id": movie.movieid, "title": movie.title} for movie in movies]
    response_data = json.dumps({"movies": movie_list}, ensure_ascii=False)
    response = app.response_class(
        response=response_data,
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response


@app.route("/cinemas", methods=["GET"])
def get_cinemas():
    cinemas = cinema_service.get_all_cinemas()
    cinema_list = [{"id": cinema.cinemaid, "name": cinema.name} for cinema in cinemas]
    return jsonify({"movies": cinema_list})


@app.route("/schedule", methods=["GET"])
def get_schedules():
    schedules = schedule_service.get_all_schedules()
    schedule_list = [
        {
            "id": schedule.scheduleid,
            "day": json.dumps(schedule.day, default=serialize_datetime),
            "starttime": json.dumps(schedule.starttime, default=serialize_datetime),
            "price": schedule.price,
            "cinema": schedule.cinema.name,
            "movie": schedule.movie.title
        }for schedule in schedules]
    response_data = json.dumps({"movies": schedule_list}, ensure_ascii=False)
    response = app.response_class(
        response=response_data,
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response


@app.route("/movies/<cid>", methods=["GET"])
def get_movies_by_cinema(cid):
    movies = movie_service.get_movies_by_cinema(cid)
    movie_list = [{"id": movie.movieid, "title": movie.title} for movie in movies]
    response_data = json.dumps({"movies": movie_list}, ensure_ascii=False)
    response = app.response_class(
        response=response_data,
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response


@app.route("/movies/genre/<genre>", methods=["GET"])
def get_movies_by_genre(genre):
    movies = movie_service.get_movies_by_genre(genre)
    movie_list = [{"id": movie.movieid, "title": movie.title, "genre": movie.genre} for movie in movies]
    response_data = json.dumps({"movies": movie_list}, ensure_ascii=False)
    response = app.response_class(
        response=response_data,
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response


@app.route("/client", methods=["POST"])
def create_client():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    if not name or not email or not phone:
        return jsonify({"error": "Missing required fields"}), 400
    try:
        new_client = client_service.add_client(name, email, phone)
        return jsonify({"clientid": new_client.clientid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ticket", methods=["POST"])
def add_ticket():
    data = request.get_json()
    cinemaid = data.get("cinemaid")
    movieid = data.get("movieid")
    clientid = data.get("clientid")
    row = data.get("row")
    column = data.get("column")
    if not cinemaid or not movieid or not clientid or not row or not column:
        return jsonify({"error": "Missing required fields"}), 400
    try:
        new_ticket = TicketsModel(cinemaid, movieid, clientid, row, column)
        ticket_service.add_ticket(new_ticket)
        return jsonify({"ticketid": new_ticket.ticketid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


db_stats = DatabaseStatistics(db_params, engine)
tables_to_analyze = ['Client', 'Cinema', 'Movie', 'Schedule', 'Tickets']

@app.route('/get_statistics/<table_name>', methods=['GET'])
def get_statistics(table_name):
    statistics = db_stats.get_table_statistics(table_name)
    return jsonify(statistics)

