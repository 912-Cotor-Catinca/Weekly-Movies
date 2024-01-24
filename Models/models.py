from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Time, Date, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class CinemaModel(Base):
    __tablename__ = 'cinema'
    cinemaid = Column(Integer, primary_key=True)
    name = Column(String(255))
    rows = Column(Integer)
    columns = Column(Integer)


class MovieModel(Base):
    __tablename__ = 'movie'
    movieid = Column(Integer, primary_key=True)
    cinemaid = Column(Integer, ForeignKey('cinema.cinemaid'))
    title = Column(String(255))
    director = Column(String(255))
    genre = Column(String)
    duration = Column(Integer)
    cinema = relationship("CinemaModel", back_populates="movie")


class ScheduleModel(Base):
    __tablename__ = 'schedule'
    scheduleid = Column(Integer, primary_key=True)
    day = Column(Date)
    starttime = Column(Time)
    price = Column(Integer)
    cinemaid = Column(Integer, ForeignKey('cinema.cinemaid'))
    movieid = Column(Integer, ForeignKey('movie.movieid'))

    cinema = relationship("CinemaModel", back_populates="schedule")
    movie = relationship("MovieModel", back_populates="schedule")


class ClientModel(Base):
    __tablename__ = 'client'
    clientid = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))


class TicketsModel(Base):
    __tablename__ = 'tickets'
    ticketid = Column(Integer, primary_key=True)
    cinemaid = Column(Integer, ForeignKey('cinema.cinemaid'))
    movieid = Column(Integer, ForeignKey('movie.movieid'))
    clientid = Column(Integer, ForeignKey('client.clientid'))
    row = Column(Integer)
    seat_nr = Column(Integer)

    cinema = relationship("CinemaModel", back_populates="tickets")
    movie = relationship("MovieModel", back_populates="tickets")
    client = relationship("ClientModel", back_populates="tickets")


CinemaModel.movie = relationship("MovieModel", back_populates="cinema")
CinemaModel.schedule = relationship("ScheduleModel", back_populates="cinema")
MovieModel.schedule = relationship("ScheduleModel", back_populates="movie")
CinemaModel.tickets = relationship("TicketsModel", back_populates="cinema")
MovieModel.tickets = relationship("TicketsModel", back_populates="movie")
ClientModel.tickets = relationship("TicketsModel", back_populates="client")