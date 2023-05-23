from faker import Faker
import random
from datetime import datetime
from models import *

# Create Faker instance
fake = Faker()

# Generate data for each model class
def generate_data(db, num_entries):
    # Generate Actors
    for _ in range(num_entries):
        actor = Actor(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            last_update=datetime.now()
        )
        db.session.add(actor)

    db.session.commit()

    # Generate Categories
    for _ in range(num_entries):
        category = Category(
            name=fake.word(),
            last_update=datetime.now()
        )
        db.session.add(category)
    db.session.commit()

    # Generate Languages
    for _ in range(num_entries):
        language = Language(
            name=fake.language_name(),
            last_update=datetime.now()
        )
        db.session.add(language)

    # Commit to add Actors, Categories and Languages to the DB
    db.session.commit()

    languages = Language.query.all()
    if not languages:
        raise ValueError("No languages available in the database.")
    for _ in range(num_entries):
        film = Film(
            title=fake.sentence(),
            description=fake.text(),
            release_year=fake.year(),
            language_id=random.choice(languages).language_id,
            original_language_id=random.choice(languages).language_id,
            rental_duration=random.randint(1, 10),
            rental_rate=fake.random_number(digits=2, fix_len=True),
            length=random.randint(60, 180),
            replacement_cost=fake.random_number(digits=2, fix_len=True),
            rating=random.choice(['G', 'PG', 'PG-13', 'R', 'NC-17']),
            special_features=fake.sentence(),
            last_update=datetime.now()
        )
        db.session.add(film)
    db.session.commit()
    # Generate Rooms
    db.session.commit()
    for _ in range(num_entries):
        room = Room(
            number=fake.random_number(),
            is_3D=fake.boolean(),
            rows=fake.random_int(min=1, max=20),
            seats=fake.random_int(min=1, max=20)
        )
        db.session.add(room)
    db.session.commit()

    # Generate Payments
    for _ in range(num_entries):
        payment = Payment(
            price=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            is_success=fake.boolean(),
            description=fake.text(max_nb_chars=45)
        )
        db.session.add(payment)

    # Commit to add Films, Rooms, and Payments to the DB
    db.session.commit()

    # Generate Seats
    for room in Room.query.all():
        for _ in range(room.rows * room.seats):
            seat = Seat(
                room_id=room.room_id,
                row=fake.random_int(min=1, max=room.rows),
                column=fake.random_int(min=1, max=room.seats)
            )
            db.session.add(seat)
    db.session.commit()

    # Generate Shows
    for _ in range(num_entries):
        show = Show(
            room_id=random.choice(Room.query.all()).room_id,
            film_id=random.choice(Film.query.all()).film_id,
            start_date=fake.date(),
            pause_time=fake.random_int(min=1, max=30)
        )
        db.session.add(show)
    db.session.commit()

    # Generate Bookings
    for _ in range(num_entries):
        booking = Booking(
            show_id=random.choice(Show.query.all()).show_id,
            payment_id=random.choice(Payment.query.all()).payment_id
        )
        db.session.add(booking)

    # Commit to add Seats, Shows, and Bookings to the DB
    db.session.commit()

    # Generate Tickets
    for _ in range(num_entries):
        ticket = Ticket(
            show_id=random.choice(Show.query.all()).show_id,
            seat_id=random.choice(Seat.query.all()).seat_id,
            booking_id=random.choice(Booking.query.all()).booking_id
        )
        db.session.add(ticket)
    db.session.commit()

    # Generate FilmActors
    for _ in range(num_entries):
        film_actor = FilmActor(
            actor_id=random.choice(Actor.query.all()).actor_id,
            film_id=random.choice(Film.query.all()).film_id,
            last_update=datetime.now()
        )
        db.session.add(film_actor)
    db.session.commit()

    # Generate FilmCategories
    for _ in range(num_entries):
        film_category = FilmCategory(
            film_id=random.choice(Film.query.all()).film_id,
            category_id=random.choice(Category.query.all()).category_id,
            last_update=datetime.now()
        )
        db.session.add(film_category)

    # Commit to add Tickets, FilmActors, and FilmCategories to the DB
    db.session.commit()