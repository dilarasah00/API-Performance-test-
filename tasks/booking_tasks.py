from locust import task, SequentialTaskSet
from endpoints.auth import login
from endpoints.booking import create_booking, get_booking, delete_booking
from utils.data_factory import random_booking_data

class BookingTasks(SequentialTaskSet):

    token = None

    def on_start(self):
        
        if not BookingTasks.token:
            BookingTasks.token = login(self.client)
        self.token = BookingTasks.token

       
        self.booking_id = None

    @task(3)
    def create_booking_task(self):
        self.booking_data = random_booking_data()
        self.booking_id = create_booking(self.client, self.booking_data)

    @task(2)
    def get_booking_task(self):
        if self.booking_id:
            get_booking(self.client, self.booking_id)

    @task(1)
    def delete_booking_task(self):
        if self.booking_id and self.token:
            delete_booking(self.client, self.booking_id, self.token)
            self.booking_id = None  
