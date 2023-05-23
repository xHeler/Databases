from locust import HttpUser, task, between
from random import randrange, choice
import string


class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_actors(self):
        self.client.get("/actors")

    @task
    def get_film_by_title(self):
        letter = choice(string.ascii_letters)
        self.client.get(f"/film?title={letter}")

    @task
    def get_films(self):
        self.client.get("/films")

    @task
    def get_categories(self):
        self.client.get("/categories")

    @task
    def get_film_actors(self):
        self.client.get("/film-actors")

    @task
    def get_film_categories(self):
        self.client.get("/film-categories")

    @task
    def get_languages(self):
        self.client.get("/languages")

    @task
    def get_shows(self):
        self.client.get("/shows")

    @task
    def get_rooms(self):
        self.client.get("/rooms")

    @task
    def get_seats(self):
        self.client.get("/seats")

    @task
    def get_bookings(self):
        self.client.get("/bookings")

    @task
    def get_tickets(self):
        self.client.get("/tickets")

    @task
    def get_payments(self):
        self.client.get("/payments")

    @task
    def generate_random(self):
        self.client.get("/random")

    @task
    def book_ticket(self):
        payload = {
            'show_id': 867668162177400833,
            'row': randrange(1, 999999),
            'column': randrange(1, 999999),
            'payment_price': 10.0
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/tickets", json=payload, headers=headers)
