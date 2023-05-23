from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Index, Enum
from sqlalchemy.dialects.mysql import INTEGER as Integer, SMALLINT as SmallInteger

db = SQLAlchemy()

class Actor(db.Model):
    __tablename__  = 'actor'
    __table_args__ = (
        Index('idx_actor_last_name', 'last_name'),
    )
    actor_id = db.Column(Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False)

class Booking(db.Model):
    __tablename__ = 'booking'
    booking_id = db.Column(Integer, primary_key=True)
    show_id = db.Column(Integer, ForeignKey('show.show_id'), nullable=False)
    payment_id = db.Column(Integer, ForeignKey('payment.payment_id'), nullable=False)
    show = db.relationship("Show", backref="bookings")
    payment = db.relationship("Payment", backref="bookings")

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False)

class FilmActor(db.Model):
    __tablename__ = 'film_actor'
    actor_id = db.Column(Integer, ForeignKey('actor.actor_id'), primary_key=True)
    film_id = db.Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    last_update = db.Column(db.TIMESTAMP, nullable=False)
    actor = db.relationship("Actor", backref="film_actors")
    film = db.relationship("Film", backref="film_actors")

class FilmCategory(db.Model):
    __tablename__ = 'film_category'
    film_id = db.Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    category_id = db.Column(Integer, ForeignKey('category.category_id'), primary_key=True)
    last_update = db.Column(db.TIMESTAMP, nullable=False)
    film = db.relationship("Film", backref="film_categories")
    category = db.relationship("Category", backref="film_categories")

class Film(db.Model):
    __tablename__ = 'film'
    film_id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    release_year = db.Column(Integer)
    language_id = db.Column(Integer, ForeignKey('language.language_id'), nullable=False)
    original_language_id = db.Column(Integer, ForeignKey('language.language_id'))
    rental_duration = db.Column(Integer, default=3)
    rental_rate = db.Column(db.Numeric(precision=4, scale=2), default=4.99)
    length = db.Column(SmallInteger)
    replacement_cost = db.Column(db.Numeric(precision=5, scale=2), default=19.99)
    rating = db.Column(Enum('G', 'PG', 'PG-13', 'R', 'NC-17', name='film_rating_enum'), default='G')
    special_features = db.Column(db.String(255))
    last_update = db.Column(db.TIMESTAMP, nullable=False)

class Language(db.Model):
    __tablename__ = 'language'
    language_id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False)

class Payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    is_success = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(45), nullable=True)

class Room(db.Model):
    __tablename__ = 'room'
    room_id = db.Column(Integer, primary_key=True)
    number = db.Column(Integer)
    is_3D = db.Column(db.Boolean)
    rows = db.Column(Integer)
    seats = db.Column(Integer)

class Seat(db.Model):
    __tablename__ = 'seat'
    seat_id = db.Column(Integer, primary_key=True, autoincrement=True)
    room_id = db.Column(Integer, ForeignKey('room.room_id'), nullable=False)
    row = db.Column(Integer)
    column = db.Column(Integer)
    room = db.relationship("Room", backref="seat_list")

class Show(db.Model):
    __tablename__ = 'show'
    show_id = db.Column(Integer, primary_key=True)
    room_id = db.Column(Integer, ForeignKey('room.room_id'), nullable=False)
    film_id = db.Column(Integer, ForeignKey('film.film_id'), nullable=False)
    start_date = db.Column(db.Date)
    pause_time = db.Column(Integer)
    room = db.relationship("Room", backref="shows")
    film = db.relationship("Film", backref="shows")

class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticket_id = db.Column(Integer, primary_key=True)
    show_id = db.Column(Integer, ForeignKey('show.show_id'), nullable=False)
    seat_id = db.Column(Integer, ForeignKey('seat.seat_id'), nullable=False)
    booking_id = db.Column(Integer, ForeignKey('booking.booking_id'), nullable=False)
    show = db.relationship("Show", backref="tickets")
    seat = db.relationship("Seat", backref="tickets")
    booking = db.relationship("Booking", backref="tickets")
