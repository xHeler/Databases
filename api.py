from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from fake_data import generate_data

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'cockroachdb://root@localhost:26257/mydatabase?sslmode=disable'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost:3307/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 1


from models import *
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/actors', methods=['GET'])
def get_actors():
    actors = Actor.query.all()
    actor_list = []
    for actor in actors:
        actor_data = {
            'actor_id': actor.actor_id,
            'first_name': actor.first_name,
            'last_name': actor.last_name,
            'last_update': actor.last_update.isoformat()
        }
        actor_list.append(actor_data)
    return jsonify(actor_list)

@app.route('/actors', methods=['DELETE'])
def delete_actors():
    Actor.query.delete()
    db.session.commit()
    return jsonify({'message': 'All actors have been deleted.'})

@app.route('/film', methods=['GET'])
def get_film_by_title():
    title_query = request.args.get('title', '')
    films = Film.query.filter(Film.title.like(f'%{title_query}%')).all()
    film_list = []
    for film in films:
        film_data = {
            'film_id': film.film_id,
            'title': film.title,
            'description': film.description,
            'release_year': film.release_year,
            'language_id': film.language_id,
            'original_language_id': film.original_language_id,
            'rental_duration': film.rental_duration,
            'rental_rate': str(film.rental_rate),
            'length': film.length,
            'replacement_cost': str(film.replacement_cost),
            'rating': film.rating,
            'special_features': film.special_features,
            'last_update': film.last_update.isoformat()
        }
        film_list.append(film_data)
    return jsonify(film_list)

@app.route('/films', methods=['GET'])
def get_films():
    films = Film.query.all()
    film_list = []
    for film in films:
        film_data = {
            'film_id': film.film_id,
            'title': film.title,
            'description': film.description,
            'release_year': film.release_year,
            'language_id': film.language_id,
            'original_language_id': film.original_language_id,
            'rental_duration': film.rental_duration,
            'rental_rate': str(film.rental_rate),
            'length': film.length,
            'replacement_cost': str(film.replacement_cost),
            'rating': film.rating,
            'special_features': film.special_features,
            'last_update': film.last_update.isoformat()
        }
        film_list.append(film_data)
    return jsonify(film_list)

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    category_list = []
    for category in categories:
        category_data = {
            'category_id': category.category_id,
            'name': category.name,
            'last_update': category.last_update.isoformat()
        }
        category_list.append(category_data)
    return jsonify(category_list)

@app.route('/film-actors', methods=['GET'])
def get_film_actors():
    film_actors = FilmActor.query.all()
    film_actor_list = []
    for film_actor in film_actors:
        film_actor_data = {
            'actor_id': film_actor.actor_id,
            'film_id': film_actor.film_id,
            'last_update': film_actor.last_update.isoformat()
        }
        film_actor_list.append(film_actor_data)
    return jsonify(film_actor_list)

@app.route('/film-categories', methods=['GET'])
def get_film_categories():
    film_categories = FilmCategory.query.all()
    film_category_list = []
    for film_category in film_categories:
        film_category_data = {
            'film_id': film_category.film_id,
            'category_id': film_category.category_id,
            'last_update': film_category.last_update.isoformat()
        }
        film_category_list.append(film_category_data)
    return jsonify(film_category_list)

@app.route('/languages', methods=['GET'])
def get_languages():
    languages = Language.query.all()
    language_list = []
    for language in languages:
        language_data = {
            'language_id': language.language_id,
            'name': language.name,
            'last_update': language.last_update.isoformat()
        }
        language_list.append(language_data)
    return jsonify(language_list)

@app.route('/shows', methods=['GET'])
def get_shows():
    shows = Show.query.all()
    show_list = []
    for show in shows:
        show_data = {
            'show_id': show.show_id,
            'room_id': show.room_id,
            'film_id': show.film_id,
            'start_date': show.start_date.isoformat(),
            'pause_time': show.pause_time
        }
        show_list.append(show_data)
    return jsonify(show_list)

@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    room_list = []
    for room in rooms:
        room_data = {
            'room_id': room.room_id,
            'number': room.number,
            'is_3D': room.is_3D,
            'rows': room.rows,
            'seats': room.seats
        }
        room_list.append(room_data)
    return jsonify(room_list)

@app.route('/seats', methods=['GET'])
def get_seats():
    seats = Seat.query.all()
    seat_list = []
    for seat in seats:
        seat_data = {
            'seat_id': seat.seat_id,
            'room_id': seat.room_id,
            'row': seat.row,
            'column': seat.column
        }
        seat_list.append(seat_data)
    return jsonify(seat_list)
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    booking_list = []
    for booking in bookings:
        booking_data = {
            'booking_id': booking.booking_id,
            'show_id': booking.show_id,
            'payment_id': booking.payment_id
        }
        booking_list.append(booking_data)
    return jsonify(booking_list)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    ticket_list = []
    for ticket in tickets:
        ticket_data = {
            'ticket_id': ticket.ticket_id,
            'show_id': ticket.show_id,
            'seat_id': ticket.seat_id,
            'booking_id': ticket.booking_id
        }
        ticket_list.append(ticket_data)
    return jsonify(ticket_list)

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    payment_list = []
    for payment in payments:
        payment_data = {
            'payment_id': payment.payment_id,
            'price': str(payment.price),
            'is_success': payment.is_success,
            'description': payment.description
        }
        payment_list.append(payment_data)
    return jsonify(payment_list)

@app.route('/random', methods=['GET'])
def generate_random():
    generate_data(db, 10)
    return jsonify("Success")

@app.route('/tickets', methods=['POST'])
def book_ticket():
    # Get the data from the request
    show_id = request.json.get('show_id')
    row = request.json.get('row')
    column = request.json.get('column')
    payment_price = request.json.get('payment_price')
    payment_description = f"Payment: {show_id} - {payment_price}"

    show = Show.query.get(show_id)

    if not show:
        return jsonify({'message': 'Show not found'}), 404

    room = show.room

    if not room:
        return jsonify({'message': 'Room not found'}), 404

    seat = Seat(room_id=room.room_id, row=row, column=column)

    db.session.add(seat)
    db.session.commit()

    payment = Payment(price=payment_price, description=payment_description, is_success=True)  # Update payment details accordingly

    db.session.add(payment)
    db.session.commit()

    booking = Booking(show_id=show_id, payment_id=payment.payment_id)

    db.session.add(booking)
    db.session.commit()

    ticket = Ticket(show_id=show_id, seat_id=seat.seat_id, booking_id=booking.booking_id)

    db.session.add(ticket)
    db.session.commit()

    return jsonify({'message': 'Ticket booked successfully!', 'ticket_id': ticket.ticket_id}), 200


if __name__ == '__main__':
    migrate.init_app(app, db)
    
    app.run()
